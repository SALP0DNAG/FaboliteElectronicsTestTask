from django.urls import path
from . import views


app_name = 'app'
urlpatterns = [
    path('', views.index),  # Главная страница
    path('login/', views.login, name='login'),  # Страница авторизации
    path('register/', views.register, name='register'),  # Страница регистрации
    path('logout/', views.logout, name='logout'),  # Страница выхода из профиля
    path('list_users/', views.list_users, name='list_users'),  # Страница списка всех пользователей
    path('profile/', views.profile, name='profile'),  # Страница профиля
    path('delete_account/', views.delete_account, name='delete_account'),  # Маршрут удаления пользователя
    path('user_page/<int:user_id>/', views.user_page, name='user_page')  # Страница пользователя
]
