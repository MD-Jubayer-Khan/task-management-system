from django.db import models
from categoryApp.models import Category

# Create your models here.
class Task(models.Model):
    taskTitle = models.CharField(max_length=100)
    taskDesc = models.TextField()
    is_completed = models.BooleanField(default=False)
    taskAssignDate = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField(Category)

    def __str__(self) -> str:
        return self.taskTitle
