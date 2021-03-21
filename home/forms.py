from django import forms

class CountForm(forms.Form):
    count = forms.IntegerField(label='Current stock')

class SearchForm(forms.Form):
    searchField = forms.CharField()

class AddForm(forms.Form):
    count = forms.IntegerField(label='How many books to add')
