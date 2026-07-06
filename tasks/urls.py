from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewsets, TaskViewSet

router = DefaultRouter()
router.register('categories', CategoryViewsets, basename='category')
router.register('tasks', TaskViewSet, basename='task')

urlpatterns = [
    path('', include(router.urls))
]
