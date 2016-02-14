from django.contrib import admin
from TIapp import models
# Register your models here.

admin.site.register(models.Issue)
admin.site.register(models.Category)
admin.site.register(models.Ti_user)