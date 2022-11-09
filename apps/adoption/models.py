from telnetlib import STATUS
from django.db import models
from apps.home.models import Customer

img_path = 'static/assets/media/adoption/'
# Create your models here.
class PetKind(models.Model):
    kind = models.CharField(max_length=100)
    image = models.ImageField(null=True, upload_to=f'{img_path}PetKind')

    def __str__(self):
        return self.kind
    

class PetBreed(models.Model):
    breed = models.CharField(max_length=100)
    image = models.ImageField(null=True, upload_to=f'{img_path}PetBreed')

    def __str__(self):
        return self.breed
    

class PetImage(models.Model):
    image = models.ImageField(null=True, upload_to=f'{img_path}Pet')

    def __str__(self):
        return self.image.name
    

AGE_CHOICES = (('years','years'),('months','months'))
STATUS_CHOICES = (('in adoption','in adoption'), ('adopted','adopted'))

class Pet(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    age_type = models.CharField(max_length=10, choices=AGE_CHOICES, default='') 
    pet_kind = models.ForeignKey(PetKind, on_delete=models.PROTECT)
    pet_breed = models.ForeignKey(PetBreed, on_delete=models.PROTECT, null=True, blank=True)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='not specified')
    images = models.ManyToManyField(PetImage)

    def __str__(self):
        return self.name
    

class Adoption(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.PROTECT)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    date = models.DateTimeField()

    def __str__(self):
        return f'{self.pet} - {self.customer}'