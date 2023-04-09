#user/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class UserModel(AbstractUser):
    class Meta:
        db_table = "user"

    birth = models.TextField(max_length=500, blank=True)
    id = models.AutoField(primary_key=True)