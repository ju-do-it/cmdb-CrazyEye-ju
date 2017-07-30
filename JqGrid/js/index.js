//
//$(function(){
//	//页面加载完成之后执行
//	pageInit();
//});
//function pageInit(){
//	//创建jqGrid组件
//
//	jQuery("#list2").jqGrid(
//			{
//				//url : 'data/JSONData.json',//组件创建完成之后请求数据的url
//				//datatype : "json",//请求数据返回的类型。可选json,xml,txt
//				colNames : [ 'Inv No', 'Date', 'Client', 'Amount', 'Tax','Total', 'Notes' ],//jqGrid的列显示名字
//				colModel : [                    //jqGrid每一列的配置信息。包括名字，索引，宽度,对齐方式.....
//				             {name : 'id',index : 'id',width : 55},
//				             {name : 'invdate',index : 'invdate',width : 90},
//				             {name : 'name',index : 'name asc, invdate',width : 100},
//				             {name : 'amount',index : 'amount',width : 80,align : "right"},
//				             {name : 'tax',index : 'tax',width : 80,align : "right"},
//				             {name : 'total',index : 'total',width : 80,align : "right"},
//				             {name : 'note',index : 'note',width : 150,sortable : false}
//				           ],
//				rowNum : 10,//一页显示多少条
//				rowList : [ 10, 20, 30 ],//可供用户选择一页显示多少条
//				pager : '#pager2',//表格页脚的占位符(一般是div)的id
//				sortname : 'id',//初始化的时候排序的字段
//				sortorder : "desc",//排序方式,可选desc,asc
//				mtype : "post",//向后台请求数据的ajax的类型。可选post,get
//				viewrecords : true,
//				caption : "JSON Example"//表格的标题名字
//			});
//	/*创建jqGrid的操作按钮容器*/
//	/*可以控制界面上增删改查的按钮是否显示*/
//	jQuery("#list2").jqGrid('navGrid', '#pager2', {edit : false,add : false,del : false});
//}

