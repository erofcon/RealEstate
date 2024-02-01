from django import forms

from .models import Feedback


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'contacts', 'subject']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'contacts': forms.Textarea(
                attrs={'class': 'form-control', 'placeholder': 'номер телефона, почта, WhatsApp или Telegram'}),
            'subject': forms.Textarea(attrs={'class': 'form-control'}),
        }
