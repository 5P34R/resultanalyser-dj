from django.urls import path

from .views import *

urlpatterns = [
    path("high-cgpa/", HighCGPA.as_view(), name="high-cgpa"),
    path("all-students/", AllStudents.as_view(), name="all-students"),   
    path("batch-students/", BatchStudentList.as_view(), name="batch-list"),   
]