# from typing import Mapping
import pyttsx3
import datetime
import speech_recognition as SR
# SR.re

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voices', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning! Sheben")

    elif hour >=12 and hour <18:
        speak("Good Afternoon! Sheben")
    else:
        speak("Good Evening! Sheben")

    speak("I am Jarvis, please tell how can I help you?")

def takeCommand():
    ''' it Take mcrophone innput from users 
    and returns string output'''
     
    r = SR.Recognizer()
    with SR.Microphone() as source:
        print("Listening .....")
        r.pause_threshold = 1
        audio = r.listen(source)
        print("Step1....")
    try:
        print("Recognising ...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
        print("Step TRY....")

    except Exception as e:
        print(e)
        print("Please say that again Please!")
        return "None"
        print("Step EXCEPT....")

    return query

if __name__=='__main__':
    # speak('Good Morning Shiben, have a good day!')
    wishMe()
    takeCommand()