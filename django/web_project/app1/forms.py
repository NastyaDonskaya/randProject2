from django import forms
from django.forms.fields import ImageField


from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

'''

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ['name', 'lastname', 'email', 'password']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input'}),
            'lastname': forms.TextInput(attrs={'class': 'form-input'}),
            'email': forms.Textarea(attrs={'cols': 60, 'rows': 10}),
            'password': forms.TextInput(attrs={'class': 'form-input'}),
            #'theme': forms.TextInput(attrs={'cols': 60, 'rows': 10}),
            #'time': forms.TextInput(attrs={'class': 'form-input'}),
        }


'''


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class RandNum(forms.Form):
    leftNum = forms.IntegerField()
    rightNum = forms.IntegerField()
    countNum = forms.IntegerField()
