from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User

# Custom UserCreationForm
class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("email",)

# Custom UserChangeForm
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ("email",)
