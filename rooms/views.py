from math import ceil
from django.shortcuts import render
from django.core.paginator import Paginator
from . import models

# Create your views here.
def all_rooms(request):
    page = request.GET.get("page")
    room_list = models.Room.objects.all()
    paginator = Paginator(room_list, 15)
    rooms = paginator.get_page(page)
    return render(request, "rooms/home.html", context={"rooms": rooms},)

