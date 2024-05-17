from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from user.forms import RegisterForm, LoginForm
from user.models import Profile


def register_view(request):
    if request.method == "GET":
        form = RegisterForm()

        return render(request, 'user/register.html', {'form': form})

    if request.method == "POST":
        form = RegisterForm(request.POST, request.FILES)

        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                password=form.cleaned_data['password']
            )
            Profile.objects.create(
                user=user,
                avatar=form.cleaned_data['avatar']
            )
            return redirect('main')

        return render(request, 'user/register.html', {'form': form})


def login_view(request):
    if request.method == "GET":
        form = LoginForm()
        return render(request, 'user/login.html', {'form': form})

    if request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )

            if user is not None:
                login(request, user)
                return redirect('main')
            form.add_error(None, "Неправильный логин или пароль")

        return render(request, 'user/login.html', {'form': form})


def logout_view(request):
    if request.method == "GET":
        logout(request)
        return redirect('main')


@login_required(login_url='/login/')
def profile_view(request):
    if request.method == "GET":
        return render(request, 'user/profile.html')