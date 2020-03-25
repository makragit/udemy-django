from django import forms
from django.core import validators
from django.contrib.auth.models import User

from first_app.models import temp_User

from .models import UserProfileInfo

# def check_for_z(value):
#     if value[0].lower() != 'z':
#         raise forms.ValidationError("NAME NEEDS TO START WITH Z")

class FormName(forms.Form):
    #name = forms.CharField(validators=[check_for_z])
    name = forms.CharField(label='First Name')
    email = forms.EmailField(label='Email')
    verify_email = forms.EmailField(label='Enter your email again')
    text = forms.CharField(widget=forms.Textarea)

    botcatcher = forms.CharField(required=False, widget=forms.HiddenInput,
                                 validators=[validators.MaxLengthValidator(0)])

    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vmail= all_clean_data['verify_email']

        if email != vmail:
            raise forms.ValidationError("EMAIL")


    # def clean_botcatcher(self):
    #     botcatcher = self.cleaned_data['botcatcher']
    #     if len(botcatcher) > 0:
    #         raise forms.ValidationError("BOT!")
    #
    #     return botcatcher

# USED FOR USERS AND POPULATING CHAPTER
class NewUserForm(forms.ModelForm):
    class Meta:
        model = temp_User
        labels = {
            "f_name": "Farst Name",
            "l_name": "Last Name",
            "email": "Email",
            }
        fields = '__all__'

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'email', 'password')

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site', 'profile_pic')


