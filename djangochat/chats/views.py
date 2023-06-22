from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import FormMixin
from django.urls import reverse_lazy
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.contrib.auth import get_user_model

from .models import *
from .forms import *

menuRooms = [{'title': 'Добавить груповой чат', 'url_name': 'add_room'},]

def frontpage(request):
    return render(request, 'frontpage.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)

            return redirect('frontpage')
    else:
        form = SignUpForm()

    return render(request, 'signup.html', {'form': form})

def addroom(request):
    if request.method =='POST':
        form = AddRoomForm(request.POST)
        if form.is_valid():
            #print(form.cleaned_data)
            try:
                Room.objects.create(**form.cleaned_data)
                return redirect('rooms')
            except:
                form.add_error(None, "Oшибка добавления чата")
    else:
         form = AddRoomForm()
    return render(request, 'room/addroom.html', {'form': form, 'title': "Добавить групповой чат"})

@login_required
def rooms(request):
    rooms = Room.objects.all()

    return render(request, 'room/rooms.html', {'menuRooms': menuRooms, 'rooms': rooms})

def addmessage(request):
    return render(request, 'room/addmessage.html', {'title': "Добавить cообщения"})


@login_required
def room(request, slug):
    room = Room.objects.get(slug=slug)
    messages = ChatModel.objects.filter(room=room)[0:25]

    context = {
        'messages': messages,
        'room': room,
    }
    return render(request, 'room/room.html', context=context)


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Старница не найдена </h1>')

