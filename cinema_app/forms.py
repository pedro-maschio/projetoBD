from django import forms
from django.db.models import fields 
from .models import Filme 

class FilmeForm(forms.ModelForm):
    class Meta:
        model = Filme 
        fields = ('nome', 'ano_lancamento', 'nome_diretor', 'audio', 'legenda', 'poster_img', 'duracao_min', 'elenco', 'genero', 'sinopse')#completar o resto depois

    def __init__(self, *args, **kwargs):
        super(FilmeForm, self).__init__(*args, **kwargs)
        self.fields['nome'].widget.attrs.update({'class': 'form-control'}) 
        self.fields['ano_lancamento'].widget.attrs.update({'class': 'form-control'})
        self.fields['nome_diretor'].widget.attrs.update({'class': 'form-control'})
        self.fields['audio'].widget.attrs.update({'class': 'form-control'})
        self.fields['legenda'].widget.attrs.update({'class': 'form-control'})
        self.fields['poster_img'].widget.attrs.update({'class': 'form-control'})
        self.fields['duracao_min'].widget.attrs.update({'class': 'form-control'})
        self.fields['elenco'].widget.attrs.update({'class': 'form-control'})
        self.fields['genero'].widget.attrs.update({'class': 'form-control'})
        self.fields['sinopse'].widget.attrs.update({'class': 'form-control'})