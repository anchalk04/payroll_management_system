from django.db import models

class Employee(models.Model):
    emp_code = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=20, blank=True)
    designation = models.CharField(max_length=100, blank=True)
    department = models.CharField(max_length=100, blank=True)
    join_date = models.DateField(null=True, blank=True)
    basic_salary = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    bank_account = models.CharField(max_length=50, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.emp_code} - {self.first_name} {self.last_name}"

class SalaryComponent(models.Model):
    COMPONENT_TYPES = (
        ('EARNING', 'Earning'),
        ('DEDUCTION', 'Deduction'),
    )
    name = models.CharField(max_length=100)
    component_type = models.CharField(max_length=10, choices=COMPONENT_TYPES)
    is_percent = models.BooleanField(default=False)
    value = models.DecimalField(max_digits=7, decimal_places=2,
                                help_text="If percent, value is percent e.g. 12.5; otherwise amount")

    def __str__(self):
        return f"{self.name} ({self.component_type})"
