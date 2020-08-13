from django.db import models

# Create your models here.
class Post(models.Model): # 항상 첫 글자는 대문자로!
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()
    
    def __str__(self): # 타이틀을 보여줌
        return self.title
        
    def summary(self):
        return self.body[:20]