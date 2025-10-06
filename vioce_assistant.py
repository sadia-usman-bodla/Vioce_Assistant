import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import wikipedia

# ---------- Initialize text-to-speech ----------
engine = pyttsx3.init()
engine.setProperty('rate', 170)
engine.setProperty('volume', 1.0)

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

# ---------- Microphone input ----------
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("\nListening...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio, language='en-US')
        print("You said:", command)
        return command.lower()
    except sr.UnknownValueError:
        speak("Sorry, I didn't understand.")
        return ""
    except sr.RequestError:
        speak("Speech recognition service error.")
        return ""

# ---------- Helper functions ----------
def tell_time():
    current_time = datetime.datetime.now().strftime("%I:%M %p")
    speak(f"The time is {current_time}")

def tell_date():
    today = datetime.date.today().strftime("%B %d, %Y")
    speak(f"Today's date is {today}")

def search_web(query):
    speak(f"Searching for {query}")
    webbrowser.open(f"https://www.google.com/search?q={query}")

# ---------- Main loop ----------
def main():
    speak("Hello! I am your voice assistant. How can I help you?")

    while True:
        command = listen()

        if not command:
            continue

        if "hello" in command or "hi" in command:
            speak("Hello there! How are you?")

        elif "time" in command:
            tell_time()

        elif "date" in command:
            tell_date()

        elif "search" in command:
            query = command.replace("search", "").strip()
            if query:
                search_web(query)
            else:
                speak("What should I search for?")

        elif "wikipedia" in command:
            speak("What should I search on Wikipedia?")
            topic = listen()
            if topic:
                try:
                    summary = wikipedia.summary(topic, sentences=2)
                    speak(summary)
                except Exception:
                    speak("Sorry, I couldn't find that on Wikipedia.")
            else:
                speak("No topic heard.")

        elif "bye" in command or "exit" in command or "stop" in command:
            speak("Goodbye! Have a nice day.")
            break

        else:
            speak("Sorry, I didn't get that. Please say again.")

if __name__ == "__main__":
    main()
