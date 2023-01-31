from django.shortcuts import render,  get_object_or_404
from django.contrib.auth import get_user_model

def index(request):
    return render(request, 'app/index.html')

def detail(request, pk):
    User = get_user_model()
    user =  get_object_or_404(User, pk=pk) # 만약 모델 객체가 존재하지 않을 경우 http404 exception(예외)을 발생
    context = {
        'user': user
    }
    return render(request, 'app/detail.html', context)
