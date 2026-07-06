from rest_framework import viewsets, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Category, Task
from .serializers import CategorySerializer, TaskSerializer

class CategoryViewsets(viewsets.ModelViewSet):
  serializer_class = CategorySerializer
  permission_classes = [permissions.IsAuthenticated]

  def get_queryset(self):
    return Category.objects.filter(owner=self.request.user)
  
  def perform_create(self, serializer):
    serializer.save(owner=self.request.user)

  def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context

class TaskViewSet(viewsets.ModelViewSet):
  serializer_class = TaskSerializer
  permission_classes = [permissions.IsAuthenticated]

  filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
  filterset_fields = ['category', 'is_completed', 'due_date']
  search_fields = ['title', 'description']
  ordering_fields = ['due_date', 'created_at']

  def get_queryset(self):
    return Task.objects.filter(owner=self.request.user)
  
  def perform_create(self, serializer):
    serializer.save(owner=self.request.user)

  def get_serializer_context(self):
    context = super().get_serializer_context()
    context['request'] = self.request
    return context