from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Issue(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    requester = models.ForeignKey('Ti_user')
    assigned_group = models.ForeignKey('Department')
    Severity = models.IntegerField()
    created_time = models.DateTimeField()
    updated_time = models.DateTimeField()
    
    def __unicode__(self):
        return self.title

class Comments(models.Model):
    content = models.TextField()
    comment_user = models.ForeignKey('Ti_user')
    created_time = models.DateTimeField()

class Category(models.Model):
    name = models.CharField(max_length=64, unique=True)
    owner = models.ForeignKey('Ti_user')
    
    def __unicode__(self):
        return self.name
    
class Type(models.Model):
    pass

class Item(models.Model):
    pass

class Ti_user(models.Model):
    user = models.OneToOneField(User)
    tel = models.IntegerField()
    photo = models.ImageField(upload_to="static/upload_images/", default="static/upload_images/user-1.jpg")
    
    def __unicode__(self):
        return self.user.username
    
class Department(models.Model):
    department_name = models.CharField(max_length=64)
    category = models.ManyToManyField('Category')
    type = models.ManyToManyField('Type')
    item = models.ManyToManyField('Item')
    
    def __unicode__(self):
        return self.department_name
