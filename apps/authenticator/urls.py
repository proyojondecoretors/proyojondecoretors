from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='alogin'),
    path('login/next', views.index, name='lnext'),
]