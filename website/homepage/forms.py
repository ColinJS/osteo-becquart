# sendemail/forms.py
from django import forms


class ContactForm(forms.Form):
    from_email = forms.EmailField(label='De:', required=True)
    subject = forms.CharField(label='Objet:', required=True)
    message = forms.CharField(label="Message:", widget=forms.Textarea(attrs={'class': 'message'}), required=True)

    from_email.widget.attrs.update({"class": "from_email"})
    subject.widget.attrs.update({"class": "subject"})
