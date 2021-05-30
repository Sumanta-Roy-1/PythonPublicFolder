from win32com.client import Dispatch
from win32com.client import Dispatch

def speak(str):
    speak = Dispatch(("SAPI.SpVoice"))
    speak.Speak(str)


if __name__=="__main__":
    speak("Good Morning Sumanta, how are you today?")