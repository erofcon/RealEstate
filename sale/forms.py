from django import forms

from catalog.models import Apartments
from catalog.models import Images


class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True


class ExternalApartmentsFormModel(forms.ModelForm):
    class Meta:
        model = Apartments
        fields = (
            'type', 'address', 'floor', 'bedrooms', 'sqft_living', 'wall_material', 'title', 'description', 'price',
            'contacts', 'plan')

        widgets = {
            'type': forms.RadioSelect(attrs={'class': 'form-check-input', 'required': True}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'floor': forms.NumberInput(attrs={'class': 'form-control', 'required': True}),
            'bedrooms': forms.NumberInput(attrs={'class': 'form-control', 'required': True}),
            'sqft_living': forms.NumberInput(attrs={'class': 'form-control', 'required': True}),
            'wall_material': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'title': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'required': True}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'required': True}),
            'contacts': forms.Textarea(
                attrs={'class': 'form-control', 'placeholder': 'номер телефона, почта, WhatsApp или Telegram',
                       'required': True}, ),

        }

    def save(self, commit=True):
        instance = super(ExternalApartmentsFormModel, self).save(commit=False)
        instance.external = True

        if commit:
            instance.save()

        return instance


class ExternalApartmentsImagesForm(forms.ModelForm):
    class Meta:
        model = Images
        fields = {'apartment', 'image'}
        widgets = {
            'image': MultipleFileInput()
        }
