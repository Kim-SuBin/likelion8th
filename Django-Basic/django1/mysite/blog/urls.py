# 기본 path 함수를 사용하기위해 똑같이 해당 기능을 import 해줍니다. 
from django.urls import path
# 프로젝트에서는 어떤 app의 views 인지 알기위해 blog.views 로 앱부터 명시했지만 여기에서는 동일 폴더내에 있는 views 라는것을 명시하기위해 form .(현재폴더) import views 로 사용했습니다. 
from . import views

urlpatterns = [
	# Index
    ## 프로젝트의 urls 와의 차이점은 어떤 App 내의 view 인지 명시하는 부분이 빠졌다는것 한가지 입니다. 
    path('', views.index, name='index'),
    path('sorry', views.sorry, name='sorry'),
]