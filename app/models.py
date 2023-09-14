
from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser,User
from django.contrib.auth.hashers import make_password, check_password


class CustomUser(AbstractUser):
    is_superadmin = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    enrollment_number = models.CharField(max_length=20, unique=True,null=True, blank=True)
    student_name = models.CharField(max_length=100,null=True, blank=True)
    program=models.CharField(max_length=100,null=True, blank=True)
    aadhaar_number=models.CharField(max_length=100,null=True, blank=True)
    name=models.CharField(max_length=100,null=True, blank=True)
    course=models.CharField(max_length=100,null=True, blank=True)
    address=models.CharField(max_length=100,null=True, blank=True)

    def __str__(self):
        return self.username

User._meta.get_field('user_permissions').remote_field.related_name = 'original_user_permissions'
User._meta.get_field('groups').remote_field.related_name = 'original_groups'








#>>>>>>>>><<<<<##





# class AdminRequest(models.Model):
#     name = models.CharField(max_length=100)
#     email = models.EmailField()
#     password = models.CharField(max_length=100)
#     is_accepted = models.BooleanField(default=False)

# class StudentProfile(models.Model):
#     user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
#     program = models.CharField(max_length=50)
#     course = models.CharField(max_length=50)

#     def __str__(self):
#         return self.user.username


# class Student(models.Model):
#     # user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='student')
#     student_name = models.CharField(max_length=100,default='abc')
#     address = models.TextField(max_length=100,null=True)
#     aadhaar_number = models.CharField(max_length=12,null=True)
#     program = models.CharField(max_length=12,null=True)
#     course = models.CharField(max_length=12,null=True)
#     enrollment_number = models.CharField(max_length=20, unique=True,default=123)
    

#     USERNAME_FIELD = 'username'
  
#     def set_password(self, raw_password):
#         self.password = make_password(raw_password)
    
#     def check_password(self, raw_password):
#         return check_password(raw_password, self.password)

#     def __str__(self):
#         return self.student_name
    

# class CustomUser(AbstractUser):
#     is_admin = models.BooleanField(default=False)  

#     def __str__(self):
#         return self.username



# from django.contrib.auth.models import AbstractUser, BaseUserManager, Group, Permission
# from django.db import models

# class CustomUserManager(BaseUserManager):
#     def create_user(self, username, password=None, **extra_fields):
#         extra_fields.setdefault('is_active', True)
#         user = self.model(username=username, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, username, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)

#         if extra_fields.get('is_staff') is not True:
#             raise ValueError('Superuser must have is_staff=True.')
#         if extra_fields.get('is_superuser') is not True:
#             raise ValueError('Superuser must have is_superuser=True.')

#         return self.create_user(username, password, **extra_fields)

# class CustomUser(AbstractUser):
#     is_superadmin = models.BooleanField(default=False)
#     is_admin = models.BooleanField(default=False)
#     is_student = models.BooleanField(default=False)

#     objects = CustomUserManager()

# class AdminRequest(models.Model):
#     name = models.CharField(max_length=100)
#     email = models.EmailField()
#     password = models.CharField(max_length=100)
#     is_accepted = models.BooleanField(default=False)

# class StudentProfile(models.Model):
#     user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
#     program = models.CharField(max_length=50)
#     course = models.CharField(max_length=50)

#     def __str__(self):
#         return self.user.username

# class Student(models.Model):
#     # user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
#     student_name = models.CharField(max_length=100)
#     address = models.TextField()
#     aadhaar_number = models.CharField(max_length=12)
#     program = models.CharField(max_length=50)
#     course = models.CharField(max_length=50)
#     enrollment_number = models.CharField(max_length=20, unique=True)

#     def __str__(self):
#         return self.student_name



