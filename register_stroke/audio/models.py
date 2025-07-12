from django.db import models
from django.core.validators import FileExtensionValidator
from register_stroke.settings import BASE_DIR, MEDIA_URL

default_path = str(BASE_DIR)+str(MEDIA_URL)

allowed_content_types = ['wav']

class AudioRecording(models.Model):
    audio_file = models.FileField('Аудиофайл',upload_to='audio_recordings/', validators=[FileExtensionValidator(allowed_extensions=allowed_content_types)])
    recorded_at = models.DateTimeField(auto_now_add=True)
    text_from_audio = models.TextField(blank=True, verbose_name='text fron audio', default='')

    def __str__(self):
        return f"Audio recorded at {self.recorded_at.strftime('%Y-%m-%d %H:%M')}"


class AudioRecordingJson(models.Model):
    author = models.CharField(
        max_length=25, null=False, blank=False, verbose_name='Autor', default='None'
    )
    recorded_at = models.DateTimeField(auto_now_add=True)
    id_data = models.CharField(max_length=23, default='')
    data = models.JSONField(default=dict, blank=True)
    audio_file = models.FileField('Аудиофайл',upload_to='audio_case/', validators=[FileExtensionValidator(allowed_extensions=allowed_content_types)], default='audio_case/')
    text_from_audio = models.TextField(blank=True, verbose_name='text fron audio', default='')

    def __str__(self):
        return f"Audio recorded at {self.recorded_at.strftime('%Y-%m-%d %H:%M')}"