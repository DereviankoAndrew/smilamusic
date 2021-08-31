from .models import StudentRequest
from django.forms import ModelForm, TextInput, Select
from django import forms


class StudentRequestForm(ModelForm):
    class Meta:
        model = StudentRequest
        fields = ['age', 'sex', 'phone_number', 'occupation']

        widgets = {
            'age': TextInput(attrs={
                'class': 'enter-input',
            }),
            'sex': TextInput(attrs={
                'class': 'enter-input',
            }),
            'phone_number': TextInput(attrs={
                'class': 'enter-input',
            }),
            'occupation': Select(choices=[
                ('Оберіть напрямок', 'Оберіть напрямок'),
                ('Барабани', 'Барабани'),
                ('Гітара', 'Гітара'),
                ('Клавішні', 'Клавішні'),
                ('Вокал', 'Вокал'),
            ],
                attrs={
                'class': 'enter-input',
            }),
        }
        # attrs = {
        #     'class': 'enter-input',
        # }