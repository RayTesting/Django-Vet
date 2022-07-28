from django.db import models

# Create your models here.
img_path = 'static/assets/media/store/'

class ProductColor(models.Model):
    color = models.CharField(max_length=20)
    
    def __str__(self):
        return self.color

class ProductImage(models.Model):
    image = models.ImageField(upload_to=f'{img_path}ProductImages')
    def __str__(self):
        return self.image

class ProductCategory(models.Model):
    category = models.CharField(max_length=100)
    image = models.ImageField(upload_to=f'{img_path}ProductCategories')
    
    def __str__(self):
        return self.category
    
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    colors = models.ManyToManyField(ProductColor)
    stock = models.IntegerField()
    images = models.ManyToManyField(ProductImage)
    category = models.ForeignKey(ProductCategory, on_delete=models.PROTECT, null=True)

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
