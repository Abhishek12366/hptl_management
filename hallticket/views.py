from django.shortcuts import render,redirect
from app.forms import*
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from app.models import *
from.models import *
# import logging
# logger = logging.getLogger(__name__)








def new_student_registration(request):
    form = StudentAdminForm() 

    if request.method == 'POST':
        form = StudentAdminForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_profile')  

    return render(request, 'student_registration.html', {'form': form})

def student_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_student:  
                login(request, user)
                return redirect('student_profile')  
            else:
                return redirect('unauthorized')  
        else:
            return redirect('login_mismatch')  
    return render(request, 'student_login.html')




@login_required
def student_dashboard(request):
    
    student = request.user 
    
    context = {
        'student': student,
  
    }
    
    return render(request, 'hall_ticket/student_dashboard.html', context)



@login_required
def student_profile(request):
   
    student = request.user 
    
    context = {
        'student': student,
        
    }
    
    return render(request, 'student_profile.html')




def new_hall_ticket_registration(request):
    if request.method == 'POST':
        form = HallTicketAdminForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_profile')
    else:
        form = HallTicketAdminForm()

    return render(request, 'hall_ticket_registration.html', {'form': form})


def generate_hall_ticket(request):
   
    if not request.user.is_authenticated or not request.user.is_student:
        return render(request, 'error.html', {'error_message': 'Access denied.'})

   
    student = request.user

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'filename="hall_ticket_{student.enrollment_number}.pdf"'

    c = canvas.Canvas(response, pagesize=letter)

    c.drawString(100, 750, f'Name: {student.username}')
    c.drawString(100, 710, f'Course: {student.course}')
    c.drawString(100, 730, f'Program: {student.program}')

    c.save()

    return response






#>>>>>>>>>>>>><<<<<<<<<<#
##########################################################



# def new_student_registration(request):
#     if request.method == 'POST':
#         form =StudentAdminForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('admin_profile')  
#         form = StudentAdminForm()

#     return render(request, 'student_registration.html', {'form': form})


# def student_login(request):
#     if request.method == 'POST':
#         enrollment_number = request.POST['enrollment_number']
#         student_name = request.POST['student_name']

#         # print(f"Received enrollment_number: {enrollment_number}")
#         # print(f"Received student_name: {student_name}")

     
#         user = authenticate(request, username=enrollment_number, password=student_name)

#         if user is not None:

#             login(request, user)
#             return redirect('student_profile')
#         else:
#             messages.error(request, 'Invalid enrollment number or student name.')

#     return render(request, 'student_login.html')





# def student_login(request):
#     if request.method == 'POST':
#         enrollment_number = request.POST['enrollment_number']
#         password = request.POST['password']
#         user = authenticate(request, username=enrollment_number, password=password)

#         if user is not None:
#             login(request, user)
#             return redirect('student_profile')
#         else:
#             error_message = 'Invalid credentials.'
#             return render(request, 'student_login.html', {'error_message': error_message})
    # return render(request, 'student_login.html')



# import logging
# logger = logging.getLogger(__name__)

# def student_login(request):
#     if request.method == 'POST':
#         enrollment_number = request.POST['enrollment_number']
#         password = request.POST['password']
#         logger.debug(f"Received login attempt - Enrollment Number: {enrollment_number}, Password: {password}")
#         user = authenticate(request, username=enrollment_number, password=password)
#         if user is not None:
#             logger.debug(f"Authentication successful for user: {user.username}")
#             if user.is_student:
#                 login(request, user)
#                 logger.debug("Student login successful")
#                 return redirect('student_profile')
#             else:
#                 logger.warning("User is not a student")
#                 return redirect('unauthorized')
#         else:
#             logger.warning("Authentication failed")
#             return redirect('login_mismatch')
#     return render(request, 'student_login.html')


# previously used
# def student_login(request):
#     if request.method == 'POST':
#         enrollment_number = request.POST['enrollment_number']
#         password = request.POST['password']
#         user = authenticate(request, username=enrollment_number, password=password)
#         if user is not None:
#             if user.is_student:
#                 login(request, user)
#                 return redirect('student_profile')
#             else:
#                 return redirect('unauthorized')
#         else:
#             return redirect('login_mismatch')
#     return render(request, 'student_login.html')




# def student_login(request):
#     if request.method == 'POST':
#         enrollment_number= request.POST['enrollment_number']
#         student_name = request.POST['student_name']
#         user = authenticate(request, enrollment_number=enrollment_number, student_name=student_name)
#         if user is not None:
#             if user.is_student:  
#                 login(request, user)
#                 return redirect('student_profile')  
#             else:
#                 return redirect('unauthorized')  
#         else:
#             return redirect('login_mismatch')  
#     return render(request, 'student_login.html')


