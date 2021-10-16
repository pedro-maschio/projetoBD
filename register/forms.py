from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    # cpf = forms.CharField(max_length=15)
    # data_nascimento = forms.DateTimeField()
    # sexos = [('Masc', 'Masculino'),('Fem','Feminino')]
    # sexo = forms.ChoiceField(choices = sexos, widget=forms.RadioSelect)
    # vacinado = forms.BooleanField()
    class Meta:
        model = User
        # fields = ["username","email","password1", "password2", "cpf","data_nascimento","sexo","vacinado"]
        fields = ["username","email","password1", "password2"]
