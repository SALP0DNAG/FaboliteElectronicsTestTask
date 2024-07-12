from django.shortcuts import render, HttpResponseRedirect, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib import auth, messages
from .models import User
from . import forms


def login(request):
    if request.method == 'POST':
        form = forms.UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('app:profile'))
    else:
        form = forms.UserLoginForm()
    context = {
        'form': form
    }
    return render(request, 'app/login.html', context=context)


def register(request):
    if request.method == 'POST':
        form = forms.UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Вы успешно зарегестрировались!')
            return HttpResponseRedirect(reverse('app:login'))
    else:
        form = forms.UserRegistrationForm()
    context = {'form': form}
    return render(request, 'app/register.html', context=context)


def list_users(request):
    users = User.objects.all()
    context = {
        'users': users,
    }
    return render(request, 'app/list_users.html', context=context)


@login_required
def profile(request):
    if request.method == 'POST':
        form = forms.UserChangeForm(data=request.POST, instance=request.user)
        if (User.objects.filter(email=request.POST['email']).exists() and
                request.user.email != request.POST['email']):  # Проверка занятости введенного email пользователем
            messages.error(request, 'Почта с таким адресом уже существует')
        if (User.objects.filter(username=request.POST['username']).exists() and
                request.user.username != request.POST['username']): # Проверка занятости введенного username пользователем
            messages.error(request, 'Пользователь с таким именем уже существет')
        if form.is_valid():
            messages.success(request, "Пользователь успешно изменен")
            form.save()
    else:
        form = forms.UserChangeForm(instance=request.user)
    context = {'form': form}
    return render(request, 'app/profile.html', context=context)


@login_required
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('app:login'))


@login_required
def delete_account(request):
    user = request.user
    user.delete()
    messages.success(request, 'Вы удалили свой аккаунт!')
    return redirect('app:login')


def user_page(request, user_id):
    user = User.objects.get(id=user_id)
    return render(request, 'app/user_page.html', context={'user': user})


def index(request):
    return render(request, 'app/base.html')
