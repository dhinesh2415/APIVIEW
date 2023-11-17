# from django.shortcuts import redirect, render
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from .serializers import StudentSerializer
# from .models import *
# from rest_framework.decorators import api_view

# @api_view(['GET'])
# def ApiOverview(request):
#     api_urls = {
#         'all_items': '/',
#         'Search by Category': '/?category=category_name',
#         'Search by Subcategory': '/?subcategory=category_name',
#         'Add': '/create',
#         'Update': '/update/pk',
#         'Delete': '/item/pk/delete'
#     }
 
#     return Response(api_urls)

# from rest_framework import serializers
# from rest_framework import status
 
# @api_view(['POST'])
# def add_items(request):
#     item = StudentSerializer(data=request.data)
 
#     # validating for already existing data
#     if Student.objects.filter(**request.data).exists():
#         raise serializers.ValidationError('This data already exists')
 
#     if item.is_valid():
#         item.save()
#         return Response(item.data)
#     else:
#         return Response(status=status.HTTP_404_NOT_FOUND)

# def create(request):
#     if request.method == 'POST':
#         name = request.POST['name']
#         email = request.POST['email']
#         roll = request.POST['roll']
#         section = request.POST['section']
#         Student(name=name,
#                 email=email,
#                 roll_number = roll,
#                 section =section).save()
#         return redirect('create')

#     data = Student.objects.all()
#     return render(request,'index.html',{'data':data})

# def edit(request,id):
#     dataget = Student.objects.get(id = id)
#     data = Student.objects.all()
#     if request.method == "POST":
#         name = request.POST['name']
#         email = request.POST['email']
#         roll = request.POST['roll']
#         section = request.POST['section']
#         dataget.name = name
#         dataget.email = email
#         dataget.roll_number = roll
#         dataget.section = section
#         dataget.save()
#         return redirect('create')
#     return render(request,'index.html',{'dataget':dataget,'data':data})

# def delete(request,id):
#     dataget = Student.objects.get(id=id)
#     dataget.delete()
#     return redirect('create')
#-------------------------------------------x------------------x-------------------------x-----------------------------------------


from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Student
from .serializers import StudentSerializer

class StudentList(APIView):
    def get(self, request):
        Students = Student.objects.all()
        serializer = StudentSerializer(Students, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StudentDetail(APIView):
    def get(self, request, pk):
        Student = get_object_or_404(Student, pk=pk)
        serializer = StudentSerializer(Student)
        return Response(serializer.data)

    def put(self, request, pk):
        Student = get_object_or_404(Student, pk=pk)
        serializer = StudentSerializer(Student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        Student = get_object_or_404(Student, pk=pk)
        Student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
