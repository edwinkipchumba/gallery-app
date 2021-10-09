from django.contrib import admin
from .models import Image, Location, categories
# Register your models here.


admin.site.register(Image)
admin.site.register(Location)
admin.site.register(categories)