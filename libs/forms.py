from django import forms
from .models import Library, Book, BookTags
from django.contrib.auth.models import User

class LibraryForm(forms.ModelForm):
    class Meta:
        model = Library
        fields = ['name']

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author']

class TagForm(forms.ModelForm):
    class Meta:
        model = BookTags
        fields = ['tagname']

class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)