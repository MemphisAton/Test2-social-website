from django import forms


class LoginForm(forms.Form):
    username = forms.CharField()
    # позволит вставлять type="password" в HTML, чтобы браузер воспринимал его как ввод пароля.
    password = forms.CharField(widget=forms.PasswordInput)
