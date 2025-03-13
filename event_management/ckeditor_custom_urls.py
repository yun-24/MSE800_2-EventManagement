from django.urls import path
from django.contrib.auth.decorators import login_required
from ckeditor_uploader import views as ckeditor_views

urlpatterns = [
    path('upload/', login_required(ckeditor_views.upload), name='ckeditor_upload'),
    path('browse/', login_required(ckeditor_views.browse), name='ckeditor_browse'),
]
