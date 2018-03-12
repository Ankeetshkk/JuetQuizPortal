from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib import messages

def index(request):
    return render(request,'MCQ/welcome_template.html')

def question_entry(request):
    return render(request,'MCQ/question_entry_template.html')

def test_area(request):
    return render(request,'MCQ/test_area_template.html')

def signup(request):
    return render(request,'MCQ/signup_template.html')

def register(request):
    if request.method == 'POST':
        f = UserCreationForm(request.POST)
        if f.is_valid():
            f.save()
            messages.success(request, 'Account created successfully')
            return redirect('register')

    else:
        f = UserCreationForm()

    return render(request, 'cadmin/register.html', {'form': f})