//
//$(function(){
//  pageInit();
//});
//function pageInit(){
//  jQuery("#list2").jqGrid(
//      {
//        datatype : "local",
//        height : 400,
//        colNames : [ 'Inv No', 'Date', 'Client', 'Amount', 'Tax','Total', 'Notes' ],
//        colModel : [
//                     {name : 'id',index : 'id',width : 60,sorttype : "int"},
//                     {name : 'invdate',index : 'invdate',width : 90,sorttype : "date"},
//                     {name : 'name',index : 'name',width : 100},
//                     {name : 'amount',index : 'amount',width : 80,align : "right",sorttype : "float"},
//                     {name : 'tax',index : 'tax',width : 80,align : "right",sorttype : "float"},
//                     {name : 'total',index : 'total',width : 80,align : "right",sorttype : "float"},
//                     {name : 'note',index : 'note',width : 150,sortable : false}
//                   ],
//		rowNum : 10,
//		autowidth : true,
//
//
//        rowList : [ 10, 20, 30 ],
//        pager : jQuery('#pager2'),
//        mtype : "post",
//        sortname : 'id',
//        viewrecords : true,
//        sortorder : "desc",
//        caption : "XML 实例"
//
//      });
//
//  var mydata = [
//
//
//                 {id : "1",invdate : "2007-10-01",name : "test",note : "note",amount : "200.00",tax : "10.00",total : "210.00"},
//                 {id : "2",invdate : "2007-10-02",name : "test2",note : "note2",amount : "300.00",tax : "20.00",total : "320.00"},
//                 {id : "3",invdate : "2007-09-01",name : "test3",note : "note3",amount : "400.00",tax : "30.00",total : "430.00"},
//                 {id : "4",invdate : "2007-10-04",name : "test",note : "note",amount : "200.00",tax : "10.00",total : "210.00"},
//                 {id : "5",invdate : "2007-10-05",name : "test2",note : "note2",amount : "300.00",tax : "20.00",total : "320.00"},
//                 {id : "6",invdate : "2007-09-06",name : "test3",note : "note3",amount : "400.00",tax : "30.00",total : "430.00"},
//                 {id : "7",invdate : "2007-10-04",name : "test",note : "note",amount : "200.00",tax : "10.00",total : "210.00"},
//                 {id : "8",invdate : "2007-10-03",name : "test2",note : "note2",amount : "300.00",tax : "20.00",total : "320.00"},
//                 {id : "9",invdate : "2007-09-01",name : "test3",note : "note3",amount : "400.00",tax : "30.00",total : "430.00"},
//
//                 {id : "1",invdate : "2007-10-01",name : "test",note : "note",amount : "200.00",tax : "10.00",total : "210.00"},
//                 {id : "2",invdate : "2007-10-02",name : "test2",note : "note2",amount : "300.00",tax : "20.00",total : "320.00"},
//                 {id : "3",invdate : "2007-09-01",name : "test3",note : "note3",amount : "400.00",tax : "30.00",total : "430.00"},
//                 {id : "4",invdate : "2007-10-04",name : "test",note : "note",amount : "200.00",tax : "10.00",total : "210.00"},
//                 {id : "5",invdate : "2007-10-05",name : "test2",note : "note2",amount : "300.00",tax : "20.00",total : "320.00"},
//                 {id : "6",invdate : "2007-09-06",name : "test3",note : "note3",amount : "400.00",tax : "30.00",total : "430.00"},
//                 {id : "7",invdate : "2007-10-04",name : "test",note : "note",amount : "200.00",tax : "10.00",total : "210.00"},
//                 {id : "8",invdate : "2007-10-03",name : "test2",note : "note2",amount : "300.00",tax : "20.00",total : "320.00"},
//                 {id : "9",invdate : "2007-09-01",name : "test3",note : "note3",amount : "400.00",tax : "30.00",total : "430.00"},
//
//               ];
//  for ( var i = 0; i <= mydata.length; i++){
//    jQuery("#list2").jqGrid('addRowData', i + 1, mydata[i]);
//  }
//}



$(function(){
  pageInit();
});
function pageInit(){
  jQuery("#list2").jqGrid(
      {
        //url : 'data/JSONData.json',
        url : 'http://127.0.0.1:8080/api/new_asset_display/',
        datatype : "json",
        colNames : [ 'id', '资产SN', '资产类型', '资产厂商', '资产模型','内存大小', 'CPU型号','CPU物理数','CPU核心数','汇报日期','是否被批准' ],
        colModel : [
                     {name : 'id',index : 'new_asset_id', width : 55,sorttype : "float"},
                     {name : '资产SN',index : 'new_asset_sn', width : 90},
                     {name : '资产类型',index : 'new_asset_type', width : 100},
                     {name : '资产厂商',index : 'new_asset_manufactory', width : 80,align : "right"},
                     {name : '资产模型',index : 'new_asset_model', width : 80,align : "right",sorttype : "float"},
                     {name : '内存大小',index : 'new_asset_ram_size', width : 80,align : "right",sorttype : "float"},
                     {name : 'CPU型号',index : 'new_asset_cpu_model', width : 150,align : "right",sorttype : "int"},
                     {name : 'CPU物理数',index : 'new_asset_cpu_count', width : 80,align : "right",sorttype: "int"},
                     {name : 'CPU核心数',index : 'new_asset_cpu_core_count', width : 80,align : "right"},
                     {name : '汇报日期',index : 'new_asset_date', width : 80,align : "right"},
                     {name : '是否被批准',index : 'new_asset_date', width : 80,align : "right"}
                   ],

        rowNum : 10,
        rowList : [ 10, 20, 30 ],
        pager : '#pager2',
        sortname : 'id',
        mtype : "GET",
        viewrecords : true,
        sortorder : "desc",
        caption : "JSON 实例",
        autowidth : true
      });

  jQuery("#list2").jqGrid('navGrid', '#pager2', {edit : false,add : false,del : false});
}





























