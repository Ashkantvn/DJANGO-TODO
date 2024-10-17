from django.urls import path
from .views import WeatherAPIView


app_name = "api-v1"

urlpatterns = [path("", WeatherAPIView.as_view(), name="get-data")]
