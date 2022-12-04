from django.contrib import admin

from student.models import Student, StudentToSection

admin.site.register(Student)
admin.site.register(StudentToSection)