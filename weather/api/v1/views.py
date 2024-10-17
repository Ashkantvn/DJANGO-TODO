# views.py
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
import requests
from django.http import JsonResponse
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class WeatherAPIView(APIView):
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                "lat",
                openapi.IN_QUERY,
                description="Latitude",
                type=openapi.TYPE_STRING,
            ),
            openapi.Parameter(
                "lon",
                openapi.IN_QUERY,
                description="Longitude",
                type=openapi.TYPE_STRING,
            ),
        ]
    )
    @method_decorator(cache_page(60 * 20))
    def get(self, request, *args, **kwargs):
        lat = request.GET.get("lat")
        lon = request.GET.get("lon")

        if not lat or not lon:
            return JsonResponse(
                {"error": "Latitude and longitude are required."},
                status=400
            )

        try:
            response = requests.get(
                f"https://api.brightsky.dev/current_weather?lat={lat}&lon={lon}"
            )
            response.raise_for_status()
            weather_data = response.json()
        except requests.exceptions.RequestException as e:
            return JsonResponse(
                {"error": f"Unable to fetch weather data: {e}"},
                status=500
            )

        return JsonResponse(weather_data)
