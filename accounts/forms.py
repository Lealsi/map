from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm

from pathlib import os

class RegistrationForm(UserCreationForm):

    def valida_convite(value):
        if str(os.getenv('CONVITE')) != value:
            raise ValidationError("Código de convite inválido")

    convite = forms.CharField(max_length=30, required=True, validators=[valida_convite])


