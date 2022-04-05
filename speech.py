import speech_recognition as sr
from gtts import gTTS

  
AUDIO_FILE = ("apples.wav")
  
# use the audio file as the audio source
  
r = sr.Recognizer()
  
with sr.AudioFile(AUDIO_FILE) as source:
    #reads the audio file. Here we use record instead of
    #listen
    audio = r.record(source)  
  
try:
    speech=r.recognize_google(audio)
    print("The audio file contains: " + speech)
  
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
  
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
    
    
tts = gTTS(text= speech, lang='en')
tts.save("record.mp3")
print("Text Converted Successfully ")