
from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .models import *
from hallticket.models import*

class AdminCreateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password']

class AdminRequestForm(forms.ModelForm):
    class Meta:
        model = AdminRequest
        fields = ['name', 'email', 'password']


class AdminCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2', 'is_active', 'is_superuser')



class StudentAdminForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

class HallTicketAdminForm(forms.ModelForm):
    class Meta:
        model = HallTicket
        fields = '__all__'


class StudentLoginForm(AuthenticationForm):
    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        user = CustomUser.objects.filter(username=username, is_student=True).first()

        if user is None:
            raise forms.ValidationError('User not found or is not a student.')

        if not user.check_password(password):
            raise forms.ValidationError('Incorrect password.')

        return cleaned_data

# class AdminLoginForm(AuthenticationForm):
#     class Meta:
#         model = CustomUser  
#         fields = ['username']

class AdminLoginForm(AuthenticationForm):
    class Meta:
        model = CustomUser  
        fields = ['username', 'password']