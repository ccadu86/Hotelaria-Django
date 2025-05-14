from django import forms
from .models import quarto

class quartoForms(forms.ModelForm):
    class Meta:
        model = quarto
        fields = ['num_Quarto','qtd_Hospedes','tipo','valor','descricao','status', 'img']