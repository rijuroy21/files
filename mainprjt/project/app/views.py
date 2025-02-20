from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import *
from django.http import HttpResponse
from .forms import RegisterForm
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import FreelancerEditForm

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
                return redirect('home')  # Redirect to account page after login
            else:
                messages.error(request, 'Invalid username or password')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')

def home(request):
    freelancers = Freelancer.objects.all()
    return render(request,'home.html',{'freelancers': freelancers})

@login_required
def contact(request):
    return render(request, 'contact.html')

@login_required
def how_it_works(request):
    return render(request, 'how_it_works.html')

@login_required
def categories(request):
    categories = Category.objects.all()
    return render(request, 'categories.html', {'categories': categories})

@login_required
def category_detail(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    subcategories = category.subcategories.all()
    return render(request, 'category_detail.html', {'category': category, 'subcategories': subcategories})

@login_required
def subcategory_detail(request, subcategory_id):
    subcategory = get_object_or_404(SubCategory, id=subcategory_id)
    freelancers = subcategory.freelancers.all()
    return render(request, 'subcategory_detail.html', {'subcategory': subcategory, 'freelancers': freelancers})

@login_required
def join(request):
    if request.method == 'POST':
        # Retrieve data from the form
        name = request.POST.get('name')
        email = request.POST.get('email')
        category_name = request.POST.get('category')
        subcategory_name = request.POST.get('subcategory')
        portfolio_url = request.POST.get('portfolio')
        bio = request.POST.get('bio')

        # Fetch the Category object
        category = Category.objects.get(name=category_name)
        # Fetch the SubCategory object
        subcategory = SubCategory.objects.get(name=subcategory_name)

        # Save the data into the database
        freelancer = Freelancer(
            name=name,
            email=email,
            category=category,
            subcategory=subcategory,
            portfolio_url=portfolio_url,
            bio=bio
        )
        freelancer.save()

        return redirect('home')
    return render(request,'join.html')

@login_required
def profile(request,freelancer_id):
    freelancer = get_object_or_404(Freelancer, id=freelancer_id)
    return render(request,'profile.html',{'freelancer': freelancer})


@login_required
def my_account(request):
    freelancer = Freelancer.objects.filter(email__iexact=request.user.email).first()  # Case-insensitive lookup

    if not freelancer:
        messages.error(request, "No freelancer profile found for this account. Please create one.")
        return redirect('join')  # Redirect to join page where they can create a profile

    if request.method == 'POST':
        form = FreelancerEditForm(request.POST, instance=freelancer)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated successfully.')
            return redirect('my_account')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = FreelancerEditForm(instance=freelancer)

    return render(request, 'my_account.html', {'form': form, 'freelancer': freelancer})
