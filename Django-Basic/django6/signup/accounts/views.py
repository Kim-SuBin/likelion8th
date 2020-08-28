from django.shortcuts import render, redirect
from django.contrib.auth.models import User  # User model 연결 
from django.contrib import auth # login 기능 구현을 위해 추가

# Create your views here.
def index(request):
    return render(request, 'index.html')

def signup(request):
    # POST method 요청이 들어올때
    if request.method == 'POST':
        # 입력한 password1과 password2가 만약 같으면
        if request.POST['password1'] == request.POST['password2']:
            # 새로운 회원을 만들고
            User.objects.create_user(request.POST['username'], password=request.POST['password1']) 
        # index로 돌아간다. 
        return redirect('index')  
    # 위의 경우가 아닐때 그냥 signup페이지를 다시 리턴한다. 
    return render(request, 'signup.html')
    
def login(request):
    # POST method 요청이 들어올떄 
    if request.method == 'POST':
        # 입력받은 아이디와 비밀번호가 데이터베이스에 있는지 확인한다. 
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        # 해당 데이터의 유저가 있다면 
        if user is not None: 
            # 로그인하고 index로 리다이렉트한다. 
            auth.login(request, user)
            return redirect('index')
        else:
            # 없다면, 에러를 표시하고, login페이지 로 이동(새로고침)
            return render(request, 'login.html', {'error': 'username or password is incorrect.'})
    else:
        # POST 요청이 아닐경우 login 페이지 새로고침
        return render(request, 'login.html')

def logout(request):
    # 로그아웃 하고 index로 리다이렉트
    auth.logout(request)
    return redirect('index')

def userpage(request):
    # 로그인 했을 경우 해당 페이지 접속
    if request.user.is_authenticated: 
        return render(request, 'userpage.html')
    # 그렇지 않을 경우 index로 돌아가기
    else:
        return render(request, 'index.html', { 'error': 'Only site member can accesss userpage'})