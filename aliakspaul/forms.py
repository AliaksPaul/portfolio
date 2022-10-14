from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'contact__input', 'placeholder': 'Name'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'contact__input', 'placeholder': 'Email'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'contact__input',  'placeholder': '...'}))