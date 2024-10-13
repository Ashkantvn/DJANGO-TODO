from django.urls import path
from .views import ProfileAPIView,RegistrationAPIView


app_name = "api-v1"

urlpatterns = [
    path("profile/", ProfileAPIView.as_view(), name="test"),



    path("registration/", RegistrationAPIView.as_view(), name=""),
]
