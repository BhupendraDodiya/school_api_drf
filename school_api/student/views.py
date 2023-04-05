from django.shortcuts import render
from rest_framework import generics
from .serializers import StudentSerializer
from .models import Student

# Create your views here.
class student_get(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class student_one(generics.RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class student_create(generics.CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class student_update(generics.UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class student_delete(generics.DestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
