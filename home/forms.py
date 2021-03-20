from django import forms

class CountForm(forms.Form):
    count = forms.IntegerField(label='Current stock')