# def student_login(request):
#     if request.method == 'POST':
#         enrollment_number = request.POST['enrollment_number']
#         name = request.POST['name']
#         user = authenticate(request, username=enrollment_number, password=name)
#         print(user)
#         if user is not None:
#             try:
#                 student = Student.objects.get(enrollment_number=enrollment_number, admin=user)
#                 login(request, user)
               
#                 return HttpResponseRedirect(reverse('student_profile'))
#             except Student.DoesNotExist:
#                 pass

#     return render(request, 'student_login.html')

#



# def student_profile(request):
    
#     try:
#         student = Student.objects.get(user=request.user)
#     except Student.DoesNotExist:
      
#         return render(request, 'error.html', {'error_message': 'Student not found.'})
    
#     return render(request, 'student_profile.html', {'student': student})






# def generate_hall_ticket(request):
    
#     try:
#         student = Student.objects.get(user=request.name)
#     except CustomUser.DoesNotExist:
        
#         return render(request, 'error.html', {'error_message': 'Student not found.'})
    
   
#     response = HttpResponse(content_type='application/pdf')
#     response['Content-Disposition'] = f'filename="hall_ticket_{student.enrollment_number}.pdf"'

#     c = canvas.Canvas(response, pagesize=letter)
   
#     c.drawString(100, 750, f'Name: {student.user.username}')
   
#     c.save()

#     return response







# def generate_hall_ticket(request):
#     # Assuming the user is authenticated and you have access to the user object
#     if request.user.is_authenticated:
#         user = request.user
        
#         try:
#             student = CustomUser.objects.get(username=user.username)
#             hall_ticket = HallTicket.objects.get(student=student)
#         except (CustomUser.DoesNotExist, HallTicket.DoesNotExist):
#             return render(request, 'error.html', {'error_message': 'Student or hall ticket not found.'})
    
#         response = HttpResponse(content_type='application/pdf')
#         response['Content-Disposition'] = f'filename="hall_ticket_{student.enrollment_number}.pdf"'

#         c = canvas.Canvas(response, pagesize=letter)
   
#         # Customize the content of the hall ticket here
#         c.drawString(100, 750, f'Name: {student.student_name}')
#         c.drawString(100, 730, f'Program: {student.program}')
#         c.drawString(100, 710, f'Course: {student.course}')
#         c.drawString(100, 690, f'Examination Center Code: {hall_ticket.examination_center_code}')
#         c.drawString(100, 670, f'Examination Center Address: {hall_ticket.examination_center_address}')
#         c.drawString(100, 650, f'Exam Date: {hall_ticket.exam_date}')
#         c.drawString(100, 630, f'Exam Time: {hall_ticket.exam_time}')
#         c.drawString(100, 610, f'Seat Number: {hall_ticket.seat_number}')
   
#         c.save()

#         return response
#     else:
#         return render(request, 'error.html', {'error_message': 'User not authenticated.'})




# def generate_hall_ticket(request, hall_ticket_id):

#     hall_ticket = HallTicket.objects.get(id=hall_ticket_id)
#     response = HttpResponse(content_type='application/pdf')
#     response['Content-Disposition'] = f'filename="hall_ticket_{hall_ticket_id}.pdf"'

#     c = canvas.Canvas(response, pagesize=letter)

#     c.setFont("Helvetica-Bold", 14)
#     c.drawString(100, 750, f'Student Name: {hall_ticket.student.user.username}')
#     c.drawString(100, 730, f'Enrollment Number: {hall_ticket.student.enrollment_number}')

#     c.setFont("Helvetica", 12)
#     c.drawString(100, 710, f'Programme: {hall_ticket.student.programme}')
#     c.drawString(100, 690, f'Course: {hall_ticket.student.course}')

#     c.setFont("Helvetica-Bold", 14)
#     c.drawString(100, 660, 'Exam Details')
#     c.setFont("Helvetica", 12)
#     c.drawString(100, 640, f'Exam Center: {hall_ticket.exam_center_name}')
#     c.drawString(100, 620, f'Exam Date: {hall_ticket.exam_date.strftime("%Y-%m-%d %H:%M:%S")}')

#     c.showPage()
#     c.save()

#     return response


# class CustomLoginView(LoginView):
#     template_name = 'student_login.html'  
#     success_url = reverse_lazy('student_profile')

