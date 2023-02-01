from django import forms
from .models import Product
from django.core.exceptions import ValidationError

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["name","description","unitPrice","discount"]
        # exclude = 
        # widgets = 
        widgets = {
                    "name": forms.TextInput(
                            attrs={
                                "placeholder": "First name of product",
                                'class': 'form-control',
                            }),
                    "description": forms.TextInput(
                        attrs={
                            "placeholder":"description of product",
                            'class': 'form-control',
                            }),
                    "unitPrice": forms.NumberInput(
                        attrs={
                            "placeholder":"unitPrice of product",
                            'class': 'form-control',
                            }),
                    "discount": forms.NumberInput(
                        attrs={
                            "placeholder":"discount of product",
                            'class': 'form-control' 

                            })
                
                }
    def clean_name(self):
        value = self.cleaned_data["name"]
        if value == "":
            raise ValidationError("this field cann't be empty")
        if "$!@#%^&*()+=-" in value:
            raise ValidationError("no specila caracter is supported for this field")
        return value
    def clean_description(self):
        value = self.cleaned_data["description"]
        if value == "":
            raise ValidationError("this field cann't be empty")
        if "$!@#%^&*()+=-" in value:
            raise ValidationError("no specila caracter is supported for this field")
        return value

    def clean_unitPrice(self):
        value = self.cleaned_data["unitPrice"]
        if value <=0:
            raise ValidationError("too low")
        return value

    def clean_discount(self):
        value = self.cleaned_data["discount"]
        print(value)
        if value < 1:
            raise ValidationError("too low")
        return value    
