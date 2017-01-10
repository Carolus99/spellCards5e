from django import forms
from.models import Spell

class SpellForm(forms.ModelForm):
    class Meta:
        model = Spell
        fields = ['name','level','distance', 'school', 'image']

class LoginForm(forms.Form):
    username = forms.CharField(label='User Name', max_length=64)
    password = forms.CharField(widget=forms.PasswordInput())
