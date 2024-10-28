import os
import eel
from engine.command import *
from engine.features import *
from engine.auth import recognize

def start():
    
    eel.init("www")

    playAssistantSound()

    @eel.expose
    def init():
        subprocess.call([r'device.bat'])
        eel.hideLoader()
        speak("Ready for face authentication")
        flag = recognize.AuthenticateFace()
        if flag==1:
            eel.hideFaceAuth()
            speak("Face authentication successful")
            eel.hideFaceAuthSuccess()
            speak("Welcome Sir!")
            eel.hideStart()
            playAssistantSound()
        else: speak("Face authentication failed")

    os.system('start msedge.exe --app="http://localhost:8000/index.html"')

    eel.start("index.html", mode=None, host="localhost", block=True)