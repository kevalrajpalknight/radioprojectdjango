from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.Podcast)
admin.site.register(models.LiveShow)