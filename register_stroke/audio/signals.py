from django.db.models.signals import post_save
from register_stroke.settings import BASE_DIR, MEDIA_URL
from audio.models import AudioRecording
import speech_recognition as sr
from django.dispatch import receiver

from pydub import AudioSegment


@receiver(post_save,sender=AudioRecording)
def create_audiorecording(sender, instance, created, **kwargs):
    if created:
        src = instance.audio_file
        sound = AudioSegment.from_file(instance.audio_file)
        dir_file = str(BASE_DIR)+str(MEDIA_URL)+str(src)
        sound.export(dir_file, format="wav")

        sample = sr.WavFile(dir_file)
        r = sr.Recognizer()
        with sample as audio:
            r.adjust_for_ambient_noise(audio)
            content = r.record(audio)
            try:
                result = r.recognize_google(content, language="ru-RU")
            except sr.UnknownValueError:
                result = "Не удалось распознать речь"
            except sr.RequestError as e:
                result = f"Ошибка сервиса Google Speech Recognition; {e}"

        instance.text_from_audio = result
        instance.save(update_fields=['text_from_audio'])
    else:
        # This code runs when an existing MyModel instance is updated
        # You can add logic here to update other fields based on changes
        pass
