from django import forms
from django.db.models import fields 
from .models import Exibicao, Filme, Sala

class FilmeForm(forms.ModelForm):
    sinopse = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = Filme 
        fields = ('nome', 'ano_lancamento', 'nome_diretor', 'poster_img', 'duracao_min', 'elenco', 'genero', 'sinopse')

    def __init__(self, *args, **kwargs):
        super(FilmeForm, self).__init__(*args, **kwargs)
        self.fields['nome'].widget.attrs.update({'class': 'form-control'}) 
        self.fields['ano_lancamento'].widget.attrs.update({'class': 'form-control'})
        self.fields['nome_diretor'].widget.attrs.update({'class': 'form-control'})
        self.fields['poster_img'].widget.attrs.update({'class': 'form-control'})
        self.fields['duracao_min'].widget.attrs.update({'class': 'form-control'})
        self.fields['elenco'].widget.attrs.update({'class': 'form-control'})
        self.fields['genero'].widget.attrs.update({'class': 'form-control'})
        self.fields['sinopse'].widget.attrs.update({'class': 'form-control'})


class SalaForm(forms.ModelForm):
    class Meta:
        model = Sala 
        fields = ('numero_assentos', 'saida_emergencia')

    def __init__(self, *args, **kwargs):
        super(SalaForm, self).__init__(*args, **kwargs)
        self.fields['numero_assentos'].widget.attrs.update({'class': 'form-control'}) 
        self.fields['saida_emergencia'].widget.attrs.update({'class': 'form-check-input'})

class ExibicaoForm(forms.ModelForm):
    class Meta:
        model = Exibicao
        fields = ('codigo_filme', 'codigo_sala', 'data', 'hora')

    def __init__(self, *args, **kwargs):
        super(ExibicaoForm, self).__init__(*args, **kwargs)
        self.fields['codigo_filme'].widget.attrs.update({'class': 'form-control'}) 
        self.fields['codigo_sala'].widget.attrs.update({'class': 'form-control'}) 
        #self.fields['codigo_administrador'].widget.attrs.update({'class': 'form-control'}) 
        self.fields['data'].widget.attrs.update({'class': 'form-control'}) 
            