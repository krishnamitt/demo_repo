from rest_framework import serializers
from .models import Student,Student1,Student2

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student1
        fields = '__all__'