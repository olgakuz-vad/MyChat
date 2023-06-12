from django.contrib import admin
from chats.models import UserProfile, ChatModel, Room

admin.site.register(ChatModel)
admin.site.register(UserProfile)
admin.site.register(Room)

