import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import subprocess
import pyjokes

from weather import get_weather
from news import get_news

# ===================== APP PROCESS MAP =====================
app_processes = {
    "whatsapp": "WhatsApp.exe",
    "code": "YourIDE.exe",  # Replace with your IDE filename
    "youtube": "msedge.exe",
    "google": "msedge.exe",
    "stackoverflow": "msedge.exe",
    "mail": "HxTsr.exe"
}

# ===================== TTS SETUP ===========================
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 170)
engine.setProperty('volume', 1.0)

def speak(audio):
    print(f"Jarvis: {audio}")
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am Jarvis. How may I assist you?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
        return query.lower()
    except Exception:
        print("Say that again please...")
        speak("I didn't catch that. Please repeat.")
        return "none"

# ===================== MAIN ===============================
if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            try:
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia:")
                print(results)
                speak(results)
            except Exception:
                speak("Sorry, I couldn't find anything.")

        elif 'search' in query:
            speak("What should I search for?")
            search = takeCommand()
            webbrowser.open(f"https://www.google.com/search?q={search}")

        elif 'open youtube' in query:
            webbrowser.open("https://youtube.com")

        elif 'open google' in query:
            webbrowser.open("https://google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("https://stackoverflow.com")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"It's {strTime} right now.")

        elif 'open code' in query:
            codePath = "C:\\programs.hrmn\\codninja\\first"  # Replace with real path
            if os.path.exists(codePath):
                os.startfile(codePath)
            else:
                speak("Code editor not found.")

        elif 'open whatsapp' in query:
            subprocess.run(["start", "whatsapp://"], shell=True)

        elif 'weather' in query:
            speak("Which city?")
            city = takeCommand()
            get_weather(city, speak)

        elif 'joke' in query:
            joke = pyjokes.get_joke()
            speak(joke)

        elif 'tell me some news' in query:
            get_news(speak)

        elif 'open email' in query:
            subprocess.run(['start', 'mailto:'], shell=True)

        elif 'remember that' in query:
            speak("What should I remember?")
            data = takeCommand()
            with open('memory.txt', 'w') as f:
                f.write(data)
            speak("Okay, I will remember that.")

        elif 'do you remember anything' in query:
            try:
                with open('memory.txt', 'r') as f:
                    memory = f.read()
                speak(f"You asked me to remember: {memory}")
            except FileNotFoundError:
                speak("I don't remember anything yet.")

        elif 'shutdown' in query:
            speak("Shutting down...")
            os.system('shutdown /s /t 1')

        elif 'restart' in query:
            speak("Restarting...")
            os.system('shutdown /r /t 1')

        elif 'sleep' in query:
            speak("Going to sleep...")
            os.system('rundll32.exe powrprof.dll,SetSuspendState 0,1,0')

        elif 'close' in query:
            for app in app_processes:
                if app in query:
                    process_name = app_processes[app]
                    try:
                        os.system(f'taskkill /f /im "{process_name}"')
                        speak(f"{app.capitalize()} has been closed.")
                    except Exception as e:
                        print(e)
                        speak(f"Couldn't close {app}.")
                    break
            else:
                speak("I couldn't identify which app to close.")

        elif 'ok thank you' in query:
            speak("Okay sir, if you need any help, run the program again.")
            break
