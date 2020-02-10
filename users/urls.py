from django.urls import path
from . import views

app_name = "login"

urlpatterns = [
    path("login/", views.LoginView.as_view(), name="login"),
    path("login/github/", views.github_login, name="github"),
    path("login/github/callback/", views.github_callback, name="github-callback/"),
    path("logout/", views.logout_view, name="logout"),
    path("register/", views.RegisterView.as_view(), name="register"),
    path(
        "verify/<str:key>", views.complete_verification, name="complete-verification/"
    ),
    path("update-profile/", views.UpdateView.as_view(), name="update"),
    path("update-password/", views.UpdatePassword.as_view(), name="password"),
    path("edit-photo/", views.UpdateProfilePhoto.as_view(), name="photo"),
    path("<int:pk>/", views.UserProfileView.as_view(), name="profile"),
]
