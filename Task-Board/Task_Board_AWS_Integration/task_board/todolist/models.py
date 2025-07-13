from django.db import models

# Create your models here.

class Status(models.TextChoices):
    New = "New"
    InProgress = "In Progress"
    Done = "Done"

class Todolist(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    status = models.CharField(max_length=45, choices=Status.choices, default="New")

    def __str__(self):
        return self.name