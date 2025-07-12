from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from case.forms import PatientEditForm
from case.models import Patient
from django.views.generic.edit import CreateView
from django.urls import path, include, reverse_lazy


class PatientUpView(CreateView):
    model = Patient
    form_class = PatientEditForm
    template_name = 'case/patient/patient.html'
    success_url = reverse_lazy('homepage:homepage')

    def form_valid(self, form):
        instance = form.instance
        instance.author = self.request.user
        return super().form_valid(form)
