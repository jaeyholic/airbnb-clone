from django.urls import path
from . import views

app_name = "login"

urlpatterns = [
    path("login", views.LoginView.as_view(), name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.RegisterView.as_view(), name="register"),
    path("verify/<str:key>", views.complete_verification, name="complete-verification"),
]
