from django.shortcuts import render, get_object_or_404, redirect
from .models import Post # models에서 Post를 가져옴
from django.utils import timezone

# Create your views here.

# model에서 templates를 보내기 위해서는 view를 거쳐야함
def home(request): 
    posts = Post.objects # Post 객체(데이터)를 담는 변수
    return render(request, 'home.html', {'posts':posts}) # posts에 담긴 데이터들을 넘겨준다는 의미

def detail(request, post_id):
    post_detail = get_object_or_404(Post, pk=post_id)
    return render(request, 'detail.html', {'post':post_detail})

def new(request):
    return render(request, 'new.html')

def create(request):
    post = Post()
    post.title = request.GET['title']
    post.body = request.GET['body']
    post.pub_date = timezone.datetime.now()
    post.save()
    return redirect('/' + str(post.id))