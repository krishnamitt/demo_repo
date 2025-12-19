from django.urls import path
from .views import LoginAPI, ProfileAPI,AboutAPI

urlpatterns = [
    path('login/', LoginAPI.as_view()),
    path('profile/', ProfileAPI.as_view()),
    path('about/', AboutAPI.as_view())
]
