from django.db import models


class UserProfile(models.Model):
    """
    用户信息
    """
    name = models.CharField(u'姓名', max_length=32)
    email = models.EmailField(u'邮箱')
    phone = models.CharField(u'座机', max_length=32, null=True, blank=True)
    mobile = models.CharField(u'手机', max_length=32)

    class Meta:
        verbose_name_plural = "用户表"

    def __str__(self):
        return self.name

class AdminInfo(models.Model):
    """
    用户登陆相关信息
    """
    user_info = models.OneToOneField("UserProfile")
    username = models.CharField(u'用户名', max_length=64)
    password = models.CharField(u'密码', max_length=64)

    class Meta:
        verbose_name_plural = "管理员表"

    def __str__(self):
        return self.user_info.name

class UserGroup(models.Model):
    """
    用户组
    """
    name = models.CharField(max_length=32, unique=True)
    users = models.ManyToManyField('UserProfile')

    class Meta:
        verbose_name_plural = "用户组表"

    def __str__(self):
        return self.name

class BusinessUnit(models.Model):
    """
    业务线
    """
    name = models.CharField('业务线', max_length=64, unique=True)
    contact = models.ForeignKey('UserGroup', verbose_name='业务联系人', related_name='c')
    manager = models.ForeignKey('UserGroup', verbose_name='系统管理员', related_name='m')

    class Meta:
        verbose_name_plural = "业务线表"

    def __str__(self):
        return self.name

