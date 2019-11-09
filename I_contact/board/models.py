from django.db import models
from login.models import Profile
from django.contrib.auth.models import User

# Create your models here.

class Board(models.Model):
    title = models.CharField(max_length = 200)
    date = models.DateTimeField('date published')
    writer = models.CharField(max_length= 200)
    body = models.TextField()
    user = models.ManyToManyField(User, blank=True, related_name='user')

    def __str__(self):
         return self.title
    
    @property
    def total_likes(self):
        return self.user.count()

class Comments(models.Model):
    writer = models.ForeignKey(Profile, on_delete = models.CASCADE)
    content = models.TextField()
    post = models.ForeignKey(Board, on_delete = models.CASCADE)

