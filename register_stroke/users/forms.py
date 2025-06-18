from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm, PasswordChangeForm, PasswordResetForm, SetPasswordForm
from .models import User, Profile

class UserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email','password1')
        widgets = {
                'username': forms.TextInput(attrs={'class': 'form-control form-control-lg', 'placeholder':'имя пользователя...',}),
                'email': forms.TextInput(attrs={'class': 'form-control form-control-lg', 'placeholder':'email...','type':'email'}),
            }
    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        self.fields["password1"].widget.attrs.update({"class": "form-control form-control-lg", 'placeholder':'введите пароль...'})
        self.fields["password2"].widget.attrs.update({"class": "form-control form-control-lg", 'placeholder':'повторите ввод пароля...'})


class UserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('username', 'email')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Комментарий...'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'email...'}),
        }

class LoginView_form(AuthenticationForm):
    class Meta(AuthenticationForm):
        model = User
        fields = ('username', 'password')
       
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update({"class": "form-control form-control-lg", 'placeholder':'введите email пользователя...'})
        self.fields["password"].widget.attrs.update({"class": "form-control form-control-lg", 'placeholder':'введите пароль...'})


class PasswordChangeForm_form(PasswordChangeForm):
    class Meta(PasswordChangeForm):
        model = User
        field_order = ["old_password", "new_password1", "new_password2"]
       
       
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["old_password"].widget.attrs.update({"class": "form-control form-control-lg", 'placeholder':'введите старый пароль...'})
        self.fields["new_password1"].widget.attrs.update({"class": "form-control form-control-lg", 'placeholder':'введите новый пароль...'})
        self.fields["new_password2"].widget.attrs.update({"class": "form-control form-control-lg", 'placeholder':'повторите ввод нового пароля...'})


class PasswordResetForm_form(PasswordResetForm):
    class Meta(PasswordResetForm):
        model = User
        field_order = ["email"]
        widgets = {
                'email': forms.TextInput(attrs={'class': 'form-control form-control-lg', 'placeholder':'email...','type':'email'}),
            }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["email"].widget.attrs.update({"class": "form-control form-control-lg", 'placeholder':'введите адрес электронной почты...'})


class SetPasswordForm_form(SetPasswordForm):
    class Meta(PasswordResetForm):
        model = User
        field_order = ["new_password1", "new_password2"]


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["new_password1"].widget.attrs.update({"class": "form-control form-control-lg", 'placeholder':'введите новый пароль...'})
        self.fields["new_password2"].widget.attrs.update({"class": "form-control form-control-lg", 'placeholder':'повторите ввод нового пароля...'})


class ProfileEditForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['first_name', 'surname', 'last_name', 'date_of_birth', 'country_code', 'phone_number', 'photo']
