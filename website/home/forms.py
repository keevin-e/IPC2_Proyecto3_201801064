from django import forms

class config_form(forms.Form):
    config_file = forms.CharField()

class consume_form(forms.Form):
    consumo_file = forms.CharField()
    