from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from core.user.models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("email",)


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ("email",)