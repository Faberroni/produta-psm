#formulir kirim email
from django import forms

class ContactForm(forms.Form):
    from_email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class':'form-control',
        'placeholder':'Masukkan email anda',
        },
        ),
        required=True)
    subject = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Masukkan subjek pesan'
        }
        ),
        required=True, 
        max_length=100)
    message = forms.CharField(widget=forms.Textarea(attrs={
        'class':'form-control',
        'placeholder':'Masukkan pesan yang ingin disampaikan!'
        }
        ),
        required=True)