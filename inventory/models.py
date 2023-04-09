from django.db import models
from user.models import UserModel
from product.models import ProductModel


class InventoryModel(models.Model):
    class Meta:
        db_table = "inventory"

    author = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE)
    total_quantity = models.IntegerField()