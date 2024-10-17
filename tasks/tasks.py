from celery import shared_task
from .models import Task


@shared_task
def delete_done_tasks():
    Task.objects.filter(done=True).delete()
