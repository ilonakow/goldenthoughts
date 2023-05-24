from django.urls import path
from randomthought import views

app_name = 'randomthought'

urlpatterns = [
    path('', views.thought),
    path('create/', views.create_sentence_view, name='create_sentence_view'),
    path('list/', views.list_sentence_view, name='list_sentence_view'),
    ]