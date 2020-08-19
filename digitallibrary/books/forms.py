from django import forms
from books.models import book

class addnew(forms.ModelForm):
    class Meta:
        model = book
        fields = ['bookname','authorname','booknum','stockavail']

class checkoutb(forms.ModelForm):
    class Meta:
        model = book
        fields = ['booknum','noc']

class SearchForm(forms.ModelForm):
    class Meta:
        model = book
        fields = ['bookname','authorname','booknum']
