from django.urls import path
from . import views

app_name = 'phish'
urlpatterns = [
    path('', views.index, name="index"),
    path('session', views.log, name="log"),
]
