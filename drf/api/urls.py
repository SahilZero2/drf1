
from django.contrib import admin
from django.db import router
from django.urls import path , include
from knox import views as knox_views
from rest_framework import routers, views
from api import views
from api.views import RegisterAdvisor , RegisterAPI , LoginAPI , advisorViewSet
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('advisor', views.advisorViewSet , basename='user')
urlpatterns = [
    
    path('register/', RegisterAPI.as_view(), name='register'),
    path('login/', LoginAPI.as_view(), name='login'),
    path('logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('',include(router.urls))
    
]
