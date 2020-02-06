from django.views.generic import ListView, DetailView
from django.shortcuts import render
from . import models

# Create your views here.
class HomeView(ListView):
    """Homeview Definition"""

    model = models.Room
    paginate_by = 15
    ordering = "created"


class RoomDetail(DetailView):
    """RoomDetail Definition"""

    model = models.Room


class search(request):
    pass


# def room_detail(request, pk):
#     try:
#         room = models.Room.objects.get(pk=pk)
#         return render(request, "rooms/detail.html", {"room": room})
#     except models.Room.DoesNotExist:
#         raise Http404()


# def all_rooms(request):
#     page = request.GET.get("page")
#     room_list = models.Room.objects.all()
#     paginator = Paginator(room_list, 15)
#     rooms = paginator.get_page(page)
#     return render(request, "rooms/home.html", context={"page": rooms},)

