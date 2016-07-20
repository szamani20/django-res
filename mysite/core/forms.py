from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Member


class RegistrationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        for f in iter(self.fields):
            print(f)
            f = self.fields[f]
            if f.required:
                f.widget.attrs.update({'class': 'required'})

    class Meta:
        model = Member
        fields = (
            'username', 'email', 'first_name',
            'last_name', 'address',
            'type_of_food', 'phone_numbers'
        )
        help_texts = {

        }
        labels = {

        }

    def clean_foods(self):
        return self.cleaned_data['foods'] or None


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = (
            'first_name', 'last_name',
            'foods', 'address',
            'type_of_food', 'phone_numbers'
        )
        help_texts = {

        }
        labels = {

        }
