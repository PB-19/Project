import re
import webbrowser
import eel
import sqlite3
import os
import pywhatkit as kit
import pvporcupine
import pyaudio
import time
import struct

from playsound import playsound
from engine.config import ASSISTANT_NAME
from engine.command import speak
from engine.helper import extract_yt_term

conn = sqlite3.connect("jarvis.db")
cursor = conn.cursor()

@eel.expose
def playAssistantSound():
    music_dir = r"www\assets\audio\start_sound.mp3"
    playsound(music_dir)

def openCommand(query):
    query = query.replace(ASSISTANT_NAME,"")
    query = query.replace("open", "")
    query.lower()

    # if query!="":
    #     speak("Opening"+query)
    #     os.system("start "+query)
    # else:
    #     speak("Not found...")

    app_name = query.strip()
    if app_name != "":
        try:
            cursor.execute("SELECT path FROM sys_command WHERE name IN (?)", (app_name,))
            results = cursor.fetchall()

            if len(results)!=0:
                speak("Opening "+query)
                os.startfile(results[0][0])
            else:
                cursor.execute("SELECT url FROM web_command WHERE name IN (?)", (app_name,))
                results = cursor.fetchall()

                if len(results)!=0:
                    speak("Opening "+query)
                    webbrowser.open(results[0][0])
                else:
                    try:
                        speak("Opening "+query)
                        os.system("start "+query)
                    except:
                        speak("Not found...")
        except:
            speak("Something went wrong...")

def playYoutube(query):
    search_term = extract_yt_term(query)
    speak("Playing "+search_term+" on YouTube")
    kit.playonyt(search_term)

def hotword():
    porcupine=None
    paud=None
    audio_stream=None
    try:
        porcupine=pvporcupine.create(keywords=["jarvis"]) 
        paud=pyaudio.PyAudio()
        audio_stream=paud.open(
            rate=porcupine.sample_rate,
            channels=1,
            format=pyaudio.paInt16,
            input=True,
            frames_per_buffer=porcupine.frame_length
        )
        while True:
            keyword=audio_stream.read(porcupine.frame_length)
            keyword=struct.unpack_from("h"*porcupine.frame_length,keyword)
            keyword_index=porcupine.process(keyword)
            if keyword_index>=0:
                print("hotword detected")
                import pyautogui as autogui
                autogui.keyDown("win")
                autogui.press("j")
                time.sleep(2)
                autogui.keyUp("win")
                
    except:
        if porcupine is not None:
            porcupine.delete()
        if audio_stream is not None:
            audio_stream.close()
        if paud is not None:
            paud.terminate()