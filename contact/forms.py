from contact.models import Contact
from django import forms
from django.core.exceptions import ValidationError


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('first_name', 'last_name', 'phone',)

    def clean(self):
        self.add_error(None, ValidationError("erro muito foda no nome mano"))

        return super().clean()
