from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length = 200)
    money = models.IntegerField(default = 0)
    power = models.BooleanField(default = False)


