from django.db import models

class Category(models.Model):
    category = models.CharField(max_length=100, null=False, blank=False, verbose_name='Category')
    description = models.TextField(max_length= 300, null=False, blank=False, verbose_name='Category Description')


class Product(models.Model):
    category = models.ForeignKey(to='webapp.Category', verbose_name='Category',null=False,blank=False, related_name='products', on_delete=models.RESTRICT)
    name = models.CharField(max_length=100, null=False, blank=False, verbose_name='Product name')
    description = models.TextField(max_length=1000, null=False, blank=False, verbose_name='Product Description')
    price = models.DecimalField(max_digits=50, decimal_places= 2,null=False, verbose_name='Product Price')
    image = models.TextField(max_length=500, null=False, blank=False, verbose_name='Product Image')
