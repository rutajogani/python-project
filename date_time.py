import pyttsx3
from datetime import datetime

engine = pyttsx3.init()
engine.setProperty('rate', 120) 

def date_time(text):  # date and time function
    now = datetime.now()
    
    date_now = now.strftime("%d-%m-%Y")
    time_now = now.strftime("%H:%M:%S")

    date_time = ["date","time"]

    if "date" in text:
        print(date_now)
        engine.say("Today's date is")
        engine.say(date_now)
        engine.runAndWait()
        print("----Here is your Date----")

    elif "time" in text:
        print(time_now)
        engine.say("Current time is")
        engine.say(time_now)
        print("----Here is your Time----")

engine.runAndWait()
