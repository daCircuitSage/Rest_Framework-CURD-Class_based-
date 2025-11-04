from django.contrib import admin
from app2.models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display=['name','roll','city']