# payroll/services.py
from decimal import Decimal, ROUND_HALF_UP
from employees.models import SalaryComponent

def calc_component(base, comp):
    base = Decimal(base)
    value = Decimal(comp.value)
    if comp.is_percent:
        return (base * value / Decimal('100')).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
    else:
        return value.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

def generate_payslip_preview(employee, working_days=30, unpaid_days=0):
    """Return dict with earnings, deductions, gross, net"""
    components = SalaryComponent.objects.all()
    earnings = []
    deductions = []
    gross = Decimal('0.00')

    for c in components:
        amt = calc_component(employee.basic_salary, c)
        if c.component_type == 'EARNING':
            earnings.append({'name': c.name, 'amount': amt})
            gross += amt
        else:
            deductions.append({'name': c.name, 'amount': amt})

    # apply LOP (simple): prorate basic in proportion to unpaid_days
    lop = (Decimal(employee.basic_salary) / Decimal(working_days) * Decimal(unpaid_days)).quantize(
        Decimal('0.01'), rounding=ROUND_HALF_UP)
    if lop > 0:
        deductions.append({'name': 'LOP', 'amount': lop})
        gross -= lop  # you may want to instead deduct from gross, depending on your policy

    total_deductions = sum(d['amount'] for d in deductions)
    net = gross - total_deductions

    return {
        'employee': employee,
        'earnings': earnings,
        'deductions': deductions,
        'gross': gross.quantize(Decimal('0.01')),
        'total_deductions': total_deductions.quantize(Decimal('0.01')),
        'net': net.quantize(Decimal('0.01')),
    }
