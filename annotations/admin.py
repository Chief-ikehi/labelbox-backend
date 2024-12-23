from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import AnnotationProject, AnnotationTask

admin.site.register(AnnotationProject)
admin.site.register(AnnotationTask)
