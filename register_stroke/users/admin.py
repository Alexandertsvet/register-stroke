from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import User, Profile

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_dysplay = ['username', 'email', 'first_name', 'last_name']


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_dysplay = ['user', 'date_of_birth', 'photo']
    raw_id_fields = ['user']
