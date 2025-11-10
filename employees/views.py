from django.shortcuts import render, redirect
from .models import Employee

# Show list of employees
def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employees/list.html', {'employees': employees})

# Create a new employee
def employee_create(request):
    if request.method == 'POST':
        emp_code = request.POST.get('emp_code')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        designation = request.POST.get('designation')
        basic_salary = request.POST.get('basic_salary', 0)

        Employee.objects.create(
            emp_code=emp_code,
            first_name=first_name,
            last_name=last_name,
            designation=designation,
            basic_salary=basic_salary
        )
        return redirect('employee_list')
    
    return render(request, 'employees/create.html')
