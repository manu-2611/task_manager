from rest_framework import serializers
from backend.models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'completed', 'created', 'modified']
        read_only_fields = ['created', 'modified']
