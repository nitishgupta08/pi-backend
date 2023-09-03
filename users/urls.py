from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import RegisterUserView, ProfileView

urlpatterns = [
    path("login/", TokenObtainPairView.as_view(), name="login_obtain_pair"),
    path("login/refresh/", TokenRefreshView.as_view(), name="login_refresh"),
    path("register/", RegisterUserView.as_view(), name="register_user"),
    path("profile/<str:username>", ProfileView.as_view(), name="user_profile"),
]
