from rest_framework import serializers
from .models import AnnotationProject, AnnotationTask

class AnnotationProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnnotationProject
        fields = '__all__'

class AnnotationTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnnotationTask
        fields = '__all__'