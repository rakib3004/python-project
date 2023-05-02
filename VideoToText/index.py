import os
import google.auth
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google.cloud import speech_v1
from google.cloud.speech_v1 import enums
from google.oauth2 import service_account

# Set up authentication credentials for Google APIs
credentials, project_id = google.auth.default(scopes=['https://www.googleapis.com/auth/cloud-platform'])
service_account_info = os.environ['GOOGLE_APPLICATION_CREDENTIALS']  # Replace with path to your own service account key file
credentials = service_account.Credentials.from_service_account_file(service_account_info)

# Set up YouTube Data API client
youtube = build('youtube', 'v3', credentials=credentials)

# Set up Google Cloud Speech-to-Text API client
client = speech_v1.SpeechClient(credentials=credentials)

# Define the YouTube video ID
video_id = 'INSERT_YOUTUBE_VIDEO_ID_HERE'

# Get the video details using the YouTube Data API
try:
    video_response = youtube.videos().list(
        part='snippet',
        id=video_id
    ).execute()
except HttpError as e:
    print(f'An HTTP error {e.resp.status} occurred: {e.content}')
    raise e

# Extract the audio from the video using the YouTube Data API
try:
    audio_url = f'https://www.youtube.com/watch?v={video_id}'
    audio_info = youtube.videos().list(
        part='contentDetails',
        id=video_id
    ).execute()
    audio_duration = audio_info['items'][0]['contentDetails']['duration']
    audio_length = int(audio_duration.replace('PT', '').replace('S', ''))
    audio_stream = os.popen(f'youtube-dl -f "bestaudio[ext=m4a]" -g {audio_url}').read().strip()
    audio_filename = f'{video_id}.m4a'
    os.system(f'ffmpeg -ss 0 -t {audio_length} -i "{audio_stream}" "{audio_filename}"')
except HttpError as e:
    print(f'An HTTP error {e.resp.status} occurred: {e.content}')
    raise e

# Transcribe the audio to text using the Google Cloud Speech-to-Text API
try:
    language_code = 'bn-BD'
    sample_rate_hertz = 44100
    encoding = enums.RecognitionConfig.AudioEncoding.LINEAR16
    config = {
        'language_code': language_code,
        'sample_rate_hertz': sample_rate_hertz,
        'encoding': encoding,
    }
    with open(audio_filename, 'rb') as audio_file:
        audio_content = audio_file.read()
    audio = {
        'content': audio_content
    }
    response = client.recognize(config, audio)
    transcript = response.results[0].alternatives[0].transcript
    print(transcript)
except Exception as e:
    print(f'An error occurred: {e}')
    raise e
finally:
    os.remove(audio_filename)
