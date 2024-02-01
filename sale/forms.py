from django import forms

from .models import ExternalApartments
from catalog.models import Images


class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True


class ExternalApartmentsFormModel(forms.ModelForm):
    class Meta:
        model = ExternalApartments
        fields = (
            'type', 'address', 'floor', 'bedrooms', 'sqft_living', 'wall_material', 'title', 'description', 'price',
            'contacts', 'plan')

        widgets = {
            'type': forms.RadioSelect(attrs={'class': 'form-check-input'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'floor': forms.NumberInput(attrs={'class': 'form-control'}),
            'bedrooms': forms.NumberInput(attrs={'class': 'form-control'}),
            'sqft_living': forms.NumberInput(attrs={'class': 'form-control'}),
            'wall_material': forms.TextInput(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'contacts': forms.Textarea(
                attrs={'class': 'form-control', 'placeholder': 'номер телефона, почта, WhatsApp или Telegram'}),

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
