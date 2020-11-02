from __future__ import print_function
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import urllib.parse, urllib.request, re
import webbrowser
import pytz
import pyttsx3
import wikipedia
import tkinter as tk
import os
import time
import playsound
import speech_recognition as sr
from gtts import gTTS
import pyaudio
import subprocess
from PIL import ImageTk, Image
alpha = 1

SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']

#screen settings
root = tk.Tk()
root.overrideredirect(1)
root.wm_attributes("-topmost", 1)
root.wm_attributes("-transparentcolor", "white")
root.attributes("-alpha", alpha)
root.geometry("250x250+1115+520")
#positioning
#scr_width = root.winfo_screenwidth()
#scr_height = root.winfo_screenheight()


#scenery
#background = tk.PhotoImage(file="192370.png")
#label2 = tk.Label(root, image=background)
#label2.lift()
#label2.pack()

#character
imgicon = tk.PhotoImage(file="girl.png")
label = tk.Label(root, image=imgicon)
label['bg'] = label.master['bg']
label.pack()
label.place()

def note(text,name):
    date = datetime.datetime.now()
    file_name = name + ".txt"
    with open(file_name, "w") as f:
        f.write(str(date) + "\n")
        f.write(text)
    subprocess.Popen(["notepad.exe",file_name])

def speak(text,lang):
    tts = gTTS(text=text,lang=lang)
    filename = "voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""
        try:
            said = r.recognize_google(audio)
            print(said)
        except:
            speak("Hanashite kudasai!",ja)
    return said.lower()
WAKE = "hey Monica"
ja = "ja"
speak("Ohayou!",ja)
while True:
    print("Listening")
    text = get_audio()

    if text.count(WAKE.lower()) > 0:
        speak("Moshi Moshi!",ja)
        text = get_audio()
        if "hello" in text:
            speak("Konichiwa!",ja)
            continue 
        if "what is your name" in text:
            speak("Boku no namaewa Monika des",ja)
            continue
        YOUT_PHRASE = ["open youtube", "youtube", "show video"]
        for phrase in YOUT_PHRASE:
            if phrase in text:
                speak("Naniga shitai deska youtube",ja)
                link = get_audio()
                webbrowser.open("https://www.youtube.com/results?search_query="+link)
                continue
        GOOG_PHRASE = ["search", "search for", "google"]
        for phrase in GOOG_PHRASE:
            if phrase in text:
                speak("Naniga shitai deska guguru",ja)
                question = get_audio()
                webbrowser.open("http://www.google.com/search?q="+question)
                continue
        SPOT_PHRASE = ["spotify", "open spotify", "play music"]
        for phrase in SPOT_PHRASE:
            if phrase in text:
                speak("Naniga shitai deska spotify",ja)
                question = get_audio()
                webbrowser.open("https://open.spotify.com/search/"+question)
                continue
        WIKI_PHRASE = ["wiki", "wikipedia", "open wiki"]
        for phrase in WIKI_PHRASE:
            if phrase in text:
                speak("Naniga shitai deska Wikipedia",ja)
                question = get_audio()
                wikipedia.set_lang("en")
                speak("Searching!",ja)
                speak((wikipedia.summary(question,sentences = 4)),"en")
                continue
        NOTE_PHRASE = ["make a note", "write this down", "remember this"]
        for phrase in NOTE_PHRASE:
            if phrase in text:
                speak("Namae?",ja)
                name_text = get_audio()
                speak("Nani o kakeba ino?",ja)
                note_text = get_audio()
                note(note_text,name_text)
                speak("Hai!",ja)
                continue

root.mainloop()
