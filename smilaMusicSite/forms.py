from .models import StudentRequest
from django.forms import ModelForm, TextInput


class StudentRequestForm(ModelForm):
    class Meta:
        model = StudentRequest
        fields = ['age', 'sex', 'occupation', 'phone_number']

        widgets = {
            'age': TextInput(attrs={
                'class': 'enter-input',
            }),
            'sex': TextInput(attrs={
                'class': 'enter-input',
            }),
            'occupation': TextInput(attrs={
                'class': 'enter-input',
            }),
            'phone_number': TextInput(attrs={
                'class': 'enter-input',
            }),
        }