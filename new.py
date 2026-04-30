import speech_recognition as sr
import pyttsx3
from datetime import datetime

#stt statement
r = sr.Recognizer()
with sr.Microphone() as source:
    audio = r.listen(source)
text = r.recognize_google(audio)
print("USER SPOKE: " + text)

# tts statement
engine = pyttsx3.init()
engine.setProperty('rate', 120) 

def date_time():  #date and time function

    now_date = datetime.now()
    date_now = now_date.strftime("%d-%m-%Y")
    now_time = datetime.now()
    time_now = now_time.strftime("%H:%M:%S")

    date_time = ["date","time"]

    if "date" in text:
        print(date_now)
        engine.say(date_now)
        engine.say("date is here:")
        print("----Here is your Date----")
    else:
        print(time_now)
        engine.say("time is here:")
        print("----Here is your Time----")

# things = {
#     "phone": "Here is your phone",
#     "tv": "Turning on the TV",
#     "bag": "Here is your bag"
# }

# for thing in things:
#     if thing in text:
#         print("FOUND IT")
#         engine.say(things[thing])
    
# else: 
#         print("Not Found")

engine.runAndWait()

date_time()
