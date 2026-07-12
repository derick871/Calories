from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import *
from django.contrib import messages

# Create your views here.
def register(request):
    return render(request, 'register.html')

def login(request):
    return render(request, 'login.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def food_list(request,):
    return render(request, 'food_list')


def subscriber(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if subscriber.object.filter(email=email).exists():
            messages.error(request, 'Email already registered.')
        else:
            subscriber.objects.create(email=email)
            messages.success(request, 'Successfully registered.')
    return render(request, 'register.html')