from django.urls import path

from . import views


app_name = 'postss'


urlpatterns = [
    path('', views.post_list_and_create, name='main'),
    path('hello/', views.hello, name='hello'),
]
