from django.urls import path
from . import views

urlpatterns = [
    path('', views.payroll_home, name='payroll_home'),  # <--- new route
    path('payslip/<int:emp_id>/', views.payslip_view, name='payslip_view'),
]
