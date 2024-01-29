import random
import pyttsx3
import speech_recognition as sr
import datetime
import os
import pyaudio
import cv2
from requests import get
import wikipedia
import webbrowser
import pywhatkit as kit

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)


# text to speech function
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


# Convert voice to text
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listerning Sir.........")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=4, phrase_time_limit=10)
        # audio=r.listen(source)
        # query=r.recognize_google(audio, language="en-in")
        # print(f"user said{query}")
        # return query

    try:

        print("Recognizing sir................")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")
    except Exception as e:
        speak("Say that again please sir...")
        return "none"
    return query


# to wish
def wish():
    hour = int(datetime.datetime.now().hour)

    if hour >= 4 and hour <= 11:
        speak("good morning SOUMADEEP  sir")

    elif hour == 12:
        speak("good noon SOUMADEEP  sir")

    elif hour > 12 and hour < 15:
        speak("good afternoon SOUMADEEP sir")

    elif hour >= 15 and hour <= 21:
        speak("good evening SOUMADEEP  sir")

    else:
        speak("good night SOUMADEEP sir")

    speak("I am jarvis a i, your servant,  please tell me how can i help you")


# def fun():
#     if 1:
#         query = takeCommand().lower()
#         if "who is alokesh" in query:
#             speak("sir, alokesh is fuck boy")


if __name__ == "__main__":
    wish()
    # fun()
    # while True:
    if 1:
        query = takeCommand().lower()

        # logic bulding for tasks

        if "open photos" in query:
            pPath = "C:\\Users\\SOUMADEEP GHOSH\\OneDrive\\Pictures\\mobile pics\\Camera"
            os.startfile(pPath)
            speak("opening photos sir")
        elif "open cmd" in query:
            speak("opening cmd sir")
            os.system("start cmd")
        elif "open camera" in query:
            cap = cv2.VideoCapture(0)
            while True:
                cap = cv2.VideoCapture(0)
                while cap.isOpened():  # Check if the camera is open
                    ret, img = cap.read()
                    if not ret:  # If no frame is received, break the loop
                        break
                    cv2.imshow('webcam', img)
                    k = cv2.waitKey(1)
                    if k == ord('q'):
                        break
        elif "play movies" in query:
            movies_dir = "C:\\Users\\SOUMADEEP GHOSH\\Videos\\movies"
            movie = os.listdir(movies_dir)
            rd = random.choice(movie)
            os.startfile(os.path.join(movies_dir, rd))
            speak("opening movies sir")

        elif "ip address" in query:
            ip = get('https://api.ipify.org').text
            speak(f"Your IP address is {ip}")

        elif "wikipedia" in query:
            speak("searching wikipedia.....")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("accoding to wikipedia")
            speak(results)

        elif "open youtube" in query:
            webbrowser.open("www.youtube.com")
            speak("opening youtube sir")
        elif "open facebook" in query:
            webbrowser.open("www.facebook.com")
            speak("opening facebook sir")
        elif "open instragram" in query:
            webbrowser.open("www.instragram.com")
            speak("opening instragram sir")
        elif "open google" in query:
            speak("sir, what should i search on google")
            cm = takeCommand().lower()
            webbrowser.open(f"{cm}")
            speak("opening google sir")


        elif "send message" in query:

            speak("Sir, please tell me the number")
            cm1 = takeCommand().lower()

            speak("Sir, please tell me the message")

            cm2 = takeCommand().lower()

            kit.sendwhatmsg(f"+91{cm1}", cm2, 13, 10)  # Corrected the time format


        elif "play songs on youtube" in query:
            speak("Sir, plese tell me name of the song")
            song = takeCommand().lower()
            kit.playonyt(song)
            speak(f"opening youtube and search {song} sir")


        elif "play music" in query:
            music_dir = "E:\\songs for jarvis"
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[0]))
        # elif "the time" in query:
        #     strTime = datetime.datetime.now().strftime("%H:%M:%S")
        #     speak(f"Sir time is{strTime}")


