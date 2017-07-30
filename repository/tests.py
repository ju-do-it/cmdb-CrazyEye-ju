from django.test import TestCase

# Create your tests here.

product_list_to_insert = list()
for x in range(10):
    product_list_to_insert.append(Product(name='product name ' + str(x), price=x))