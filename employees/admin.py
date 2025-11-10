from django.contrib import admin
from .models import Employee, SalaryComponent

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('emp_code', 'first_name', 'last_name', 'designation', 'basic_salary', 'is_active')
    search_fields = ('emp_code', 'first_name', 'last_name', 'designation')

@admin.register(SalaryComponent)
class SalaryComponentAdmin(admin.ModelAdmin):
    list_display = ('name', 'component_type', 'is_percent', 'value')
