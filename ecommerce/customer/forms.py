from django import forms 
from .models import Customer 
from django.core.exceptions import ValidationError
class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ["firstName","LastName","address","postalCode"]
        widgets = {
                    "firstName": forms.TextInput(
                            attrs={
                                "placeholder": "First name of customer",
                                'class': 'form-control',
                            }),
                    "LastName": forms.TextInput(
                        attrs={
                            "placeholder":"Lastname of customer",
                            'class': 'form-control',
                            }),
                    "address": forms.TextInput(
                        attrs={
                            "placeholder":"address of customer",
                            'class': 'form-control',
                            }),
                    "postalCode": forms.NumberInput(
                        attrs={
                            "placeholder":"postalCode of customer",
                            'class': 'form-control' 

                            })
                
                }
    def clean_address(self):
        value = self.cleaned_data["address"]
        if value < 12:
            raise forms.ValidationError("your value is lower than 12")
        return value

    def clean_firstName(self):
        value = self.cleaned_data['firstName'] ## cleaned_data is only available after form.is_valid() is called 
        if value.lower() != value:
            raise ValidationError("{} is not lowercase.".format(value))
        return value

    def clean_LastName(self):
        value = self.cleaned_data['LastName']
        return value.lower()