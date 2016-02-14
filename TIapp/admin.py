from django.contrib import admin
from TIapp import models
# Register your models here.

class IssueAdmin(admin.ModelAdmin):
    display_list = ('title', 'description', 'requester', 'assigned_group', 'Severity', 'created_time', 'updated_time')

admin.site.register(models.Issue,IssueAdmin)
admin.site.register(models.Comments)
admin.site.register(models.Ti_user)
admin.site.register(models.Cti)
admin.site.register(models.Department)
