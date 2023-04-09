# tweet/models.py
from django.db import models
from user.models import UserModel


# Create your models here.
class ProductModel(models.Model):
    class Meta:
        db_table = "product"

    author = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    code = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    description = models.TextField(max_length=20)
    price = models.IntegerField(null=False)
    sizes = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    size = models.CharField(choices=sizes, max_length=1)
