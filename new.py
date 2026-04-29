import speech_recognition as sr
import pyttsx3

#stt statement
r = sr.Recognizer()
with sr.Microphone() as source:
    audio = r.listen(source)
text = r.recognize_google(audio)
print("USER SPOKE: " + text)

# tts statement
engine = pyttsx3.init()
engine.setProperty('rate', 120) 

things = ["phone", "TV", "bag"]
for thing in things:
    if thing in text:
        print("FOUND IT")
        engine.say("this is your thing")

engine.runAndWait()