import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init()
engine.say('Sally sells seashells by the seashore.')
engine.say('The quick brown fox jumped over the lazy dog.')
engine.runAndWait()


r = sr.Recognizer()
with sr.Microphone() as source:
    audio = r.listen(source)

print(r.recognize_google(audio))