import re
import webbrowser
import eel
import sqlite3
import os
import pywhatkit as kit
from playsound import playsound
from engine.config import ASSISTANT_NAME
from engine.command import speak

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

def extract_yt_term(command):
    pattern = r"play\s+(.*?)\s+on\s+youtube"
    match = re.search(pattern,command,re.IGNORECASE)
    return match.group(1) if match else None