from django import forms


class SearchForm(forms.Form):
    keywords = forms.CharField(label='Keywords', max_length=100)
