from django import forms

class ImageForm(forms.Form):
    imgFile = forms.ImageField(
        label='Selecciona una imagen',
        help_text='max. 42 mb'
    )