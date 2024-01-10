from django.db import models
from django.contrib.auth.models import User

class Room(models.Model):

    name = models.CharField(max_length=250, blank=False, unique=True)
    slug = models.SlugField(max_length=25)

    def __str__(self):
        return self.name


class Message(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content















# from django.db import models
# from django.conf import settings
#
#
# class PublicChatRoom(models.Model):
#
#     title = models.CharField(max_length=250, unique=True, blank=False)
#     online_users = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, help_text='Online users')
#
#     def __str__(self):
#         return self.title
#
#     def connect_user(self, user):
#
#         is_user_added = False
#         if not user in self.online_users.all():
#             self.online_users.add(user)
#             self.save()
#             is_user_added = True
#         elif user in self.online_users.all():
#             is_user_added = True
#         return is_user_added
#
#     def disconnect_user(self, user):
#
#         is_user_removed = False
#         if user in self.online_users.all():
#             self.online_users.remove(user)
#             self.save()
#             is_user_removed = True
#         return is_user_removed
#
#     @property
#     def group_name(self):
#         """
#         Returns the channels group name that sockets should subscribe to and get sent messages as they are generated.
#         """
#         return f"PublicChatRoom-{self.id}"
#
# class PublicRoomChatMessageManager(models.Model):
#     def by_room(self, room):
#         qs = PublicRoomChatMessage.objects.filter(room=room).order_by('-date')
#         return qs
#
# class PublicRoomChatMessage(models.Model):
#
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     room = models.ForeignKey(PublicChatRoom, on_delete=models.CASCADE)
#     date = models.DateTimeField(auto_now_add=True)
#     msg  = models.TextField(unique=False, blank=False)
#
#     objects = PublicRoomChatMessageManager()
#
#     def __str__(self):
#         return self.msg
