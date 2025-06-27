from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from users.constant import MAX_LENGHT_USERS, MAX_LENGHT_EMAIL, EMPTY


class User(AbstractUser):
    email = models.EmailField(
        verbose_name='e-mail',
        unique=True,
        max_length=MAX_LENGHT_EMAIL,
    )
    username = models.CharField(
        unique=True,
        verbose_name='имя пользователя в системе',
        max_length=MAX_LENGHT_USERS,
        validators=[
            RegexValidator(
                regex=r'^[\w.@+-]+$',
                message='«Нельзя использовать'
                ' пробел и символы, кроме . @ + - _».',
            ),
        ],
    )
    password = models.CharField(
        verbose_name='пароль пользователя',
        max_length=MAX_LENGHT_USERS,
        null=False,
    )
    created = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        ordering = ('username',)
        indexes = [models.Index(fields=['username'])]
        verbose_name = 'Поьзователь.'
        verbose_name_plural = 'Пользователи.'


    def __str__(self):
        return self.username


class Profile(models.Model):
    user = models.OneToOneField('User', verbose_name=('profile'), on_delete=models.CASCADE)
    first_name = models.CharField(
        max_length=MAX_LENGHT_USERS, blank=True, verbose_name='First name'
    )
    surname = models.CharField(
        max_length=MAX_LENGHT_USERS, blank=True, verbose_name='Surname'
    )
    last_name = models.CharField(
        max_length=MAX_LENGHT_USERS, blank=True, verbose_name='Last name'
    )
    country_code = models.CharField(max_length=5, default=EMPTY)
    phone_number = models.CharField(max_length=15, default=EMPTY)
    date_of_birth = models.DateField('Вate of birth', auto_now=False, auto_now_add=False, blank=True, null=True)
    photo = models.ImageField('аватар - ', upload_to='users/profile_images/%Y/%m/%d/', blank=True, null=True, height_field=None, width_field=None, max_length=None)

    class Meta:
        ordering = ('user',)
        indexes = [models.Index(fields=['user'])]
        verbose_name = ('Profile')
        verbose_name_plural = ('Profiles')

    def __str__(self):
        return f'Профиль {self.user}'
