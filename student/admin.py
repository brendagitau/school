from django.contrib import admin
from .models import Student
# Register your models   here. Make migrations before this.alows you to control your db from the django admin dashboard.create super user(pytho manage.pi createsuperusa)
admin.site.register(Student)
