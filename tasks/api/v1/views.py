from rest_framework import viewsets,permissions
from ...models import Task
from .serializer import TaskSerializer
from .permissions import IsOwner

class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated,IsOwner]


    def get_queryset(self):
        return Task.objects.filter(creator=self.request.user)

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)
        return super().perform_create(serializer)