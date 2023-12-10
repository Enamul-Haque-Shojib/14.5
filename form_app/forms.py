from django import forms 
from django.core import validators
from django.forms.widgets import NumberInput
import datetime

class contactForm(forms.Form):
	name = forms.CharField()
	email = forms.EmailField()
	comment = forms.CharField(widget=forms.Textarea(attrs={'rows':3}))
	agree = forms.BooleanField()
	date = forms.DateField()
	birth_date = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))
	birth_year = forms.DateField(widget=forms.SelectDateWidget(years=['1980', '1981', '1982']))
	value = forms.DecimalField()
	day = forms.DateField(initial=datetime.date.today)
	favorite_color = forms.ChoiceField(choices=[
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),])
	favorite_color = forms.ChoiceField(widget=forms.RadioSelect, choices=[
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),])
	favorite_colors = forms.MultipleChoiceField(choices=[
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),])
	favorite_colors = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=[
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),])