from django import forms
from . import models


class LoginForm(forms.Form):
    """LoginView Definition"""

    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        try:
            user = models.User.objects.get(username=username)
            if user.check_password(password):
                return self.cleaned_data
            else:
                self.add_error("password", forms.ValidationError("Password is wrong"))
        except models.User.DoesNotExist:
            self.add_error("username", forms.ValidationError("User does not exist!"))


class RegisterForm(forms.ModelForm):
    """RegisterForm Definition"""

    class Meta:
        model = models.User
        fields = [
            "first_name",
            "last_name",
            "username",
            "email",
        ]

    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(
        widget=forms.PasswordInput, label="Confirm Password"
    )

    def clean_confirm_password(self):
        password = self.cleaned_data.get("password")
        confirm_password = self.cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match!")
        else:
            return password

    def save(self, *args, **kwargs):
        user = super().save(commit=False)  # Call the real save() method
        password = self.cleaned_data.get("password")
        user.set_password(password)
        user.save()

