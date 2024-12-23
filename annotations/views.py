from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import AnnotationProject, AnnotationTask
from .serializers import AnnotationProjectSerializer, AnnotationTaskSerializer

class ProjectListCreateView(APIView):
    def get(self, request):
        projects = AnnotationProject.objects.all()
        serializer = AnnotationProjectSerializer(projects, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AnnotationProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TaskListCreateView(APIView):
    def get(self, request):
        tasks = AnnotationTask.objects.all()
        serializer = AnnotationTaskSerializer(tasks, many=True)
        return Response(serializer.data)


    def post(self, request):
        print("Received data:", request.data)  # This will print incoming data to the console
        task_id = request.data.get('id')
        annotations = request.data.get('annotations')

        try:
            task = AnnotationTask.objects.get(id=task_id)
            task.annotations = annotations  # Update the annotations field
            task.save()  # Save the task with the new annotations

            return Response({"message": "Annotations saved successfully!"}, status=status.HTTP_200_OK)
        except AnnotationTask.DoesNotExist:
            return Response({"error": "Task not found!"}, status=status.HTTP_404_NOT_FOUND)
