from django.shortcuts import render,redirect 
from django.contrib.auth.models import User

def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            User.objects.create_user(request.POST['username'], password=request.POST['password1']) 
        return redirect('index')  
    return render(request, 'signup.html')
    
def login(request):
    return render(request, 'login.html')

def logout(request):
    return render(request, 'logout.html')

def index(request):
    return render(request, 'index.html')