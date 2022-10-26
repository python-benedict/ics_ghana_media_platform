from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('<str:id>', views.detail_page, name="detailed_page"),
]