from django import forms

class RegistroEvento(forms.Form):
    nomedoevento = forms.CharField(label='Evento:')
    local = forms.CharField(label='Local:')