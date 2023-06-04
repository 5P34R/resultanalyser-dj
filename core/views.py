from django.shortcuts import render,HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser

from .models import Student
from .serializers import StudentSerializer

import pandas as pd


class HighCGPA(APIView):
    def get(self, request):
        students = Student.objects.order_by("-cgpa")
        serializers = StudentSerializer(students, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)
    

class AllStudents(APIView):
    def get(self, request):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class BatchStudentList(APIView):
    
    parser_classes = [MultiPartParser]
    
    def get(self, request):
        batch = request.query_params.get('batch', '')
        if batch == '':
            return Response("Please provide batch name", status=status.HTTP_400_BAD_REQUEST)
        students = Student.objects.filter(batch__name__icontains=batch)
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
    def post(self, request):
        file_obj = request.FILES['file']
        try:
            data = pd.read_excel(file_obj)
            return Response(data.to_dict(orient='records'))
        except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)