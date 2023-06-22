from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

from .views import *

urlpatterns = [
    path("", views.frontpage, name="frontpage"),
    path('signup/', views.signup, name='signup'),
    #path('author_profile/', views.author_prof, name='author_profile'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('addroom/', addroom, name="add_room"),
    path('rooms/', views.rooms, name="rooms"),
    path('<slug:slug>/', views.room, name='room'),


]