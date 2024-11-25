from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

#django form
class ContactForm(forms.Form):
    name = forms.CharField(label='Your Name', max_length=100)
    email = forms.EmailField(label='Enter email')
    msg = forms.CharField(label='your message', widget=forms.Textarea)

#model form
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'age', 'place', 'course']

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2']

class UserloginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'passowrd']

class ItemForm(forms.ModelForm):
    class Meta:
        model = Items
        fields = ['name', 'price', 'desription']

