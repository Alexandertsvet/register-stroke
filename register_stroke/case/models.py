from django.db import models
from django.core.validators import RegexValidator

from register_stroke.settings import DATE_INPUT_FORMATS

from case.constant import MAX_LENGHT_PATIENT, MAX_LENGHT_CODE_PATIENT
from case.functions import preprocessing_hash
from users.models import User

from datetime import datetime


class Patient(models.Model):
    author = models.CharField(
        max_length=MAX_LENGHT_PATIENT, null=False, blank=False, verbose_name='Autor', default='None'
    )
    first_name = models.CharField(
        max_length=MAX_LENGHT_PATIENT, null=False, blank=False, verbose_name='First name', default='имя'
    )
    surname = models.CharField(
        max_length=MAX_LENGHT_PATIENT, blank=True, verbose_name='Surname', default='отчество'
    )
    last_name = models.CharField(
        max_length=MAX_LENGHT_PATIENT, null=False, blank=False, verbose_name='Last name', default='фамилия'
    )
    date_of_birth = models.DateField('Вate of birth', auto_now=False, auto_now_add=False, null=False, blank=False, default=datetime.now)
    code_patient = models.CharField(max_length=MAX_LENGHT_PATIENT, blank=True, null=True)


    def save(self, *args, **kwargs):
        self.first_name = self.first_name.capitalize()
        self.surname = self.surname.capitalize()
        self.last_name = self.last_name.capitalize()
        if not self.pk:
            self.code_patient = preprocessing_hash(self.first_name, self.surname, self.last_name, self.date_of_birth)
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.code_patient}'
