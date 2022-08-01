from django.contrib import admin
from .models import Customer,HomeSlide,SiteSettings  
# Register your models here.

admin.site.register(Customer)
admin.site.register(HomeSlide)
admin.site.register(SiteSettings)