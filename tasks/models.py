from django.db import models
from django.urls import reverse

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    done = models.BooleanField(default=False)
    created_date = models.DateField(auto_now=False, auto_now_add=True)
    updated_date = models.DateField(auto_now=True, auto_now_add=False)
    creator = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    

    def __str__(self) -> str:
        return self.title
    
    def get_absolute_url(self):
        return reverse("tasks:details", kwargs={"pk": self.pk})

    def get_delete_url(self):
        return reverse('tasks:delete',kwargs={'pk':self.pk})
    
    def get_update_url(self):
        return reverse('tasks:update',kwargs={'pk':self.pk})
    
    