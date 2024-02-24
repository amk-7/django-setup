
from django import forms

class LoginForm(forms.Form):
    phone_number = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())

class ChangePasswordForm(forms.Form):
    old_password = forms.CharField(widget=forms.PasswordInput())
    new_password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())

class ForgetPasswordForm(forms.Form):
    email_or_phone_number = forms.CharField(widget=forms.TextInput())


# def clean(self):
#     self.clean_data = super(ChangePasswordForm, self).clean()
#     old_password = self.clean_data.get('old_password')
#     new_password = self.clean_data.get('new_password')
#     confirm_password = self.clean_data.get('new_password')
    
#     if confirm_password != new_password:
#         self._errors['confirm_password'] = "Les mot de passe d"