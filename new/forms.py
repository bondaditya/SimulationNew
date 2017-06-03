from django import forms
from django.contrib.auth.models import User, Group


from .models import Vendor,Vendor2, Vendor3, Vendor4, Forcast, Product, College

class VendorForm(forms.ModelForm):

    class Meta:
        model = Vendor
        fields = [
            'monthly_order1',
            'start_month1',
            'monthly_order2',
            'start_month2',
            'monthly_order3',
            
            
            'start_month3',
           
]
class VendorForm2(forms.ModelForm):

    class Meta:
        model = Vendor2
        fields = [
            'monthly_order4',
            
            'monthly_order5',
            
            'monthly_order6',
            
            
            
           
]
class VendorForm3(forms.ModelForm):

    class Meta:
        model = Vendor3
        fields = [
            'monthly_order7',
            
            'monthly_order8',
            
            'monthly_order9',
            
            
            
           
]
class VendorForm4(forms.ModelForm):

    class Meta:
        model = Vendor4
        fields = [
            'monthly_order10',
            
            'monthly_order11',
            
            'monthly_order12',
            
            
            
           
]

class ProductForm(forms.ModelForm):
	class Meta:
		model=Product
		fields = [
			'style',
			'storage',
			'extended_battery',
			'durability',
		]

class ForcastForm(forms.ModelForm):
	class Meta:
		model=Forcast
		fields = [
		'forcast',


		]


# class UserProfileForm(forms.ModelForm):
#     group = forms.ModelChoiceField(queryset=Group.objects.all(),
#                                    required=True)
    
#     class Meta:
#         model = User
#         fields = ['first_name', 'last_name', 'email', 'group']


class ProfileForm(forms.ModelForm):
    group = forms.ModelChoiceField(queryset=Group.objects.all(),
                                 required=True)
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'group']


