import speech_recognition as sr
import pyttsx3
import datetime

recognizer = sr.Recognizer()
engine = pyttsx3.init()


def speak(text):
    engine.say(text)
    engine.runAndWait()


def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio)
        print(f"You said: {query}")
        return query.lower()
    except sr.UnknownValueError:
        print("Sorry, I didn't get that.")
        return ""
    except sr.RequestError as e:
        print(f"Sorry, an error occurred: {e}")
        return ""


def get_time():
    current_time = datetime.datetime.now().strftime("%A, %d %B %Y %H:%M %Z")
    return current_time


def get_weather():
    # Replace this with actual weather fetching code
    return "Currently 32 degrees."


def get_special_days():
    special_days = {
        "March 19th, 2024": [
            "National Poultry Day",
            "National Let's Laugh Day",
            "National Chocolate Caramel Day",
            "National Certified Nurses Day"
        ]
    }
    today = datetime.date.today().strftime("%B %dth, %Y")
    if today in special_days:
        return special_days[today]
    else:
        return "There are no special days today."


def future_plans():
    plans = [
        "Specialization in different domains like medicine, law, or engineering.",
        "Improved ability to generate different creative text formats, like poems or code."
    ]
    return plans


if __name__ == "__main__":
    speak("Hello, I'm your voice assistant. How can I help you?")

    while True:
        query = listen()

        if "hello" in query:
            speak("Hi there! How can I assist you today?")
        elif "goodbye" in query or "bye" in query:
            speak("Goodbye! Have a great day!")
            break
        elif "time" in query:
            speak(f"It is {get_time()}.")
        elif "weather" in query:
            speak(get_weather())
        elif "special day" in query:
            speak("Today's special days are:")
            for day in get_special_days():
                speak(day)
        elif "future plans" in query:
            plans = future_plans()
            speak("My future plans include:")
            for plan in plans:
                speak(plan)
        else:
            speak("Sorry, I'm not sure how to help with that.")