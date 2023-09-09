from django.shortcuts import render,redirect
from app.forms import*
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from app.models import *
from.models import *


class CustomLoginView(LoginView):
    template_name = 'student_login.html'  
    success_url = reverse_lazy('student_profile')

def new_student_registration(request):
    if request.method == 'POST':
        form =StudentAdminForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_profile')  # Redirect to admin profile or another appropriate page
    else:
        form = StudentAdminForm()

    return render(request, 'student_registration.html', {'form': form})



from app.forms import HallTicketAdminForm  # Import forms from the 'app' app

def new_hall_ticket_registration(request):
    if request.method == 'POST':
        form = HallTicketAdminForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_profile')
    else:
        form = HallTicketAdminForm()

    return render(request, 'hall_ticket_registration.html', {'form': form})



# def student_login(request):
#     if request.method == 'POST':
#         enrollment_number = request.POST['enrollment_number']
#         student_name = request.POST['student_name']

       
#         matching_users = CustomUser.objects.filter(enrollment_number=enrollment_number, student_name=student_name)

       
#         if matching_users.count() == 1:
#             user = matching_users.first()  
#             login(request, user)
#             return redirect('student_profile')  
#         else:
          
#             if matching_users.count() == 0:
#                 error_message = "No user found with this enrollment number and student name."
#             else:
#                 error_message = "Multiple users found with the same enrollment number and student name."

#             messages.error(request, error_message)
    
#     return render(request, 'student_login.html')


def student_login(request):
    if request.method == 'POST':
        enrollment_number = request.POST['enrollment_number']
        student_name = request.POST['student_name']

        print(f"Received enrollment_number: {enrollment_number}")
        print(f"Received student_name: {student_name}")

     
        user = authenticate(request, username=enrollment_number, password=student_name)

        if user is not None:

            login(request, user)
            return redirect('student_profile')
        else:
            messages.error(request, 'Invalid enrollment number or student name.')

    return render(request, 'student_login.html')


# def student_login(request):
#     if request.method == 'POST':
#         enrollment_number = request.POST['enrollment_number']
#         name = request.POST['name']
#         student = authenticate(request, enrollment_number=enrollment_number, name=name)
#         if student is not None:
#             login(request, student)
#             # Redirect to student's profile or dashboard
#             return redirect('student_profile')
#         else:
#             # Authentication failed, show an error message
#             return render(request, 'student_login.html', {'error_message': 'Invalid credentials'})
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


@login_required
def student_profile(request):
   
    student = request.user 
    
    context = {
        'student': student,
        
    }
    
    return render(request, 'hall_ticket/student_profile.html', context)


# def student_profile(request):
    
#     try:
#         student = Student.objects.get(user=request.user)
#     except Student.DoesNotExist:
      
#         return render(request, 'error.html', {'error_message': 'Student not found.'})
    
#     return render(request, 'student_profile.html', {'student': student})


@login_required
def student_dashboard(request):
    
    student = request.user 
    
    context = {
        'student': student,
  
    }
    
    return render(request, 'hall_ticket/student_dashboard.html', context)


def generate_hall_ticket(request):
    
    try:
        student = Student.objects.get(user=request.user)
    except Student.DoesNotExist:
        
        return render(request, 'error.html', {'error_message': 'Student not found.'})
    
   
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'filename="hall_ticket_{student.enrollment_number}.pdf"'

    c = canvas.Canvas(response, pagesize=letter)
   
    c.drawString(100, 750, f'Name: {student.user.username}')
   
    c.save()

    return response





