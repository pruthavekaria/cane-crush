from django import forms
from .models import ContactMessage

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['fname', 'lname', 'email','message']
    # fname = forms.CharField(max_length=100)
    # lname = forms.CharField(max_length=100)
    # email = forms.EmailField()
    # message = forms.CharField(widget=forms.Textarea)
