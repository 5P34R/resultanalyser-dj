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
    year = models.CharField(max_length=20, default="2020-2024")
    sem = models.CharField(max_length=20)
    tutor = models.OneToOneField(Tutor, on_delete=models.CASCADE)
    teachers = models.ManyToManyField(Tutor, related_name="teachers")
    
    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=100)
    roll_no = models.IntegerField(default=0)
    gender = models.CharField(max_length=10)
    batch = models.ForeignKey(Class, on_delete=models.CASCADE)
    clg_adm = models.CharField(max_length=100, unique=True)
    ktu_adm = models.CharField(max_length=100, unique=True)
    cgpa = models.FloatField(default=0)
    
    
    def __str__(self):
        return f"{self.name}"
    
    class Result(models.Model):
        subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
        tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE)
        grade = models.CharField(max_length=2)
        
        def __str__(self) -> str:
            return f"{self.subject.name} -> {self.tutor.name} -> {self.grade}"