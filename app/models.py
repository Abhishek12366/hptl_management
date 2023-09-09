from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser,User,AbstractBaseUser

class CustomUser(AbstractUser):
    is_superadmin = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    enrollment_number = models.CharField(max_length=20, unique=True,null=True, blank=True)
    student_name = models.CharField(max_length=100,null=True, blank=True)

    def __str__(self):
        return self.username

User._meta.get_field('user_permissions').remote_field.related_name = 'original_user_permissions'
User._meta.get_field('groups').remote_field.related_name = 'original_groups'

class AdminRequest(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    is_accepted = models.BooleanField(default=False)

class StudentProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    program = models.CharField(max_length=50)
    course = models.CharField(max_length=50)

    def __str__(self):
        return self.user.username

    

# class CustomUser(AbstractUser):
#     is_admin = models.BooleanField(default=False)  

#     def __str__(self):
#         return self.username


