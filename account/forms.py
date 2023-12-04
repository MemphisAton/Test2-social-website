from django import forms
from django.contrib.auth.models import User

from .models import Profile


class LoginForm(forms.Form):
    username = forms.CharField()
    # позволит вставлять type="password" в HTML, чтобы браузер воспринимал его как ввод пароля.
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'email']

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']

    def clean_email(self):
        data = self.cleaned_data['email']
        if User.objects.filter(email=data).exists():
            raise forms.ValidationError('Email already in use.')
        return data


class UserEditForm(forms.ModelForm):
    '''
    позволит пользователям редактировать свое имя, фамилию и адрес электронной почты,
    которые являются атрибутами встроенной в Django модели User
    '''
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

    def clean_email(self):
        '''
        валидация поля email, чтобы пользователи не могли изменять свой бывший адрес
        электронной почты на существующий адрес электронной почты другого пользователя.
        '''
        data = self.cleaned_data['email']
        qs = User.objects.exclude(id=self.instance.id) \
            .filter(email=data)
        if qs.exists():
            raise forms.ValidationError(' Email already in use.')
        return data


class ProfileEditForm(forms.ModelForm):
    '''
    позволит пользователям редактировать данные профиля, сохраненные в
    конкретно-прикладной модели Profile
    '''
    class Meta:
        model = Profile
        fields = ['date_of_birth', 'photo']
