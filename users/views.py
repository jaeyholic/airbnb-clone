import os
import requests
from django.views import View
from django.contrib.auth.views import PasswordChangeView
from django.views.generic import FormView, DetailView, UpdateView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, login, logout
from django.core.files.base import ContentFile
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from . import models, forms, mixins

# Create your views here.
class LoginView(mixins.LoggedInUsers, FormView):
    """LoginView Definition"""

    template_name = "users/login.html"
    form_class = forms.LoginForm

    def form_valid(self, form):
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(self.request, username=username, password=password)
        if user is not None:
            login(self.request, user)
        return super().form_valid(form)

    def get_success_url(self):
        next_arg = self.request.GET.get("next")
        if next_arg is not None:
            return next_arg
        else:
            return reverse("core:home")


def logout_view(request):
    logout(request)
    return redirect(reverse("core:home"))


class RegisterView(mixins.LoggedInUsers, FormView):
    """RegisterView Definition"""

    template_name = "users/register.html"
    form_class = forms.RegisterForm
    success_url = reverse_lazy("core:home")

    def form_valid(self, form):
        form.save()
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(self.request, username=username, password=password)
        if user is not None:
            login(self.request, user)
            user.verify_email()
        return super().form_valid(form)


def complete_verification(request, key):
    try:
        user = models.User.objects.get(email_secret=key)
        user.email_verified = True
        user.email_secret = ""
        user.save()
        # todo: add success message
    except models.User.DoesNotExist:
        # todo: add error message
        pass
    return redirect(reverse("core:home"))


def github_login(request):
    client_id = os.environ.get("GITHUB_ID")
    redirect_uri = "http://127.0.0.1:8000/users/login/github/callback"
    return redirect(
        f"https://github.com/login/oauth/authorize?client_id={client_id}&redirect_uri={redirect_uri}&scope=read:user"
    )


class GitHubException(Exception):
    pass


def github_callback(request):
    try:
        client_id = os.environ.get("GITHUB_ID")
        client_secret = os.environ.get("GITHUB_SECRET")
        code = request.GET.get("code", None)
        if code is not None:
            token_request = requests.post(
                f"https://github.com/login/oauth/access_token?client_id={client_id}&client_secret={client_secret}&code={code}",
                headers={"Accept": "application/json"},
            )
            token_json = token_request.json()
            error = token_json.get("error", None)
            if error is not None:
                raise GitHubException("Can't get access token")
            else:
                access_token = token_json.get("access_token")
                profile_request = requests.get(
                    "https://api.github.com/user",
                    headers={
                        "Authorization": f"token {access_token}",
                        "Accept": "application/json",
                    },
                )
                profile_json = profile_request.json()
                username = profile_json.get("login", None)
                if username is not None:
                    name = profile_json.get("name")
                    email = profile_json.get("email")
                    bio = profile_json.get("bio")
                    avatar = profile_json.get("avatar_url")
                    try:
                        user = models.User.objects.get(email=email)
                        if user.login_method != models.User.LOGIN_GITHUB:
                            raise GitHubException(
                                f"Please log in with: {user.login_method}"
                            )
                    except models.User.DoesNotExist:
                        user = models.User.objects.create(
                            email=email,
                            first_name=name,
                            username=email,
                            bio=bio,
                            login_method=models.User.LOGIN_GITHUB,
                            # email_verified=True,
                        )
                        user.set_unusable_password()
                        user.save()
                        if avatar is not None:
                            avatar_request = request.get(avatar)
                            user.avatar.save(
                                f"{username}-avatar",
                                ContentFile(avatar_request.content()),
                            )
                    login(request, user)
                    messages.success(request, f"Welcome back {user.first_name}")
                    return redirect(reverse("core:home"))
                else:
                    raise GitHubException("Can't get your profile")
        else:
            raise GitHubException("Can't get code")
    except GitHubException:
        messages.error(request)
        return redirect(reverse("users:login"))


class UserProfileView(mixins.Authorization, DetailView):
    model = models.User
    context_object_name = "user_obj"


class UpdateView(mixins.Authorization, SuccessMessageMixin, UpdateView):
    template_name = "users/update-profile.html"
    form_class = forms.UpdateProfileForm
    success_message = "Profile successfully updated"

    def get_object(self, queryset=None):
        return self.request.user


class UpdatePassword(
    mixins.Authorization, mixins.EmailOnly, SuccessMessageMixin, PasswordChangeView
):
    template_name = "users/update-password.html"
    success_message = "Password successfully updated"

    def get_form(self, form_class=None):
        """Return an instance of the form to be used in this view."""
        form = super().get_form(form_class=form_class)
        form.fields["old_password"].widget.attrs = {"placeholder": "Current Password"}
        form.fields["new_password1"].widget.attrs = {"placeholder": "New Password"}
        form.fields["new_password2"].widget.attrs = {"placeholder": "Confirm Password"}
        return form

    def get_success_url(self):
        return self.request.user.get_absolute_url()


class UpdateProfilePhoto(UpdateView):

    template_name = "users/edit-photo.html"
    form_class = forms.UpdateProfilePhotoForm
