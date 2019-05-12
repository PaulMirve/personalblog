from django.urls import path
from django.contrib.auth import views as vistas
from aboutme import views

app_name = 'aboutme'

urlpatterns = [
    path('aboutme/', views.AboutMeView.as_view(), name="aboutme"),
]