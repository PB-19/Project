import pyttsx3
import speech_recognition as sr
import eel

def speak(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 125)
    engine.say(text)
    engine.runAndWait()

@eel.expose
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
        speak(query)
        eel.ShowHood()
    except Exception as e:
        return ""

    return query.lower()
