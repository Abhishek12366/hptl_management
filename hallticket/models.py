from django.db import models
from django.http import HttpResponse
from app.models import CustomUser
from app import models
from django.contrib.auth.hashers import make_password, check_password
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
# Create your models here.

from django.db import models
from django.contrib.auth.models import User

class Program(models.Model):
    code = models.CharField(max_length=10)
    title = models.CharField(max_length=100)

class Course(models.Model):
    code = models.CharField(max_length=10)
    title = models.CharField(max_length=100)
    semester = models.PositiveIntegerField()
    program = models.ForeignKey(Program, on_delete=models.CASCADE)

class HallTicket(models.Model):
    student = models.OneToOneField(CustomUser, on_delete=models.CASCADE,null=True)
    program = models.CharField(max_length=50)
    course = models.CharField(max_length=50)
    examination_center_code = models.CharField(max_length=10)
    examination_center_address = models.TextField()
    exam_date = models.DateField()
    exam_time = models.TimeField()
    seat_number = models.CharField(max_length=10)

    def __str__(self):
        return f"Hall Ticket for {self.student.name}"




# class ExaminationCenter(models.Model):
#     code = models.CharField(max_length=10)
#     address = models.TextField()


# class Student(models.Model):
#     user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='student')
#     student_name = models.CharField(max_length=100)
#     address = models.TextField()
#     aadhaar_number = models.CharField(max_length=12)
#     program = models.CharField(max_length=50)
#     course = models.CharField(max_length=50)
#     enrollment_number = models.CharField(max_length=20, unique=True)

#     USERNAME_FIELD = 'username'
  
#     def set_password(self, raw_password):
#         self.password = make_password(raw_password)
    
#     def check_password(self, raw_password):
#         return check_password(raw_password, self.password)

#     def __str__(self):
#         return self.student_name
    

    


