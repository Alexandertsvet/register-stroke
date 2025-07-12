from django.urls import path
from case.views import PatientUpView

app_name = 'case'

urlpatterns = [
    path('patient/create/', PatientUpView.as_view(), name='patient_create'),
]
