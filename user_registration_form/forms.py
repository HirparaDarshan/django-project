# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from user_registration_form.models import CustomUser, Profile


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)  #
    mobile_number = forms.CharField(max_length=15, required=False)  #
    hobby = forms.CharField(max_length=100, required=False)  #
    country = forms.CharField(max_length=50, required=False)  #
    profile_pic = forms.ImageField(required=False)  #

    class Meta:
        model = CustomUser
        fields = [
            "username",
            "email",
            "password1",
            "password2",
            "mobile_number",
            "hobby",
            "country",
            "profile_pic",
        ]

    def save(self, commit=True):
        user = super().save(commit=commit)

        Profile.objects.create(
            user=user,
            mobile_number=self.cleaned_data.get("mobile_number"),
            hobby=self.cleaned_data.get("hobby"),
            country=self.cleaned_data.get("country"),
            profile_pic=self.cleaned_data.get("profile_pic"),
        )

        return user