class CPU(models.Model):

    asset = models.OneToOneField('Asset')
    cpu_model = models.CharField(u'CPU型号', max_length=128,blank=True)
    cpu_count = models.SmallIntegerField(u'物理cpu个数')
    cpu_core_count = models.SmallIntegerField(u'cpu核数')
    memo = models.TextField(u'备注', null=True,blank=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(blank=True,null=True)

    class Meta:
        verbose_name = 'CPU部件'
        verbose_name_plural = "CPU部件"
    def __str__(self):
        return self.cpu_model

class IDC(models.Model):
    """
    机房信息
    """
    name = models.CharField('机房', max_length=32)
    floor = models.IntegerField('楼层', null=True, blank=True, default=0)

    class Meta:
        verbose_name_plural = "机房表"

    def __str__(self):
        return self.name

class Tag(models.Model):
    """
    资产标签
    """
    name = models.CharField(verbose_name='标签', max_length=32, unique=True)

    class Meta:
        verbose_name_plural = "标签表"

    def __str__(self):
        return self.name

class ArticleDetail(models.Model):
    article = models.OneToOneField('Asset')
    # nid = models.BigAutoField(primary_key=True)
    title = models.CharField(verbose_name='文章标题', max_length=128)
    summary = models.CharField(verbose_name='文章简介', max_length=255)
    content = models.TextField(verbose_name='文章内容', )

    class Meta:
        verbose_name_plural = '备注_文章'

    def __str__(self):
        return ('%s----%s') % (self.id,self.title)

class Asset(models.Model):
    """
    资产信息表，所有资产公共信息（交换机，服务器，防火墙等）
    """
    device_type_choices = (
        (1, '服务器-硬件'),
        (2, '服务器-虚拟机'),
        (3, '交换机'),
        (4, '防火墙'),
    )
    device_status_choices = (
        (1, '上架'),
        (2, '在线'),
        (3, '离线'),
        (4, '下架'),
    )

    device_type_id = models.IntegerField(verbose_name="资产类型", choices=device_type_choices, default=1)
    name = models.CharField(max_length=64,unique=True)
    device_status_id = models.IntegerField(verbose_name="资产状态", choices=device_status_choices, default=1)

    cabinet_num = models.CharField(verbose_name='机柜号', max_length=30, null=True, )
    cabinet_order = models.CharField(verbose_name='机柜中序号', max_length=30, null=True, )

    sn = models.CharField(u'资产SN号',max_length=128, unique=True)
    idc = models.ForeignKey('IDC', verbose_name='IDC机房', null=True,blank=True ,  default=None)
    business_unit = models.ForeignKey('BusinessUnit', verbose_name='属于的业务线', null=True,blank=True ,default=None)

    contract = models.ForeignKey('Contract', verbose_name=u'合同',null=True, blank=True)
    trade_date = models.DateField(u'购买时间',null=True, blank=True)
    expire_date = models.DateField(u'过保修期',null=True, blank=True)
    price = models.FloatField(u'价格',null=True, blank=True)


    tag = models.ManyToManyField('Tag')
    manufactory = models.ForeignKey('Manufactory',verbose_name=u'制造商',null=True, blank=True)

    latest_date = models.DateField(verbose_name="最后更新时间", null=True)
    create_at = models.DateTimeField(auto_now_add=True, null=True )

    class Meta:
        verbose_name_plural = "资产表"


    def __str__(self):
        # return "%s-%s-%s" % (self.id, self.idc.name, self.cabinet_num)
        return "%s--%s" % (self.id,self.name)

class Server(models.Model):
    """
    服务器信息
    """
    asset = models.OneToOneField('Asset')

    hostname = models.CharField(max_length=128, unique=True)
    sn = models.CharField('SN号', max_length=64, db_index=True, null=True, blank=True)
    # manufacturer = models.CharField(verbose_name='制造商', max_length=64, null=True, blank=True)

    model = models.CharField('型号', max_length=64, null=True, blank=True)

    login_user = models.CharField('登录用户名',max_length=32,unique=True)
    password = models.CharField('登录密码',max_length=64,unique=True)

    private_ip = models.GenericIPAddressField('私有IP',null=True, blank=True )
    public_ip = models.GenericIPAddressField('公网IP', null=True, blank=True )

    os_platform = models.CharField('系统', max_length=64, null=True, blank=True)
    os_version = models.CharField('系统版本', max_length=64, null=True, blank=True)

    cpu_count = models.IntegerField('CPU个数', null=True, blank=True)
    cpu_physical_count = models.IntegerField('CPU物理个数', null=True, blank=True)
    cpu_model = models.CharField('CPU型号', max_length=128, null=True, blank=True)

    raid_type = models.CharField(u'raid类型',max_length=512, blank=True,null=True)
    # os_type  = models.CharField(u'操作系统类型',max_length=64, blank=True,null=True)
    # os_distribution =models.CharField(u'发型版本',max_length=64, blank=True,null=True)
    # os_release  = models.CharField(u'操作系统版本',max_length=64, blank=True,null=True)

    create_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "服务器表"
        verbose_name = "服务器"


    def __str__(self):
        return '%s--%s' % (self.id, self.hostname)


class NetworkDevice(models.Model):
    asset = models.OneToOneField('Asset')
    management_ip = models.CharField('公网IP', max_length=64, blank=True, null=True)
    vlan_ip = models.CharField('VlanIP', max_length=64, blank=True, null=True)

    intranet_ip = models.CharField('内网IP', max_length=128, blank=True, null=True)
    sn = models.CharField('SN号', max_length=64, unique=True)
    manufacture = models.CharField(verbose_name=u'制造商', max_length=128, null=True, blank=True)
    model = models.CharField('型号', max_length=128, null=True, blank=True)
    port_num = models.SmallIntegerField('端口个数', null=True, blank=True)
    device_detail = models.CharField('设置详细配置', max_length=255, null=True, blank=True)

    name = models.CharField(u'网卡名', max_length=64, blank=True,null=True)
    macaddress = models.CharField(u'MAC', max_length=64,unique=True)

    # ipaddress = models.GenericIPAddressField(u'IP', blank=True,null=True)

    netmask = models.CharField(max_length=64,blank=True,null=True)
    bonding = models.CharField(max_length=64,blank=True,null=True)
    memo = models.CharField(u'备注',max_length=128, blank=True,null=True)
    create_date = models.DateTimeField(blank=True, auto_now_add=True)
    update_date = models.DateTimeField(blank=True,null=True)

    class Meta:
        verbose_name_plural = "网络设备"

class Disk(models.Model):
    """
    硬盘信息
    """
    asset = models.ForeignKey('Asset')
    server_obj = models.ForeignKey('Server',related_name='disk')
    slot = models.CharField('插槽位', max_length=8)
    model = models.CharField('磁盘型号', max_length=128)
    capacity = models.FloatField('磁盘容量GB')
    pd_type = models.CharField('磁盘类型', max_length=64)

    class Meta:
        verbose_name_plural = "硬盘表"

    def __str__(self):
        return self.slot

class NIC(models.Model):
    """
    网卡信息
    """
    asset = models.ForeignKey('Asset')
    name = models.CharField('网卡名称', max_length=128)
    hwaddr = models.CharField('网卡mac地址', max_length=64)
    netmask = models.CharField('掩码',max_length=64)
    ipaddrs = models.CharField('ip地址', max_length=256)
    up = models.BooleanField('状态',default=False)
    server_obj = models.ForeignKey('Server',related_name='nic')

    class Meta:
        verbose_name_plural = "网卡表"

    def __str__(self):
        return self.name

class Memory(models.Model):
    """
    内存信息
    """
    asset = models.ForeignKey('Asset')
    # server_obj = models.ForeignKey('Server',related_name='memory')

    sn = models.CharField(u'SN号', max_length=128, blank=True,null=True)
    model =  models.CharField(u'内存型号', max_length=128)
    slot = models.CharField(u'插槽', max_length=64)
    capacity = models.IntegerField(u'内存大小(MB)')
    memo = models.CharField(u'备注',max_length=128, blank=True,null=True)

    speed = models.CharField('速度', max_length=16, null=True, blank=True)
    manufacturer = models.CharField('制造商', max_length=32, null=True, blank=True)

    create_date = models.DateTimeField(blank=True, auto_now_add=True)
    update_date = models.DateTimeField(blank=True,null=True)

    def __str__(self):
        return '%s:%s:%s' % (self.asset_id,self.slot,self.capacity)

    class Meta:
        verbose_name = '内存'
        verbose_name_plural = "内存表"
    #     unique_together = ("asset", "slot")
    # auto_create_fields = ['sn','slot','model','capacity']

# class Memory(models.Model):
#     """
#     内存信息
#     """
#     slot = models.CharField('插槽位', max_length=32)
#     manufacturer = models.CharField('制造商', max_length=32, null=True, blank=True)
#     model = models.CharField('型号', max_length=64)
#     capacity = models.FloatField('容量', null=True, blank=True)
#     sn = models.CharField('内存SN号', max_length=64, null=True, blank=True)
#     speed = models.CharField('速度', max_length=16, null=True, blank=True)
#
#     server_obj = models.ForeignKey('Server',related_name='memory')
#
#
#     class Meta:
#         verbose_name_plural = "内存表"
#
#     def __str__(self):
#         return self.slot

class AssetRecord(models.Model):
    """
    资产变更记录,creator为空时，表示是资产汇报的数据。
    """
    asset_obj = models.ForeignKey('Asset', related_name='ar')
    content = models.TextField(null=True)
    creator = models.ForeignKey('UserProfile', null=True, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "资产记录表"

    def __str__(self):
        return "%s-%s-%s" % (self.asset_obj.idc.name, self.asset_obj.cabinet_num, self.asset_obj.cabinet_order)

class ErrorLog(models.Model):
    """
    错误日志,如：agent采集数据错误 或 运行错误
    """
    asset_obj = models.ForeignKey('Asset', null=True, blank=True)
    title = models.CharField(max_length=16)
    content = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "错误日志表"

    def __str__(self):
        return self.title

class Manufactory(models.Model):

    manufactory = models.CharField(u'厂商',max_length=64, unique=True)
    
    support_num = models.CharField(u'支持电话',max_length=30,blank=True)
    memo = models.CharField(u'备注',max_length=128,blank=True)

    def __str__(self):
        return self.manufactory
    class Meta:
        verbose_name = '厂商'
        verbose_name_plural = "厂商"

class Contract(models.Model):
    '''
    合同表。可进行合同管理。
    '''
    sn = models.CharField(u'合同号', max_length=128,unique=True)
    name = models.CharField(u'合同名称', max_length=64 )
    memo = models.TextField(u'备注', blank=True,null=True)
    price = models.IntegerField(u'合同金额')
    detail = models.TextField(u'合同详细',blank=True,null=True)
    start_date = models.DateField(blank=True)
    end_date = models.DateField(blank=True)
    license_num = models.IntegerField(u'license数量',blank=True)

    create_date = models.DateField(auto_now_add=True)
    update_date= models.DateField(auto_now=True)

    class Meta:
        verbose_name = '合同'
        verbose_name_plural = "合同"

    def __str__(self):
        return self.name

class NewAssetApprovalZone(models.Model):
    '''
    资产待批准表
    '''
    sn = models.CharField(u'资产SN号',max_length=128, unique=True)
    asset_type_choices = (
        ('server', u'服务器'),
        ('switch', u'交换机'),
        ('router', u'路由器'),
        ('firewall', u'防火墙'),
        ('storage', u'存储设备'),
        ('NLB', u'NetScaler'),
        ('wireless', u'无线AP'),
        ('software', u'软件资产'),
        ('others', u'其它类'),
    )
    asset_type = models.CharField(choices=asset_type_choices,max_length=64,blank=True,null=True)
    manufactory = models.CharField(max_length=64,blank=True,null=True)
    model = models.CharField(max_length=128,blank=True,null=True)
    ram_size = models.IntegerField(blank=True,null=True)
    cpu_model = models.CharField(max_length=128,blank=True,null=True)
    cpu_count = models.IntegerField(blank=True,null=True)
    cpu_core_count = models.IntegerField(blank=True,null=True)
    os_distribution =  models.CharField(max_length=64,blank=True,null=True)
    os_type =  models.CharField(max_length=64,blank=True,null=True)
    os_release =  models.CharField(max_length=64,blank=True,null=True)
    data = models.TextField(u'资产数据')
    date = models.DateTimeField(u'汇报日期',auto_now_add=True)
    approved = models.BooleanField(u'已批准',default=False)
    approved_by = models.ForeignKey('UserProfile',verbose_name=u'批准人',blank=True,null=True)
    approved_date = models.DateTimeField(u'批准日期',blank=True,null=True)

    def __str__(self):
        return '%s--%s' %  (self.id,self.sn)

    class Meta:
        verbose_name = '新上线待批准资产'
        verbose_name_plural = "新上线待批准资产"





