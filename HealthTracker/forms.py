from django import forms
from .models import Lift, Nutrition, Weight
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class LiftForm(forms.ModelForm):
    class Meta:
        model = Lift
        fields = '__all__'

        widgets = {
            'lift_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Add Lift Name",
            }),

        }


class NutritionForm(forms.ModelForm):
    class Meta:
        model = Nutrition
        fields = '__all__'

        widgets = {
            'food_item': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Add Food Name",
            }),

        }


class WeightForm(forms.ModelForm):
    class Meta:
        model = Weight
        fields = '__all__'


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username', 'email', 'password1', 'password2'
        ]
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Add username",
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': "Add email",
            }),
            'password1': forms.PasswordInput(attrs={
                'placeholder': "Add password",

            }),

        }

