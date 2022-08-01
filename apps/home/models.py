from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    birth = models.DateField()
    user = models.OneToOneField(User, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.name} {self.last_name}'

class BaseItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    class Meta:
        abstract = True
    

img_path = 'static/assets/media/home/'
class HomeSlide(models.Model):
    image = models.ImageField(upload_to=f'{img_path}HomeSlide')

    def __str__(self):
        return self.image.name

class SiteSettings(models.Model):
    header = models.CharField(max_length=150, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    slides = models.ManyToManyField(HomeSlide)
    logo = models.ImageField(upload_to=f'{img_path}Logos')
    whatsapp_number = models.CharField(max_length=10, blank=True, null=False, validators=[MinLengthValidator(10)])
    facebook_url = models.URLField(max_length=250, blank=True)
    products_image = models.ImageField(upload_to=f'{img_path}HomeImages')
    services_image = models.ImageField(upload_to=f'{img_path}HomeImages')
    adoption_image = models.ImageField(upload_to=f'{img_path}HomeImages')
    