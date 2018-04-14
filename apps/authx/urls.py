from django.urls import path
from django.contrib.auth import views as auth_views
from apps.authx import views

app_name = 'auth'
urlpatterns = [
    path('register', views.register, name='register'),
    path('login', auth_views.login, {'template_name': 'authx/login.html'}, name='login'),
    path('logout', auth_views.logout, {'next_page': '/'}, name='logout'),
]
