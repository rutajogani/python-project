import speech_recognition as sr
import pyttsx3


#stt statement
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
    text = r.recognize_google(audio)
    print("USER SPOKE: " + text)/
    return text

text = listen()

# tts statement
engine = pyttsx3.init()
engine.setProperty('rate', 120) 
engine.runAndWait()
