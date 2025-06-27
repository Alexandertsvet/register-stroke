from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponseRedirect

from users.models import Profile
from users.forms import ProfileEditForm

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

@login_required
def profile_edit(request, username):
    if request.method == 'POST':
        profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)
        if profile_form.is_valid():
            print(profile_form)
            if bool(request.FILES):
                get_object_or_404(Profile, user=request.user.id).photo.delete()
            profile_form.save()
            
            return render(request, 'registration/profile.html', {'user': request.user, 'profile': request.user.profile,})  
        else:
            messages.error(request, 'Error update your profile')
    else:
        profile_form = ProfileEditForm(instance=request.user.profile)
    return render(request, 'registration/profile_edit.html', {'profile_form': profile_form,})


"""@login_required
def profile_edit(request, username):
    #user = request.user
    if request.method == 'POST':
        profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)
        if profile_form.is_valid():
            if bool(request.FILES):
                get_object_or_404(Profile, user=request.user.id).photo.delete()
            profile_form.save()
            
            return render(request, 'registration/profile.html', {'user': request.user, 'profile': request.user.profile,})  
        else:
            messages.error(request, 'Error update your profile')
    else:
        profile_form = ProfileEditForm(instance=request.user.profile)
    return render(request, 'registration/profile_edit.html', {'profile_form': profile_form,})"""