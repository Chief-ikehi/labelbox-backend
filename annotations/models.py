
# Create your models here.
from django.db import models
from django.contrib.postgres.fields import ArrayField

class AnnotationProject(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

class AnnotationTask(models.Model):
    project = models.ForeignKey(AnnotationProject, on_delete=models.CASCADE, related_name='tasks')
    image_url = models.URLField()  # Storing image URLs
    annotations = models.JSONField(default=list)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
