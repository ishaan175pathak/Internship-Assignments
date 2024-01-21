from django.db import models
from django.db.models import Model
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.

class Votes(models.Model):
    username = models.CharField(max_length = 100, blank = False)
    vote = models.CharField(max_length = 100, blank = False)
    datetime = models.DateTimeField(default = datetime.now())

    def __str__(self) -> str:
        return f"User name - {self.username} | Vote to - {self.vote} | Voted on - {self.datetime}"