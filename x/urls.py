from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("2FA/", views.twoFA, name="2FA"),
]
