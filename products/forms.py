from django import forms
from .models import Product


class ProductUploadForm(forms.ModelForm):

    class Meta:
        model = Product

        fields = [
            'product_name',
            'description',
            'price',
            'product_image',
            'seller_name',
            'whatsapp_number',
        ]

        widgets = {
            'product_name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter product name'
                }
            ),

            'description': forms.Textarea(
                attrs={
                    'placeholder': 'Describe your product',
                    'rows': 4
                }
            ),

            'price': forms.NumberInput(
                attrs={
                    'placeholder': 'Enter product price'
                }
            ),

            'seller_name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter your name'
                }
            ),

            'whatsapp_number': forms.TextInput(
                attrs={
                    'placeholder': 'e.g. 2348012345678'
                }
            ),
        }

    def clean_price(self):
        price = self.cleaned_data['price']

        if price <= 0:
            raise forms.ValidationError(
                'Price must be greater than zero.'
            )

        return price