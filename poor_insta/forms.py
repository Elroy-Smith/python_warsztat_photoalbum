from django import forms

from poor_insta.models import Photo


class AddPhotoForm(forms.Form):
    photo = forms.FileField()
    class Meta:
        model = Photo
        exclude = ['path', 'user']
