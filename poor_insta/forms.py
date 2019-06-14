from django import forms

from poor_insta.models import Photo


class AddPhotoForm(forms.Form):
    photo = forms.FileField()
    class Meta:
        model = Photo
        exclude = ['path', 'user']


class LoginForm(forms.Form):
    user_login = forms.CharField(max_length=64, label='login')
    user_password = forms.CharField(max_length=128, widget=forms.PasswordInput, label='hasło')

