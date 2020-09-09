from django.forms import models
from .models import UserModel


class UserForm(models.ModelForm):
    class Meta:
        model = UserModel
        fields = "__all__"