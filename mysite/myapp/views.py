from django.shortcuts import render
## Create your views here.
from . import models
from . import forms

def home(request):
    context = {
        "body":"CINS465 Hello World",
    }
    return render(request, "home.html", context=context)

def chatSupport(request):
    context = {
        "body":"finger butt",
        "title":"Hello",
    }
    return render(request, "chatSupport.html", context=context)

def store(request):
    context = {
        "body":"finger butt",
        "title":"Hello",
    }
    return render(request, "store.html", context=context)

def itemDescription(request):
    context = {
        "body":"finger butt",
        "title":"Hello",
    }
    return render(request, "itemDescription.html", context=context)

def shoppingCart(request):
    context = {
        "body":"finger butt",
        "title":"Hello",
    }
    return render(request, "shoppingCart.html", context=context)

def login(request):
    context = {
        "body":"finger butt",
        "title":"Hello",
    }
    return render(request, "login.html", context=context)
        #return HttpResponse("CINS465 Hello World")
def chat_room(request, label):
    room, created = Room.objects.get_or_create(label=label)
    messages = reversed(room.messages.order_by('-timestamp')[:50])
    return render(request, "chat/room.html", {
        'room': room,
        'messages': messages,
    })
