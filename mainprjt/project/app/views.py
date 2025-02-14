from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import *
from django.http import HttpResponse
from .forms import RegisterForm
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect(login_view)
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home') 
            else:
                messages.error(request, 'Invalid username or password')
        else:
            messages.error(request, 'Invalid form submission')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')

def home(request):
    return render(request,'home.html')

def categories(request):
    return render(request,'categories.html')


CATEGORIES = {
    "ui-ux-design": ["UI/UX Designer", "Web Designer", "Mobile App Designer", "Wireframe & Prototype Designer"],
    "graphic-design": ["Graphic Designer", "Illustrator", "Logo & Brand Identity Designer", "Packaging Designer"],
    "digital-marketing": ["Social Media Designer", "Motion Graphics Designer", "Infographic Designer", "Advertising Designer"],
    "multimedia": ["Video Editor", "3D Designer", "Game UI/UX Designer", "VR/AR Designer"],
    "product-design": ["Product Designer", "Interior Designer", "Fashion Designer", "Jewelry Designer"],
}

# View for the main categories page
def categories(request):
    return render(request, 'categories.html', {"categories": CATEGORIES})

# View for the category details page (subcategories)
def category_detail(request, category_slug):
    subcategories = CATEGORIES.get(category_slug, [])
    return render(request, 'category_detail.html', {"category_slug": category_slug, "subcategories": subcategories})
