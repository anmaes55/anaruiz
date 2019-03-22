from django import forms


class ContactForm(forms.Form):
    nombre = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Nombre'}))
    from_email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    asunto = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Asunto'}))
    mensaje = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Escribe aquí tu duda o comentario'}),
                              required=True)
