from django.contrib import admin
from .models import User, Student, Teacher, Admin
# Register your models here.

admin.site.register(Student)
admin.site.register(User)
admin.site.register(Teacher)
admin.site.register(Admin)
