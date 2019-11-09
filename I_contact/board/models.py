from django.db import models
from login.models import Profile

# Create your models here.

class Board(models.Model):
    title = models.CharField(max_length = 200)
    date = models.DateTimeField('date published')
    writer = models.CharField(max_length= 200)
    body = models.TextField()

    def __str__(self):
         return self.title

class Comments(models.Model):
    writer = models.ForeignKey(Profile, on_delete = models.CASCADE)
    content = models.TextField()
    post = models.ForeignKey(Board, on_delete = models.CASCADE)

