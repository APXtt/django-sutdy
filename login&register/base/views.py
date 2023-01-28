from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import UseForm


# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UseForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index') # index url 경로가 있다고 가정
    else:
        form = UseForm()
    return render(request, 'register.html', {'form': form})