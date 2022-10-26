from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

from . import views as user_views

urlpatterns = [
    path('', views.home, name="home"),
    path('trending/', views.trending, name="trending"),
    path('newevent/', views.newEvent, name="newevent"),
    path('<int:id>', views.detail_newEvent, name="detailed_newEvent"),
    path('<int:id>/', views.detail_page, name="detailed_page"),
    path('<int:id>', views.trending_detailed_page, name="trending_detailed_page"),
    path("register/", views.register, name="register"),
    
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
]