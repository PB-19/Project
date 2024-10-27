import time
import pyttsx3
import speech_recognition as sr
import eel

def speak(text):
    text=str(text)
    engine = pyttsx3.init()
    engine.setProperty('rate', 125)
    eel.DisplayMessage(text)
    engine.say(text)
    eel.receiverText(text)
    engine.runAndWait()

def takecommand():
    r = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("Listening...")
        eel.DisplayMessage("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)

        audio = r.listen(source, 10, 5)

    try:
        print("Recognizing...")
        eel.DisplayMessage("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}")
        eel.DisplayMessage(query)
        time.sleep(3)
    except Exception as e:
        return ""

    return query.lower()

@eel.expose
def allCommands(message=1):

    if message==1:
        query = takecommand()
        eel.senderText(query)
    else:
        query = message
        eel.senderText(query)

    try:
        if "open" in query:
            from engine.features import openCommand
            openCommand(query)
        elif "on youtube" in query:
            from engine.features import playYoutube
            playYoutube(query)
        elif "send message" in query or "phone call" in query or "video call" in query:
            from engine.features import findContact, whatsapp
            flag=""
            contact_no,name = findContact(query)
            if contact_no!=0:
                if "send message" in query:
                    flag = "message"
                    speak("What message to send? ")
                    query = takecommand()
                elif "phone call" in query:
                    flag = "call"
                else:
                    flag = "video call"
                whatsapp(contact_no,query,flag,name)
        else:
            from engine.features import chatbot
            chatbot(query)
    except:
        pass
    
    eel.ShowHood()