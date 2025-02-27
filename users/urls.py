from django.urls import path
from . import views

app_name = 'users'  # This sets the application namespace

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('personal-center/', views.personal_center, name='personal_center'),
]
