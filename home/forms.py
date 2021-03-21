from django import forms

class CountForm(forms.Form):
    count = forms.IntegerField(label='Current stock')

class SearchForm(forms.Form):
    search = forms.CharField()
