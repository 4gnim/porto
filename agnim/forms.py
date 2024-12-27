from django import forms
from .models import ContactForm

class FormContact(forms.ModelForm):
    class Meta:
        model = ContactForm
        fields = ['name', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Name', 'class': 'contact__input'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email', 'class': 'contact__input'}),
            'message': forms.Textarea(attrs={
                'placeholder': 'Your message...',
                'class': 'contact__input',
                'rows': 10,
                'cols': 0,
            }),
        }
