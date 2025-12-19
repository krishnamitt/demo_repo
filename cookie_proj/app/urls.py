from django.urls import path
from .views import login_view, profile,about,logout_view

urlpatterns = [
    path('', login_view, name='login'),
    path('profile/', profile, name='profile'),
     path('about/', about, name='about'),
    path('logout/', logout_view, name='logout'),
]
