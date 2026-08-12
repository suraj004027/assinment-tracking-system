
from rest_framework import serializers

from .models import Assignment


class AssignmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Assignment

        fields = [
            'id',
            'title',
            'course',
            'subject_teacher',
            'description',
            'due_date',
            'status',
            'created_at',
            
        ]

        read_only_fields = [
            'id',
            'created_at',
    
        ]

