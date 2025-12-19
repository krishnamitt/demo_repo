from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from .views import StudentViewSet
from . import defaultview,drfview
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from .views import ProfileView

router = DefaultRouter()
router.register(r'students', StudentViewSet)

urlpatterns = [
    path('hello/', views.hello),   # default route
    path('echo/', views.echo),   # default route
    path('update/', views.update_echo),     # PUT
    path('delete/', views.delete_echo),     # DELETE
    path('cbv-post/', views.SimplePostView.as_view()),
    path('drf-post/', views.UserAPI.as_view()),
    path('', include(router.urls)),
    path('simple-products/', views.simple_page),
    path('newstudents/',views.student_api),
    path("login/", defaultview.login_page),
    path("home/", defaultview.home),
    path("drfview/",drfview.ProfileAPI.as_view()),
    path("api-token-auth/", obtain_auth_token),
    path("jwt/login/", TokenObtainPairView.as_view()),
    path("jwt/refresh/", TokenRefreshView.as_view()),
    path('<str:version>/profile/', ProfileView.as_view(), name='profile')

]
