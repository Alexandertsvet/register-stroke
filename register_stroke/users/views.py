from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

from django.shortcuts import get_object_or_404, redirect, render

from users.models import Profile


from .forms import UserCreationForm, LoginView_form, PasswordChangeForm_form, PasswordResetForm_form, SetPasswordForm_form

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('users:login')
    template_name = 'registration/signup.html'

class LoginView(auth_views.LoginView):
    form_class = LoginView_form
    success_url = reverse_lazy('homepage:homepage')
    template_name = 'registration/login.html'


class LogoutView(auth_views.LogoutView):
    success_url = reverse_lazy('homepage:homepage')


class PasswordChangeView(auth_views.PasswordChangeView):
    form_class = PasswordChangeForm_form
    success_url = reverse_lazy('users:login')
    template_name = 'registration/password_change_form.html'


class PasswordResetView(auth_views.PasswordResetView):
    form_class = PasswordResetForm_form
    subject_template_name = "registration/password_reset_subject.txt"
    success_url = reverse_lazy("password_reset_done")
    template_name = "registration/password_reset_form.html"


class PasswordResetConfirmView(auth_views.PasswordResetConfirmView):
    form_class = SetPasswordForm_form
    success_url = reverse_lazy("password_reset_complete")
    template_name = "registration/password_reset_confirm.html"

@login_required
def profile(request, username):
    user = request.user
    profile = get_object_or_404(Profile, user=username)
    context = {
        'user': user,
        'profile': profile,
    }
    return render(request, 'registration/profile.html', context)