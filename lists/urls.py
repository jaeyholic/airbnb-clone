from django.urls import path
from . import views


app_name = "trips"

urlpatterns = [
    path("", views.ListView.as_view(), name="trips"),
]
