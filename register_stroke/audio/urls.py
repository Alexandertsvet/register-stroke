from django.urls import path
from audio.views import upload_audio, analysis_audio, delete_audio

app_name = 'audio'

urlpatterns = [
    path('create/', upload_audio, name='audio'),
    path('create/analysis/', analysis_audio, name='analysis'),
    path('create/delete/', delete_audio, name='delete'),
]