# from rest_framework import serializers
# from .models import Student

# class StudentSerializer(serializers.ModelSerializer):
#     name =serializers.CharField(max_length = 255,required=True)
#     roll =serializers.EmailField()
#     email =serializers.IntegerField()
#     section = serializers.CharField(max_length = 3,required=True)
#     class Meta:
#         model = Student
#         fields = ['__all__']

from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'