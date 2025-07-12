from django import forms
from case.models import Patient
from register_stroke.settings import DATE_INPUT_FORMATS


class PatientEditForm(forms.ModelForm):

    class Meta:
        model = Patient
        fields = ('first_name', 'surname', 'last_name', 'date_of_birth')

        widgets = {
                'first_name': forms.TextInput(attrs={'class': 'form-control form-control-lg', 'placeholder':'имя...',}),
                'surname': forms.TextInput(attrs={'class': 'form-control form-control-lg', 'placeholder':'отчество...',}),
                'last_name': forms.TextInput(attrs={'class': 'form-control form-control-lg', 'placeholder':'фамилия...',}),
                'date_of_birth': forms.DateInput(attrs={'class': 'form-control form-control-lg','type':'date', 'placeholder':'дата рождения...',}),
            }