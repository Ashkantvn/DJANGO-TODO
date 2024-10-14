from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

app_name = "api-v1"

urlpatterns = [
    path("profile/", views.ProfileAPIView.as_view(), name="profile"),
    # token base authentication
    path(
        "token/profile/<str:token>",
        views.TokenProfileAPIView.as_view(),
        name="profile-token",
    ),
    path(
        "token/registration/",
        views.RegistrationAPIView.as_view(),
        name="register"),
    path("token/login", views.LoginAPIView.as_view(), name="login"),
    path(
        "token/logout/<str:token>",
        views.LogoutAPIView.as_view(),
        name="logout"),
    # jwt authentication
    path(
        "jwt/profile/<str:token>",
        views.JwtProfileAPIView.as_view(),
        name="profile-jwt-token",
    ),
    path("jwt/login", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("jwt/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("jwt/verify/",
         TokenVerifyView.as_view(),
         name="token_verify"),
    path(
        "jwt/registration/",
        views.JwtRegistrationAPIView.as_view(),
        name="jwt-register"
    ),
]
