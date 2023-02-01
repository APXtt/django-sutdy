from django.db import models
from django.utils import timezone
import datetime

# Create your models here.

class Question(models.Model): # 이렇게 상속받을 경우 실제로 데이터베이스와 ORM 동작을 해서 맵핑함
    def __str__(self):
        return self.question_text
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class Choice(models.Model):
    def __str__(self):
        return self.choice_text
    
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

"""
models 클래스의 각 변수들은 자료형을 나타냄
date published는 사람이 읽기 쉬운 형태의 Datetime
타 모델과 관계를 맺기 위해서는 ForeignKey를 사용(왜래키)
"""