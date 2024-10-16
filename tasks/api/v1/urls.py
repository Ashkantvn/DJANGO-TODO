from rest_framework.routers import DefaultRouter
from .views import TaskViewSet

app_name = "api-v1"


router = DefaultRouter()
router.register("", TaskViewSet, basename="tasks")
urlpatterns = router.urls
