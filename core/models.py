from django.db import models

# Create your models here.

class Subject(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
    
    
class Tutor(models.Model):
    name = models.CharField(max_length=100)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} -> {self.subject.name}"
    
    
class Class(models.Model):
    name = models.CharField(max_length=100)
    tutor = models.OneToOneField(Tutor, on_delete=models.CASCADE)
    teachers = models.ManyToManyField(Tutor, related_name="teachers")
    
    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    clg_adm = models.CharField(max_length=100, unique=True)
    ktu_adm = models.CharField(max_length=100, unique=True)
    cgpa = models.IntegerField(default=0)
    
    def __str__(self):
        return f"{self.name}"