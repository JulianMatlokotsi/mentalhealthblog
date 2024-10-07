from django.urls import path
from .views import post_list, post_detail, post_create
from . import views
from .views import login_view, logout_view

urlpatterns = [
    path('user/<str:username>/', views.user_profile, name='user_profile'),
    path('', post_list, name='post_list'),
    path('post/<int:pk>/', post_detail, name='post_detail'),
    path('post/new/', post_create, name='post_create'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('login/', views.login_view, name='account_login'),
    path('logout/', logout_view, name='account_logout'),
]
