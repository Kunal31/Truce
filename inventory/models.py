from __future__ import unicode_literals

from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = "products"  

    def __str__(self):
        return self.name
    
class ProductPriceHistory(models.Model):
    product = models.ForeignKey(Product)
    price = models.IntegerField()
    date = models.DateField()

    class Meta:
        db_table = "product_price_history"

class Transactions(models.Model):
    trans_id = models.IntegerField()
    product = models.ForeignKey(Product)

    class Meta:
        db_table = "transactions"

