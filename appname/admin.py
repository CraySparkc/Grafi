from django.contrib import admin
from appname import models
# Register your models here.

admin.site.register(models.Division)
admin.site.register(models.Priority)
admin.site.register(models.Profile)
admin.site.register(models.Project)
admin.site.register(models.State)
admin.site.register(models.Task)
admin.site.register(models.Resource)
admin.site.register(models.Journal)