from django import forms


from .models import Vendor, Demand, DemandForcast

class VendorForm(forms.ModelForm):
    # order   = forms.IntegerField(widget=forms.TextInput())
    class Meta:
        model = Vendor
        fields = [
            'monthly_order'
]

class DemandForm(forms.ModelForm):
	class Meta:
		model=Demand 
		fields = [
			'new_style',
			'new_flavour',
			'discount',
			'marketing',
		]

class ForcastForm(forms.ModelForm):
	class Meta:
		model=DemandForcast
		fields = [
		'demand_forcast'

		]
		

