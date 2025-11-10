from datetime import date

def generate_payslip_preview(employee, working_days, unpaid_days):
    """
    Generate a simple preview of the payslip for an employee.
    """
    # Let's assume employee has fields: basic_salary, allowances, deductions
    try:
        basic = employee.basic_salary
        allowances = employee.allowances or 0
        deductions = employee.deductions or 0
    except AttributeError:
        print("Employee object is missing required fields.")
        return None

    # Basic salary computation
    per_day_salary = basic / working_days
    payable_salary = per_day_salary * (working_days - unpaid_days)

    gross_salary = payable_salary + allowances
    net_salary = gross_salary - deductions

    print("\n------ PAYSLIP PREVIEW ------")
    print(f"Employee: {employee.name}")
    print(f"Working Days: {working_days}")
    print(f"Unpaid Days: {unpaid_days}")
    print(f"Basic Pay: ₹{basic:.2f}")
    print(f"Allowances: ₹{allowances:.2f}")
    print(f"Deductions: ₹{deductions:.2f}")
    print(f"Net Salary: ₹{net_salary:.2f}")
    print("-----------------------------\n")

    return {
        "employee": employee.name,
        "working_days": working_days,
        "unpaid_days": unpaid_days,
        "net_salary": net_salary,
        "date": date.today()
    }
