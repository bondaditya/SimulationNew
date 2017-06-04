from django import forms 
from .models import Marketing

class SpentForm(forms.ModelForm):
	class Meta:
		model = Marketing
		fields = [
			'offline',
			'online',
			'tv',
			'hr',
			'radio',
			'prints',

		]

