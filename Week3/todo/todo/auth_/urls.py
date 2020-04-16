from django.urls import path

from todo.auth_.views import login, logout, register

urlpatterns = [
    path('login/', login),
    path('logout/', logout),
    path('register/', register),
]