from django.contrib import admin
from .models import Adoption,Pet,PetBreed, PetImage, PetKind
# Register your models here.
admin.site.register(Adoption)
admin.site.register(Pet)
admin.site.register(PetBreed)
admin.site.register(PetKind)
admin.site.register(PetImage)