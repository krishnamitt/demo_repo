from django.urls import path
from .views import LoginTokenAPI, ProfileTokenAPI, AboutTokenAPI

urlpatterns = [
    path('login/', LoginTokenAPI.as_view()),
    path('profile/', ProfileTokenAPI.as_view()),
    path('about/', AboutTokenAPI.as_view()),   
]
