from django.urls import path

from homepage.views import HomePage

app_name = 'homepage'

urlpatterns = [
    path('', HomePage.as_view(), name='homepage'),
]