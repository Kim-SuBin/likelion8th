from django.shortcuts import render,redirect 
from django.contrib.auth.models import User
from django.contrib import auth

def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            User.objects.create_user(request.POST['username'], password=request.POST['password1']) 
        return redirect('index')  
    return render(request, 'signup.html')
    
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None: 
            auth.login(request, user)
            return redirect('index')
        else:
            return render(request, 'login.html', {'error': 'username or password is incorrect.'})
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('index')

def index(request):
    return render(request, 'index.html')

def userpage(request):
    if request.user.is_authenticated: 
        return render(request, 'userpage.html')
    else:
        return render(request, 'index.html', { 'error': 'Only site member can accesss userpage'})