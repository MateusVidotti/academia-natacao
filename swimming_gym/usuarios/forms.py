from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from usuarios.models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = [
            'empresa',
            'email',
            'nome',
            'is_admin',
            'is_comum',
        ]

    def __init__(self, request, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        if not request.user.is_staff:
            del self.fields['empresa']


class EditCustomUserCreationForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = [
            'email',
            'nome',
            'is_admin',
            'is_comum',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        del self.fields['password']


class EditPasswordCustomUserForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = [
            'password'
        ]
