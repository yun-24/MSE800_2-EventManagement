from django.urls import path
from . import views

app_name = 'events'  # This sets the application namespace

urlpatterns = [
    path('', views.event_list, name='event_list'),
    path('event/<int:pk>/', views.event_detail, name='event_detail'),
    path('event/new/', views.create_event, name='create_event'),
    path('<int:pk>/edit/', views.edit_event, name='edit_event'),
    path('personal-center/', views.personal_center, name='personal_center'),
]
