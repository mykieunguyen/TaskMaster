from django import forms

# Login form


class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(
        max_length=150,
        widget=forms.PasswordInput,
    )
