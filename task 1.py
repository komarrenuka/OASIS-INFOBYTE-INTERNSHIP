import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser

# Initialize speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 160)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def wish():
    hour = int(datetime.datetime.now().hour)
    if hour < 12:
        speak("Good Morning")
    elif hour < 18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("I am your Python voice assistant. How can I help you?")

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        command = r.recognize_google(audio)
        print("You said:", command)
        return command.lower()s
    except:
        speak("Sorry, I did not understand.")
        return ""

if __name__ == "__main__":
    wish()
    while True:
        query = take_command()

        if "time" in query:
            time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {time}")

        elif "wikipedia" in query:
            speak("Searching Wikipedia")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            speak(result)

        elif "open google" in query:
            webbrowser.open("https://www.google.com")
            speak("Opening Google")

        elif "exit" in query or "stop" in query:
            speak("Goodbye")
            break
