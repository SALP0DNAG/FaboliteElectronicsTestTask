from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms
from . import models


class UserLoginForm(AuthenticationForm):
    """
    Модель UserLoginForm представляет собой форму авторизации пользователя.

    Атрибуты:
        username (str): Username пользователя.
        password (str): Пароль пользователя.
    """
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'username-input'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'password-input'}))

    class Meta:
        model = models.User
        fields = ('username', 'password')


class UserRegistrationForm(UserCreationForm):
    """
    Модель UserRegistrationForm представляет собой форму регистрации пользователя.

    Атрибуты:
        username (str): Username пользователя.
        password1 (str): Пароль пользователя.
        password2 (str): Повторение пароля пользователя.
    """
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'username-input'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'password-input'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'password-input'}))

    class Meta:
        model = models.User
        fields = ('username', 'password1', 'password2')


class UserChangeForm(forms.ModelForm):
    """
    Модель UserChangeForm представляет собой форму редактирвоания пользователя.

    Атрибуты:
        username (str): Username пользователя.
        first_name (str): Имя пользователя.
        last_name (str): Фамилия пользователя.
        email (str): Почта пользователя.
        address (str): Адрес пользователя.
        about_me (str): Информация о пользователе.
    """
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'username-input'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'first-name-input'}), required=False)
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'last-name-input'}), required=False)
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'email-input'}), required=False)
    address = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'input-address', 'rows': '2'}), required=False)
    about_me = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'input-address', 'rows': '3'}), required=False)

    class Meta:
        model = models.User
        fields = ('username', 'first_name', 'last_name', 'email', 'address', 'about_me')
