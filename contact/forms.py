from contact.models import Contact
from django import forms
from django.core.exceptions import ValidationError


class ContactForm(forms.ModelForm):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'classe-a classe-b',
                'placeholder': 'teste',
            }
        ),
        label='Primeiro Nome',
        help_text='help text'
    )

    class Meta:
        model = Contact
        fields = (
            'first_name', 'last_name', 'phone',
            'email', 'description', 'category',
            )

    def clean(self):
        cleaned_data = self.cleaned_data
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')

        if first_name == last_name:
            error_msg = ValidationError(
                    'O Primeiro Nome Não Deve Ser Igual ao Segundo Nome !',
                    code='invalid')

            self.add_error('first_name', error_msg)
            self.add_error('last_name', error_msg)

        return super().clean()

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')

        if first_name == 'teste':
            self.add_error(
                'first_name',
                ValidationError('ERRO', code='invalid')
                )

        return first_name
