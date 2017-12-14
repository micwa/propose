from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics

from .models import *
from .serializers import *

# Create your views here.
class ProjectList(APIView):
    """
    /api/projects
    """
    def get(self, request, format=None):
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ProjectCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProjectDetail(APIView):
	"""
	/api/projects/<id>
	"""
	def get_object(self, pk):
		return get_object_or_404(Project, pk=pk)

	def get(self, request, pk, format=None):
		project = self.get_object(pk)
		serializer = ProjectSerializer(project)
		return Response(serializer.data)

	def delete(self, request, pk, format=None):
		project = self.get_object(pk)
		project.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)

class ProjectTask(APIView):
    """
    /api/projects/<id>/tasks
    """

    def get_object(self, pk):
        return get_object_or_404(Project, pk=pk)

    def get(self, request, pk, format=None):
        project = self.get_object(pk)
        task = Task.objects.filter(project=project)
        serializer = TaskSerializer(task, many=True)
        return Response(serializer.data)

    def post(self, request, pk, format=None):
        project = self.get_object(pk)
        task_number = Task.objects.filter(project=project.pk).count()+1
        task_data = request.data
        task_data['project'] = project.pk
        task_data['task_number'] = task_number
        serializer = TaskCreateSerializer(data=task_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProjectTaskDetail(APIView):
    """
    /api/projects/<id>/tasks/<task_number>
    """

    def get_object(self, pk):
        return get_object_or_404(Project, pk=pk)

    def get(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        task_number = self.kwargs.get('task_number')
        project = self.get_object(pk)
        task = get_object_or_404(Task, project=project, task_number=task_number)
        serializer = TaskSerializer(task)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        task_number = self.kwargs.get('task_number')
        project = self.get_object(pk)
        task = get_object_or_404(Task, project=project, task_number=task_number)
        task_data = request.data
        serializer = TaskUpdateSerializer(task, data=task_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
