from rest_framework.serializers import ModelSerializer
from .models import Student, Subject

class StudentSerializer(ModelSerializer):
    
    class Meta:
        model = Student
        fields = ['id', 'name', 'gender', 'batch', 'clg_adm', 'ktu_adm', 'cgpa']
        
class SubjectSerializer(ModelSerializer):
    class Meta:
        model = Subject
        fields = ['id', 'name', 'code']