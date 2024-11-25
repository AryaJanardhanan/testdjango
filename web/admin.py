from django.contrib import admin
from .models import *

# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display = ('course', 'name')
    search_fields = ('age', 'place', 'course')
    list_filter = ('course', 'age')

    
admin.site.register(Student, StudentAdmin)