from django.contrib import admin
from .models import StudentsAmount, StudentRequest, PhoneNumbers
# Register your models here.

admin.site.register(StudentsAmount)
admin.site.register(StudentRequest)
admin.site.register(PhoneNumbers)