from django.urls import path, include
from randomthought import views

urlpatterns = [
    path('', views.thought),
    ]