from django.shortcuts import render, get_object_or_404
from employees.models import Employee
from decimal import Decimal
def payroll_home(request):
    employees = Employee.objects.all()
    return render(request, 'payroll/home.html', {'employees': employees})

from django.shortcuts import render, get_object_or_404
from employees.models import Employee
from decimal import Decimal

def payslip_view(request, emp_id):
    employee = get_object_or_404(Employee, id=emp_id)

    gross = employee.basic_salary or Decimal('0')
    deductions = gross * Decimal('0.1')  # 10% deduction
    net = gross - deductions

    context = {
        'employee': employee,
        'gross': gross,
        'deductions': deductions,
        'net': net
    }
    return render(request, 'payroll/payslip.html', context)
