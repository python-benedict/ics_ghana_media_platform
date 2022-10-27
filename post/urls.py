from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import profile, edit_profile
from . import views as user_views

from django.contrib.auth.views import (
    PasswordChangeView,
    PasswordChangeDoneView
)
from django.urls import reverse_lazy

urlpatterns = [
    path('', views.home, name="home"),
    path('trending/', views.trending, name="trending"),
    path('newevent/', views.newEvent, name="newevent"),
    path('internationalnews/', views.internationalnews, name="internationalnews"),
    path('technologicalnews/', views.technologicalnews, name="technologicalnews"),
    path('newEvent/<int:id>', views.detail_newEvent, name="detailed_newEvent"),
    path('detail/<int:id>/', views.detail_page, name="detailed_page"),
    path('trendings/<int:id>/', views.trending_detailed_page, name="trending_detailed_page"),
    path('internationalnewsDetail/<int:id>/', views.InternationNewsDetailedPage, name="internationalnewsDetail"),
    path('technologicalNewsDetailPage/<int:id>/', views.technologicalNewsDetailPage, name="technologicalNewsDetailPage"),
    path("register/", views.register, name="register"),
    
    
    path('edit-profile/', edit_profile, name='edit_profile'),
    path('profile/<username>/', profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    
    path('password_change/', PasswordChangeView.as_view(template_name='password_change.html',success_url=reverse_lazy('password_change_done')),name='password_change'),
    path('password_change/done/', PasswordChangeDoneView.as_view(template_name='password_change_done.html'),name='password_change_done'),

]