from django.shortcuts import render,redirect, get_object_or_404
from .models import Profile
from django.contrib.auth.models import User
from django.contrib import auth 

# Create your views here.


def signup(request):
    if request.method=='POST':
        if request.POST.get('password1')==request.POST.get('password2'):
            user = User.objects.create_user(request.POST.get('username'), password = request.POST.get('password1'))
            profile = Profile()
            profile.name = request.POST.get('name')
            profile.user = user
            profile.save()
            auth.login(request, user)
            return redirect('home')
    return render(request,'signup.html')

def login(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username = username, password = password)
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            return render(request,'login.html',{'error':'username or password is incorrect.'})
    else:
        return render(request,'login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')
    return render(request,'signup.html')

def profile(request, user_id):
    profile_user = User.objects.get(id=user_id)
    profile = get_object_or_404(Profile, user = profile_user)
    return render(request, 'profile.html',{'profile':profile})