from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

app_name = "api-v1"

urlpatterns = [
    path("profile/", views.ProfileAPIView.as_view(), name="profile"),

    # token base authentication
    path("profile/<str:token>", views.TokenProfileAPIView.as_view(), name="profile-token"),
    path("registration/", views.RegistrationAPIView.as_view(), name="register"),
    path("login", views.LoginAPIView.as_view(), name="login"),
    path('logout/<str:token>',views.LogoutAPIView.as_view(),name='logout'),



    #jwt authentication
    path("profile/jwt/<str:token>", views.JwtProfileAPIView.as_view(), name="profile-jwt-token"),
    path('jwt/login', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('jwt/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('jwt/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
