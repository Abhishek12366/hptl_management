

from django.contrib.auth.backends import ModelBackend
from hallticket .models import *

# class StudentBackend(ModelBackend):
#     def authenticate(self, request, enrollment_number=None, name=None):
#         try:
#             student = Student.objects.get(enrollment_number=enrollment_number, name=name)
#         except Student.DoesNotExist:
#             return None
        
#         return student if self.user_can_authenticate(student) else None

#     def get_user(self, user_id):
#         try:
#             return Student.objects.get(pk=user_id)
#         except Student.DoesNotExist:
#             return None

class StudentBackend(ModelBackend):
    def authenticate(self, request, enrollment_number=None, student_name=None, **kwargs):
        try:
            user = CustomUser.objects.get(enrollment_number=enrollment_number, student_name=student_name)
            return user
        except CustomUser.DoesNotExist:
            return None