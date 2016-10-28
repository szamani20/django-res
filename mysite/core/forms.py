from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Member, Food


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
            'email', 'name',
            'address', 'type_of_food',
            'phone_numbers'
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
            'name',
            'address', 'type_of_food',
            'phone_numbers', 'brand_photo'
        )
        help_texts = {

        }
        labels = {

        }


class UserFoodForm(forms.ModelForm):
    class Meta:
        model = Food

        fields = (
            'title', 'price',
            'description', "food_photo"
        )
