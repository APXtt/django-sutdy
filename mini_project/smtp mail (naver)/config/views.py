from django.shortcuts import render, redirect
from django.core.mail import send_mail


def index(request):
    return render(request, 'index.html')


def mailsend(request):
    send_mail('title' # <- 메일의 제목
            , 'body' # <- 메일의 본문
            , 'okjoop213@naver.com' # <- 메일의 전송자
            , ['dfwtt11@gmail.com'] # <- 메일의 수신자
            , fail_silently=False) # <- 이메일 전송 실패에 대한 로그나 오류가 표시되지 않음

    return redirect('')
