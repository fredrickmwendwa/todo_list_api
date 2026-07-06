from rest_framework import viewsets, permissions
from .models import Category, Task
from .serializers import CategorySerializer, TaskSerializer

class CategoryViewsets(viewsets.ModelViewSet):
  serializer_class = CategorySerializer
  permission_classes = [permissions.IsAuthenticated]

  def get_queryset(self):
    return Category.objects.filter(owner=self.request.user)
  
  def perform_create(self, serializer):
    serializer.save(owner=self.request.user)

class TaskViewSet(viewsets.ModelViewSet):
  serializer_class = TaskSerializer
  permission_classes = [permissions.IsAuthenticated]

  def get_queryset(self):
    return Task.objects.filter(owner=self.request.user)
  
  def perform_create(self, serializer):
    serializer.save(owner=self.request.user)

  def get_serializer_context(self):
    context = super().get_serializer_context()
    context['request'] = self.request
    return context