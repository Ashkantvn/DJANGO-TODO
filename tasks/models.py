from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    done = models.BooleanField()
    created_date = models.DateField(auto_now=False, auto_now_add=True)
    updated_date = models.DateField(auto_now=True, auto_now_add=False)
    creator = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    

    def __str__(self) -> str:
        return self.title
    