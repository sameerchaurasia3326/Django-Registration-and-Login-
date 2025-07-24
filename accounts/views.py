from django.contrib.auth.forms import AuthenticationForm , UserCreationForm
from django.contrib.auth import login as auth_login
from django.shortcuts import render , redirect

def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('index')  # or wherever you want to redirect after login
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})