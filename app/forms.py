
from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .models import *
from hallticket.models import*
from django.contrib.auth import get_user_model


class AdminLoginForm(AuthenticationForm):
    class Meta:
        model = CustomUser  
        fields = ['username', 'password']


class AdminCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2', 'is_active', 'is_superuser')

class StudentLoginForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username','password1', 'password2')



class StudentAdminForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2', 'is_active', 'is_student','enrollment_number', 'name', 'email', 'address', 'aadhaar_number', 'program', 'course',)



class HallTicketAdminForm(forms.ModelForm):
    class Meta:
        model = HallTicket
        fields = '__all__'










#>>>>>>>>>>>>><<<<<<<<<<<<<#







# class StudentLoginForm(AuthenticationForm):
#     def clean(self):
#         cleaned_data = super().clean()
#         username = cleaned_data.get('username')
#         password = cleaned_data.get('password')

#         user = CustomUser.objects.filter(username=username, is_student=True).first()

#         if user is None:
#             raise forms.ValidationError('User not found or is not a student.')

#         if not user.check_password(password):
#             raise forms.ValidationError('Incorrect password.')

#         return cleaned_data

# class StudentLoginForm(AuthenticationForm):
#     enrollment_number = forms.CharField(max_length=20, required=True)
#     student_name = forms.CharField(max_length=100, required=True)

#     def clean(self):
#         cleaned_data = super().clean()
#         enrollment_number = cleaned_data.get('enrollment_number')
#         student_name = cleaned_data.get('student_name')

#         User = get_user_model()

#         user = User.objects.filter(username=enrollment_number, is_student=True).first()

#         if user is None:
#             raise forms.ValidationError('No student found with this enrollment number.')

#         if user.student_profile.name != student_name:
#             raise forms.ValidationError('Incorrect student name.')

#         return cleaned_data


# class AdminLoginForm(AuthenticationForm):
#     class Meta:
#         model = CustomUser  
#         fields = ['username']




# class StudentLoginForm(AuthenticationForm):
#     class Meta:
#         model = Student
#         fields= ['password', 'enrollment_number']

# class StudentRegistrationForm(UserCreationForm):
#     enrollment_number = forms.CharField(max_length=20, required=True)
#     name = forms.CharField(max_length=100, required=True)
#     email = forms.EmailField(max_length=255, required=True)
#     address = forms.CharField(widget=forms.Textarea, required=True)
#     aadhaar_number = forms.CharField(max_length=12, required=True)
#     program = forms.CharField(max_length=100, required=True)
#     course = forms.CharField(max_length=100, required=True)

#     class Meta:
#         model = Student
#         fields = ('enrollment_number', 'name', 'email', 'address', 'aadhaar_number', 'program', 'course', 'password1', 'password2')


# class StudentLoginForm(forms.Form):
#     enrollment_number = forms.CharField(max_length=20, required=True)
#     password = forms.CharField(widget=forms.PasswordInput, required=True)

# class AdminCreateForm(forms.ModelForm):
#     class Meta:
#         model = CustomUser
#         fields = ['username', 'email', 'password']

# class AdminRequestForm(forms.ModelForm):
#     class Meta:
#         model = AdminRequest
#         fields = ['name', 'email', 'password']