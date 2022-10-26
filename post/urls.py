from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('trending/', views.trending, name="trending"),
    path('<str:id>/', views.detail_page, name="detailed_page"),
    path('<str:id>', views.trending_detailed_page, name="trending_detailed_page")
]