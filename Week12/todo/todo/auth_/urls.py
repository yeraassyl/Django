from django.urls import path

from rest_framework_jwt.views import obtain_jwt_token
from todo.auth_.views import login, logout, register

# urlpatterns = [
#     path('login/', login),
#     path('logout/', logout),
#     path('register/', register),
#
# ]

urlpatterns = [
    path('login/', obtain_jwt_token),
    path('logout/', logout),
    path('register/', register),
]