from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render

# Simple homepage view
def home(request):
    return render(request, 'home.html')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),  # Root homepage
    path('accounts/', include('accounts.urls')),
    path('employees/', include('employees.urls')),
    path('payroll/', include('payroll.urls')),
]
