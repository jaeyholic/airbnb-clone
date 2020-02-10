from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.shortcuts import redirect
from django.contrib import messages
from django.urls import reverse_lazy


class LoggedInUsers(UserPassesTestMixin):
    def test_func(self):
        return not self.request.user.is_authenticated

    def handle_no_permission(self):
        messages.error(self.request, "You're not permitted to visit this page")
        return redirect("core:home")


class Authorization(LoginRequiredMixin):
    login_url = reverse_lazy("users:login")


class EmailOnly(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.login_method == "email"

    def handle_no_permission(self):
        messages.error(self.request, "You're not permitted to visit this page")
        return redirect("core:home")
