from django.contrib import admin
from django.urls import path, include

from . import views
from .views import *

urlpatterns = [
    path('hello/', views.hello, name='hello'),
    path('', views.index, name='home'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('students/', views.students, name='students'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('save/<int:id>/', views.save_student, name='save_student'),
    path('remove-saved/<int:id>/', views.remove_saved, name='remove_saved'),
    path('saved/', views.saved_list, name='saved_list'),
    path('send/<int:target_user_id>/', views.send_requests, name='send_requests'),
    path('request/accept/<int:id>/', views.accept_request, name='accept_request'),
    path('request/reject/<int:id>/', views.reject_request, name='reject_request'),
    path('students/', students, name='students'),
    path('edit/<int:id>/', edit_student, name='edit_student'),
    path('delete/<int:id>/', delete_student, name='delete_student'),
]
