from email.policy import default
from django.db import models
from apps.adoption.models import PetKind
from apps.home.models import BaseItem

# Create your models here.
img_path = 'static/assets/media/store/'

class ProductImage(models.Model):
    image = models.FileField(upload_to=f'{img_path}ProductImages')
    
    def __str__(self):
     return self.image.name

class ProductCategory(models.Model):
    category = models.CharField(max_length=100)
    image = models.FileField(upload_to=f'{img_path}ProductCategories')
    
    def __str__(self):
        return self.category
    
class Product(BaseItem):
    stock = models.IntegerField()
    images = models.ManyToManyField(ProductImage)
    category = models.ForeignKey(ProductCategory, on_delete=models.PROTECT, null=True)
    pet_kind = models.ForeignKey(PetKind, on_delete=models.PROTECT, null=True)
    settings = models.JSONField(db_index=True, default=None, null=True, blank=True)

    def __str__(self):
        return self.name

# static
#   assets
#   media
#       store
#           ProductCategory
#       home
#




######

# components
# ProductItem
# AdoptionTable
# --------
# pages
# ----------
