from django.contrib import admin

# Register your models here.
from .models import *
from .forms import*
from hallticket.models import*

admin.site.register(CustomUser)
# admin.site.register(AdminRequest)


# @admin.register(CustomUser)
# class StudentAdmin(admin.ModelAdmin):
#     form = StudentAdminForm

@admin.register(HallTicket)
class HallTicketAdmin(admin.ModelAdmin):
    form = HallTicketAdminForm
