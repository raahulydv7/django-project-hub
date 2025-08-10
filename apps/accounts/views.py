from django.shortcuts import render,redirect,get_object_or_404
from .models import CustomUser,Profile
from .forms import UserRegisterForm,LoginForm,ProfileForm
from django.contrib.auth import login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def root(request):
    return render(request,'accounts/root.html')

def create_user(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            messages.success(request,"User created and logged in")
            return redirect('root')
        else:
            messages.error(request,"can't create user try again")
    else:
        form = UserRegisterForm()
    return render(request,'accounts/user_register.html',{'form':form})

def authenticate_user(request):
    if request.method=="POST":
        form = LoginForm(request,data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            messages.success(request,"User Logged in")
            return redirect('root')
        else:
            messages.error(request,'Unable to login user, try again')
    else:
        form = LoginForm()
    
    return render(request,'accounts/login_user.html',{'form':form})

def logout_user(request):
    logout(request)
    messages.success(request,"user logged out")
    return redirect('login')

@login_required
def view_update_user_profile(request):
    user = request.user
    profile = get_object_or_404(Profile, user=user)
    
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=profile)  
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully")
            return redirect('profile')
        else:
            messages.error(request, "Unable to update profile, try again")
    else:
        form = ProfileForm(instance=profile)

    return render(request, 'accounts/user_profile.html', {'form': form, 'profile': profile})