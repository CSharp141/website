from datetime import datetime
from django.dispatch import receiver
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import authenticate, login, logout
import requests
from .forms import signUpForm, LoginForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import Group
from django.contrib.auth.signals import user_logged_out
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Product
from .forms import ProductForm
from django.core.files.base import ContentFile



def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('dashBoard')   
                
    else:
        form = LoginForm()
        
    return render(request, 'login.html', {'form': form})

def user_signup(request):
    if request.method == 'POST':
        form = signUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Registration successful. Please log in with your new credentials.')

            # Redirect to the login page
            return redirect('login')
    else:
        form = signUpForm()

    return render(request, 'signup.html', {'form': form})

@login_required(login_url='login')
def dashboard(request):
    user = request.user
    user_group = user.groups.first()
    return render(request, 'dashBoard.html', {'user_group': user_group, 'user': user})

@login_required(login_url='login')
def inventory(request):
    user = request.user
    user_group = user.groups.first()
    return render(request, 'inventory.html', {'user_group': user_group, 'user': user})

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            # Extract data from the form
            product = form.save(commit=False)
            
            # Handle image URL
            image_url = form.cleaned_data.get('image')
            if image_url:
                # Download the image
                response = requests.get(image_url)
                if response.status_code == 200:
                    # Save the image to the model's image field
                    product.image.save(
                        f"{product.barcode}.jpg",  # Use a unique name for the image file
                        ContentFile(response.content),
                        save=False
                    )
            
            # Save the product instance
            product.save()
            return redirect("inventory")
    else:
        form = ProductForm()
    
    return render(request, 'inventory.html', {'form': form})



