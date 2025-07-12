from django import forms
from audio.models import AudioRecording

class AudioFileForm(forms.ModelForm):
    class Meta:
        model = AudioRecording
        fields = ['audio_file']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['audio_file'].widget.attrs.update({"class": "form-control form-control-lg",})
