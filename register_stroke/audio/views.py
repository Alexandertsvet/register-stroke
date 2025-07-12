from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404, redirect, render
from django.http import JsonResponse
from audio.models import AudioRecording, AudioRecordingJson # Assuming you have an AudioRecording model
from django.contrib.auth.decorators import login_required

from register_stroke.settings import BASE_DIR, MEDIA_URL

from audio.forms import AudioFileForm
from django.core.exceptions import ValidationError
from django.http import JsonResponse
import json
import base64

from pathlib import Path
from django.core.files import File
from django.core.files.base import ContentFile
import os

from pydub import AudioSegment
import speech_recognition as sr


from audio.functions import split_data_from_base64, extract_text_from_audio


def upload_audio(request):
    allowed_content_types = ['audio/wav']
    if request.method == 'POST':
        form = AudioFileForm(request.POST, request.FILES)
        if request.FILES:
            audio_data = request.FILES.get('audio_file')
            #print(audio_data.content_type)
            #print(request.FILES['audio_file'])
            
        if form.is_valid():
            form.save()
            return render(request,'homepage/homepage.html',)  # Redirect to a success page
    else:
        form = AudioFileForm()
    return render(request, 'audio/audio.html', {'form': form})

def analysis_audio(request):
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'

    if is_ajax:
        if request.method == 'POST':   
            data = json.load(request)
            id_data = data.get("id_data")
            base64_string = data.get("data") 
            fromat, data = split_data_from_base64(base64_string)
            decoded_data = base64.b64decode(data)
            audio_instance = AudioRecordingJson.objects.create(data=base64_string, author=request.user,id_data=id_data)
            result = extract_text_from_audio(audio_instance, decoded_data)
            audio_instance.text_from_audio = result
            audio_instance.save(update_fields=['text_from_audio'])
            return JsonResponse({'text': audio_instance.text_from_audio})
        return JsonResponse({'status': 'Invalid request'}, status=400)
    else:
        return HttpResponseBadRequest('Invalid request')


def delete_audio(request):
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
    if is_ajax:
        if request.method == 'POST':   
            data = json.load(request)
            id_data = data.get("id_data")
            obj = get_object_or_404(AudioRecordingJson, id_data=id_data)
            obj.delete()
            return JsonResponse({
                'id_data': id_data,
                'delete': True,
                'messege': 'Запись удалена из базы данных!'
            })
        return JsonResponse({'status': 'Invalid request'}, status=400)
    else:
        return HttpResponseBadRequest('Invalid request')