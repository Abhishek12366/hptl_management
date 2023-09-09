from django.db import models
from django.http import HttpResponse
from app.models import CustomUser
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

# class ExaminationCenter(models.Model):
#     code = models.CharField(max_length=10)
#     address = models.TextField()


class Student(models.Model):
    # admin = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100)
    address = models.TextField()
    aadhaar_number = models.CharField(max_length=12)
    program = models.CharField(max_length=50)
    course = models.CharField(max_length=50)
    enrollment_number = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name
    
class HallTicket(models.Model):
    # student = models.OneToOneField(Student, on_delete=models.CASCADE)
    program = models.CharField(max_length=50)
    course = models.CharField(max_length=50)
    examination_center_code = models.CharField(max_length=10)
    examination_center_address = models.TextField()
    exam_date = models.DateField()
    exam_time = models.TimeField()
    seat_number = models.CharField(max_length=10)

    def __str__(self):
        return f"Hall Ticket for {self.student.name}"
    


def generate_hall_ticket_pdf(request, hall_ticket_id):

    hall_ticket = HallTicket.objects.get(id=hall_ticket_id)
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'filename="hall_ticket_{hall_ticket_id}.pdf"'

    c = canvas.Canvas(response, pagesize=letter)

    c.setFont("Helvetica-Bold", 14)
    c.drawString(100, 750, f'Student Name: {hall_ticket.student.user.username}')
    c.drawString(100, 730, f'Enrollment Number: {hall_ticket.student.enrollment_number}')

    c.setFont("Helvetica", 12)
    c.drawString(100, 710, f'Programme: {hall_ticket.student.programme}')
    c.drawString(100, 690, f'Course: {hall_ticket.student.course}')

    c.setFont("Helvetica-Bold", 14)
    c.drawString(100, 660, 'Exam Details')
    c.setFont("Helvetica", 12)
    c.drawString(100, 640, f'Exam Center: {hall_ticket.exam_center_name}')
    c.drawString(100, 620, f'Exam Date: {hall_ticket.exam_date.strftime("%Y-%m-%d %H:%M:%S")}')

    c.showPage()
    c.save()

    return response


