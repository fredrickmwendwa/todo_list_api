from rest_framework import serializers
from .models import Category, Task


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'created_at']
        
class TaskSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True)

    class Meta:
        model = Task
        fields = [
            'id', 'title', 'description', 'is_completed',
            'due_date', 'category', 'category_name',
            'created_at', 'updated_at'
        ]

    def validate_category(self, value):
        request = self.context.get('request')
        if value and value.owner != request.user:
            raise serializers.ValidationError("You do not own this category.")
        return value