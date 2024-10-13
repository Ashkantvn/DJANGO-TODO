from django.urls import path
from . import views


app_name = "api-v1"

urlpatterns = [
    path("profile/", views.ProfileAPIView.as_view(), name="profile"),
    path("profile/<str:token>", views.TokenProfileAPIView.as_view(), name="profile-token"),

    # token base authentication
    path("registration/", views.RegistrationAPIView.as_view(), name="register"),
    path("login", views.LoginAPIView.as_view(), name="login"),
    path('logout/<str:token>',views.LogoutAPIView.as_view(),name='logout')
]
