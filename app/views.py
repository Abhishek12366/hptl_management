from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import *
from .forms import *
# import logging
# from django.contrib.auth.views import LoginView
# from django.urls import reverse
# from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
# from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
# from django.contrib import messages
# from django.urls import reverse_lazy




# logger = logging.getLogger(__name__)

def index(request):
    return render(request, 'index.html')






def superadmin_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None and user.is_active:
            if user.is_superuser:
                login(request, user)
                return redirect('superadmin_profile')
            else:
             
                return redirect('unauthorized')
        else:
            
            return redirect('login_mismatch')
    
    return render(request, 'superadmin_login.html')

        

   

@login_required
def admin_profile(request):
    if not request.user.is_admin:
        return redirect('unauthorized')  
    return render(request, 'admin_profile.html')    


@login_required
def superadmin_profile(request):
    if not request.user.is_superuser:
        return redirect('unauthorized')  
    return render(request, 'superadmin_profile.html', {'user': request.user})





@login_required
def new_admin(request):
    if not request.user.is_superuser:
        return redirect('unauthorized')  

    if request.method == 'POST':
        form = AdminCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('superadmin_profile')
    else:
        form = AdminCreationForm()

    return render(request, 'admin_creation.html', {'form': form})


def admin_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_admin:  
                login(request, user)
                return redirect('admin_profile')  
            else:
                return redirect('unauthorized')  
        else:
            return redirect('login_mismatch')  
    return render(request, 'admin_login.html')


def unauthorized(request):
    return render(request, 'unauthorized.html')
def login_mismatch(request):
    return render(request, 'login_mismatch.html')




##>>>><<<<<<<###

# def admin_requests(request):
#     requests = AdminRequest.objects.all()
#     return render(request, 'admin_request.html', {'requests': requests})




# def admin_login(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']

     
#         matching_users = CustomUser.objects.filter(username=username)

    
#         if matching_users.count() == 1:
#             user = matching_users.first() 
#             authenticated_user = authenticate(request, username=username, password=password)
            
#             if authenticated_user is not None:
#                 login(request, authenticated_user)
#                 return redirect('admin_profile')  
#             else:
               
#                 messages.error(request, "Invalid password.")
#         else:
        
#             if matching_users.count() == 0:
#                error_message = "No user found with this username."
#             else:
#                 error_message = "Multiple users found with the same username."

#             messages.error(request, error_message)
    
#     return render(request, 'admin_login.html')






# def create_admin(request):
#     if request.method == 'POST':
#         form = AdminCreationForm(request.POST)
#         if form.is_valid():
#             admin_user = form.save(commit=False)
#             admin_user.is_admin = True
#             admin_user.save()
#             return redirect('admin_profile')  
#     else:
#         form = AdminCreationForm()

#     return render(request, 'create_admin.html', {'form': form})



# def superadmin_login(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
        
#         if user is not None and user.is_active :
#             if user.is_superuser:
            
#                 login(request, user)
#                 return redirect('superadmin_profile')  
#             else:
            
#                     return redirect('unauthorized')  
#         else:
#             return redirect('login_mismatch')  
#     return render(request, 'superadmin_login.html')







# logger = logging.getLogger(__name__)



# def student_login(request):
#     if request.method == 'POST':
#         enrollment_number = request.POST['enrollment_number']
#         student_name = request.POST['student_name']

    
#         user = authenticate(request, username=enrollment_number, password=student_name)

#         if user is not None:
          
#             login(request, user)
#             return redirect('student_profile')
#         else:
        
#             messages.error(request, 'Invalid enrollment number or student name.')

#     return render(request, 'student_login.html')


# def admin_login(request):
#     if request.method == 'POST':
#         form = AdminLoginForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             user = authenticate(request, username=username, password=password)

#             if user is not None and user.is_admin:
#                 login(request, user)
#                 return redirect('admin_profile')
#             else:
#                 # Handle authentication failure
#                 return redirect('login_mismatch')  # You need to define this URL pattern

#     else:
#         form = AdminLoginForm()

#     return render(request, 'admin_login.html', {'form': form})


# @login_required
# def admin_requests(request):
#     requests = AdminRequest.objects.all()
#     return render(request, 'admin_request.html', {'requests': requests})

# def create_admin(request):
#     if request.method == 'POST':
#         form = AdminCreateForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             user.is_staff = True
#             user.save()
#             return redirect('admin_requests')
#     else:
#         form = AdminCreateForm()
#     return render(request, 'create_admin.html', {'form': form})

# def superadmin_login(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(request, username=username, password=password)
#         if user is not None and user.is_active and user.is_superadmin:
#             login(request, user)
#             return redirect('admin_requests')
#         else:
#             message = "Unauthorized user"
#             return render(request, 'superadmin_login.html', {'message': message})
#     return render(request, 'superadmin_login.html')


# @login_required  # Ensure that only authenticated users can access this view
# def admin_profile_view(request):
#     # Retrieve information about the logged-in admin (you can customize this)
#     admin = request.user

#     # Pass the admin object to the template for rendering
#     context = {'admin': admin}
#     return render(request, 'admin_profile.html', context) 