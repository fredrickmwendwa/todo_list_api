from rest_framework import serializers
from .models import Category, Task


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'created_at']

    def validate_name(self, value):
        if not value.strip():
            raise serializers.ValidationError("Category name cannot be empty.")

    
        request = self.context.get('request')
        if request and Category.objects.filter(owner=request.user, name=value).exists():
            raise serializers.ValidationError("You already have a category with this name.")
        return value

class TaskSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True)

    class Meta:
        model = Task
        fields = [
            'id', 'title', 'description', 'is_completed',
            'due_date', 'category', 'category_name',
            'created_at', 'updated_at'
        ]

    def validate_title(self, value):
        if not value.strip():
            raise serializers.ValidationError("Task title cannot be empty.")
        return value

    def validate_category(self, value):
        request = self.context.get('request')
        if value and value.owner != request.user:
            raise serializers.ValidationError("You do not own this category.")
        return value