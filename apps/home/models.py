from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    birth = models.DateField()
    user = models.OneToOneField(User, on_delete=models.PROTECT)

