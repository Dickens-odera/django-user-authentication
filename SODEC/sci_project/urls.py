from django.urls import path, include
from django.conf.urls import url
from . import views
urlpatterns = [
    path('',views.index, name='index' ),
    path("register/", views.register, name='register'),
    path('home/', views.home, name = 'home'),
]