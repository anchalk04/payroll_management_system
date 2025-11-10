from django.urls import path
from django.http import HttpResponse

def placeholder(request):
    return HttpResponse("<h2>Accounts module coming soon</h2>")

urlpatterns = [
    path('', placeholder),
]
