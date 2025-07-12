from django.core.files import File
from register_stroke.settings import BASE_DIR, MEDIA_URL

from audio.models import AudioRecording
import speech_recognition as sr
import wave
import soundfile as sf
from pydub import AudioSegment
import speech_recognition as sr

from pathlib import Path

#!apt install -y ffmpeg

def extract_text_from_audio(src):
    pass


def split_data_from_base64(data):
    format, data = data.split(',')
    return format, data


def extract_text_from_audio(instance, decoded_data):
    '''
    
    '''
    dir = str(BASE_DIR)+str(MEDIA_URL)+str(instance.audio_file)+str(instance.id)+'.wav'
    model_dir = str(instance.audio_file)+str(instance.id)+'.wav'
    path = Path(dir)
    if not path.is_dir():
        path.parent.mkdir(parents=True, exist_ok=True)
    path.touch(exist_ok=True)
    with open(dir, "wb") as f:
        f.write(decoded_data)
    instance.audio_file = model_dir
    instance.save(update_fields=['audio_file'])
    sound = AudioSegment.from_file(dir)      
    sound.export(dir, format="wav")
    sample = sr.WavFile(dir)
    r = sr.Recognizer()
    with sample as audio:
        r.adjust_for_ambient_noise(audio)
        content = r.record(audio)
        try:
            result = r.recognize_google(content, language="ru-RU")
            return result
        except sr.UnknownValueError:
            result = "Не удалось распознать речь"
            return result
        except sr.RequestError as e:
            result = f"Ошибка сервиса Google Speech Recognition; {e}"
            return result
