import speech_recognition as sr
import pyttsx3

#stt statement
r = sr.Recognizer()
with sr.Microphone() as source:
    audio = r.listen(source)
text = r.recognize_google(audio)
print(text)

# tts statement
engine = pyttsx3.init()
engine.say(text)
engine.runAndWait()