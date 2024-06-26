from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import auth
from django.contrib import messages

from favourites.models import Favourite
from .forms import CustomUserCreationForm

from django.shortcuts import render

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # login(request, user)
            send_mail(
                'Welcome to Movie Platform',
                'Your registration was successful!',
                settings.DEFAULT_FROM_EMAIL,
                [user.email],
                fail_silently=False,
            )
            return redirect('custom_login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'profile/register.html', {'form': form})

def custom_login(request):

    if request.method == 'POST':
        email = request.POST['email']
        password= request.POST['password']
        
        user = authenticate(request, email=email,password=password)
        
        if user is not None:
            login(request, user)
            #messages.success(request,'You are logged in.')
            return redirect('movie_list')
        else:
            messages.error(request,'Invalid credentials!')
            return redirect('custom_login')
            
    return render(request, 'profile/login.html')


@login_required(login_url='login')
def custom_logout(request):
    logout(request)
    
    return redirect('movie_list')




@login_required()
def view_profile(request):
    is_favourite = False
    if request.user.is_authenticated:
        is_favourite = Favourite.objects.filter(user=request.user).exists()
    return render(request,'profile/view_profile.html',{'user':request.user,'is_favourite':is_favourite})

@login_required
def edit_profile(request):
    if request.method == 'POST':
        user_form = CustomUserCreationForm(request.POST, instance=request.user)
        if user_form.is_valid():
            user_form.save()
            return redirect('view_profile')
    else:
        user_form = CustomUserCreationForm(instance=request.user)

    return render(request, 'profile/edit_profile.html', {
        'user_form': user_form,
    })