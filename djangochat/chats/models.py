from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image


class UserProfile(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, blank=True, null=True)
    avatar = models.ImageField(max_length=None, upload_to='avatars', null=True, blank=True)

    def __str__(self):
        return self.user.username


class Room(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class ChatModel(models.Model):
    sender = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    message = models.TextField(null=True, blank=True)
    room = models.ForeignKey(Room, related_name='messages', on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('sender','date_added', )

    def __str__(self):
        return self.message

    def get_absolute_url(self):
        return reverse('chat', kwargs={'chat_id':self.pk})









