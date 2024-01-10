from django.shortcuts import render
from .models import Room, Message


def rooms(request):

    context = {}
    all_rooms = Room.objects.all()
    context['rooms'] = all_rooms
    return render(request, 'rooms.html', context)


def room(request, slug):
    room_name = Room.objects.get(slug=slug).name
    room_ = Room.objects.get(slug=slug)
    messages = Message.objects.filter(room=room_)
    context = {'slug': slug, 'room_name': room_name, 'messages': messages}
    return render(request, 'room.html', context)
