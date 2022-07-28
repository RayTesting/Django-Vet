from django.db import models
from apps.home.models import Customer

img_path = 'static/assets/media/adoption/'
# Create your models here.
class PetKind(models.Model):
    kind = models.CharField(max_length=100)
    image = models.ImageField(null=True, upload_to=f'{img_path}PetKind')
class PetBreed(models.Model):
    breed = models.CharField(max_length=100)
    image = models.ImageField(null=True, upload_to=f'{img_path}PetBreed')

class Pet(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    age_type = models.IntegerChoices('AgeType', 'months years') 
    pet_kind = models.ForeignKey(PetKind, on_delete=models.PROTECT)
    pet_breed = models.ForeignKey(PetBreed, on_delete=models.PROTECT)
    status = models.IntegerChoices('Status','in_adoption adopted')

    def __str__(self):
        return self.name
    

class Adoption(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.PROTECT)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    date = models.DateTimeField()

    def __str__(self):
        return f'{self.pet} - {self.customer}'
    
