import os   
import time
import playsound
import speech_recognition as sr
from gtts import gTTS
from getip import getip
from TESS import talk_to_tess
import webbrowser

def speak(text):
    tts = gTTS(text=text,lang="en")
    filename="voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        said = ""
        try:
            said = r.recognize_google(audio)
            print(said)
        except Exception as e:
            print("exeption:"+str(e))
    return said




def tess():
    text="hello omar what can i do"
    speak(text)
    while text != "goodbye":
        text = str(input("talk:"))
        if "text" in text:
            speak("opening text editor")
            os.system("gedit")
        if "search" in text:
            b=text.split(" ")
            speak("searching"+b[1])
            webbrowser.open('https://www.google.com/search?q='+b[1], new=2)
        text=talk_to_tess(text)
        text=text.split("000")
        speak(text[1])
        print(os.system(text[0]))
        if "goodbye" in text:
            speak("goodbye omar")
            return 0


text0=""
while True:
    try:
        tess()
    except OSError:
        speak("i cant hear you")
        break
