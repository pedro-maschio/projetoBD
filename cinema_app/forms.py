from django import forms
from django.db.models import fields
from .models import Exibicao, Filme, Sala, Artigo, Cinema

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
        self.fields['sinopse'].widget.attrs.update({'class': 'form-control d-block mb-2'})

class SalaForm(forms.ModelForm):
    class Meta:
        model = Sala
        fields = ('numero_assentos', 'codigo_cinema', 'sessao_normal','sessao_3d','sessao_platinum')

    def __init__(self, *args, **kwargs):
        super(SalaForm, self).__init__(*args, **kwargs)
        self.fields['numero_assentos'].widget.attrs.update({'class': 'form-control d-block mb-2'})
        self.fields['codigo_cinema'].widget.attrs.update({'class': 'form-control'})

class ExibicaoForm(forms.ModelForm):
    class Meta:
        model = Exibicao
        fields = ('codigo_filme', 'codigo_sala', 'audio', 'legenda', 'data', 'hora')

    def __init__(self, *args, **kwargs):
        super(ExibicaoForm, self).__init__(*args, **kwargs)
        self.fields['codigo_filme'].widget.attrs.update({'class': 'form-control'})
        self.fields['codigo_sala'].widget.attrs.update({'class': 'form-control'})
        #self.fields['codigo_administrador'].widget.attrs.update({'class': 'form-control'})
        self.fields['audio'].widget.attrs.update({'class': 'form-control'})
        self.fields['legenda'].widget.attrs.update({'class': 'form-control'})
        self.fields['data'].widget.attrs.update({'class': 'form-control d-block'})

        self.fields['hora'].widget.attrs.update({'class': 'form-control d-block mb-2'})

class ArtigoForm(forms.ModelForm):
    class Meta:
        model = Artigo
        fields = ('author','artigo_img', 'titulo', 'texto')

    def __init__(self, *args, **kwargs):
        super(ArtigoForm, self).__init__(*args, **kwargs)
        self.fields['author'].widget.attrs.update({'class': 'form-control'})
        self.fields['artigo_img'].widget.attrs.update({'class': 'form-control'})
        self.fields['titulo'].widget.attrs.update({'class': 'form-control'})
        self.fields['texto'].widget.attrs.update({'class': 'form-control'})

class CinemaForm(forms.ModelForm):
    class Meta:
        model = Cinema
        fields = ('nome','cnpj', 'numero', 'cep','estado','cidade','endereco','codigo_admin')

    def __init__(self, *args, **kwargs):
        super(ArtigoForm, self).__init__(*args, **kwargs)
        self.fields['nome'].widget.attrs.update({'class': 'form-control'})
        self.fields['cnpj'].widget.attrs.update({'class': 'form-control'})
        self.fields['numero'].widget.attrs.update({'class': 'form-control'})
        self.fields['cep'].widget.attrs.update({'class': 'form-control'})
        self.fields['estado'].widget.attrs.update({'class': 'form-control'})
        self.fields['cidade'].widget.attrs.update({'class': 'form-control'})
        self.fields['endereco'].widget.attrs.update({'class': 'form-control'})
        self.fields['codigo_admin'].widget.attrs.update({'class': 'form-control'})
