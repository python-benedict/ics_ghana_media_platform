from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('trending/', views.trending, name="trending"),
    path('newevent/', views.newEvent, name="newevent"),
    path('<str:id>', views.detail_newEvent, name="detailed_newEvent"),
    path('<str:id>/', views.detail_page, name="detailed_page"),
    path('<str:id>', views.trending_detailed_page, name="trending_detailed_page"),
]