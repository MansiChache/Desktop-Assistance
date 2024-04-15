import subprocess
import wolframalpha
import pyttsx3
import random
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import winshell
import pyjokes
import feedparser
import smtplib
import datetime 
import json
import requests
from twilio.rest import Client
from bs4 import BeautifulSoup
import win32com.client as wincl
from urllib.request import urlopen
import tkinter 
from tkinter import *
import shutil
import cv2


# voice engine
voiceEngine = pyttsx3.init('sapi5')
voices = voiceEngine.getProperty('voices')
voiceEngine.setProperty('voice', voices[1].id)

def speak(text):
	voiceEngine.say(text)
	voiceEngine.runAndWait()

# wishing, greeting and getting user name
def wish():
    print("Hello.")
    time = int(datetime.datetime.now().hour)
    global uname,asname
    if time>= 0 and time<12:
        speak("Good Morning sir or madam!")

    elif time<18:
        speak("Good Afternoon sir or madam!")

    else:
        speak("Good Evening sir or madam!")

    asname ="Charvi"
    speak("I am your Voice Assistant,")
    speak(asname)
    print("I am your Voice Assistant,",asname)
def getName():
    global uname
    speak("Can I please know your name?")
    uname = takeCommand()
    print("Name:",uname)
    speak("I am glad to know you!")
    columns = shutil.get_terminal_size().columns
    speak("How can i Help you, ")
    speak(uname)

def takeCommand():
    global showCommand
    showCommand.set("Listening....")
    cmdLabel.config(textvariable=showCommand)

    recog = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("Listening to the user")
        recog.pause_threshold = 1
        userInput = recog.listen(source)

    try:
        print("Recognizing the command")
        command = recog.recognize_google(userInput, language ='en-in')
        print(f"Command is: {command}\n")

    except Exception as e:
        print(e)
        print("Unable to Recognize the voice.")
        return "None"

    return command

def getWeather(cityName):
    baseUrl = "http://api.openweathermap.org/data/2.5/weather?"
    url = baseUrl + "appid=" + 'd850f7f52bf19300a9eb4b0aa6b80f0d' + "&q=" + cityName
    response = requests.get(url)
    x = response.json()

    if x["cod"] != "404":
        y = x["main"]
        temp = y["temp"]
        temp -= 273
        pressure = y["pressure"]
        humidity = y["humidity"]
        desc = x["weather"]
        description = desc[0]["description"]
        info = (
            " Temperature= " + str(temp) + "°C" + "\n atmospheric pressure (hPa) =" + str(pressure) +
            "\n humidity = " + str(humidity) + "%" + "\n description = " + str(description)
        )
        print(info)
        speak("Here is the weather report at")
        speak(cityName)
        speak(info)
    else:
        speak("City Not Found")


# Define the open_wikipedia function to open Wikipedia in the web browser
# def open_wikipedia():
#     webbrowser.open("https://www.wikipedia.org")
#     speak("Wikipedia is opened.")


def getNews():
    try:
        response = requests.get('https://www.bbc.com/news')
  
        b4soup = BeautifulSoup(response.text, 'html.parser')
        headLines = b4soup.find('body').find_all('h3')
        unwantedLines = ['BBC World News TV', 'BBC World Service Radio',
                    'News daily newsletter', 'Mobile app', 'Get in touch']

        for x in list(dict.fromkeys(headLines)):
            if x.text.strip() not in unwantedLines:
                print(x.text.strip())
    except Exception as e:
        print(str(e))

def capture_photo():
        # Open the default camera
                 cap = cv2.VideoCapture(0)
        # Capture frame-by-frame
                 ret, frame = cap.read()
        # Save the captured frame as an image
                 cv2.imwrite("img.jpg", frame)
        # Release the camera
                 cap.release()

                # Inform the user that the photo has been captured
                 speak("Photo captured successfully!")



# def search_wikipedia(query, num_sentences=3):
#     try:
#         summary = wikipedia.summary(query, sentences=num_sentences)
#         return summary
#     except wikipedia.exceptions.DisambiguationError as e:
#         # If the query is ambiguous, print out the options to help the user choose
#         options = e.options
#         print("The search term is ambiguous. Please choose one of the following options:")
#         for i, option in enumerate(options, 1):
#             print(f"{i}. {option}")
#     except wikipedia.exceptions.PageError:
#         print("Page not found.")
#     except Exception as e:
#         print("An error occurred:", e)

# Your existing code for handling voice commands and responses

# # Example usage of search_wikipedia function
# search_term = "when"
# try:
#     result = search_wikipedia(search_term)
#     if result:
#         print(result)
# except KeyboardInterrupt:
#     print("\nSearch cancelled by user.")

    
def callVoiceAssistant():

    uname=" "
    assname="Charvi"
    os.system('cls')
    wish()
    getName()
    print(uname)

    while True:

        command = takeCommand().lower()
        print(command)

        if "Charvi" in command:
            wish()
            
        elif 'how are you' in command:
            speak("I am fine, Thank you")
            speak("How are you, ")
            speak(uname)

        elif "good morning" in command or "good afternoon" in command or "good evening" in command:
            speak("A very" +command)
            speak("Thank you for wishing me! Hope you are doing well!")

        elif 'fine' in command or "good" in command:
            speak("It's good to know that your fine")
       
        elif "who are you" in command:
            speak("I am your virtual assistant.")

        elif "change my name to" in command:
            speak("What would you like me to call you, Sir or Madam ")
            uname = takeCommand()
            speak('Hello again,')
            speak(uname)
        
        elif "change name" in command:
            speak("What would you like to call me, Sir or Madam ")
            assname = takeCommand()
            speak("Thank you for naming me!")

        elif "what's your name" in command:
            speak("People call me")
            speak(assname)
        
        elif 'time' in command:
            strTime = datetime.datetime.now()
            curTime=str(strTime.hour)+"hours"+str(strTime.minute)+"minutes"+str(strTime.second)+"seconds"
            speak(uname)
            speak(f" the time is {curTime}")
            print(curTime)

        elif "wikipedia" in command:
            speak('Searching Wikipedia')
            command = command.replace("wikipedia", "")
            results = wikipedia.summary(command, sentences=3)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in command:
            speak("Here you go, the Youtube is opening\n")
            webbrowser.open("youtube.com")

        elif 'open google' in command:
            speak("Opening Google\n")
            webbrowser.open("google.com")

        elif 'play music' in command or "play song" in command:
            speak("Enjoy the music!")
            music_dir = "D:\Python\Desktop_voice_assistant"
            songs = os.listdir(music_dir)
            print(songs)
            random = os.startfile(os.path.join(music_dir, songs[1]))

        elif 'joke' in command:
            speak(pyjokes.get_joke())
            
        # elif 'mail' in command:
        #     try:
        #         speak("Whom should I send the mail")
        #         to = input()
        #         speak("What is the body?")
        #         content = takeCommand()
        #         sendEmail(to, content)
        #         speak("Email has been sent successfully !")
        #     except Exception as e:
        #         print(e)
        #         speak("I am sorry, not able to send this email")

        elif 'exit' in command:
            speak("Thanks for giving me your time")
            exit()

        elif "weather" in command:
            speak(" Please tell your city name ")
            print("City name : ")
            cityName = takeCommand()
            getWeather(cityName)

        elif "what is" in command or "who is" in command:
            
            client = wolframalpha.Client("UVUX9U-YT496GJWRE")
            res = client.query(command)

            try:
                print (next(res.results).text)
                speak (next(res.results).text)
            except StopIteration:
                print ("No results")

        elif 'search' in command:
            command = command.replace("search", "")
            webbrowser.open(command)

        elif 'tell me the news' in command:
            speak("Sure, fetching the latest news for you.")
            getNews()
        
        elif "don't listen" in command or "stop listening" in command:
            speak("for how much time you want to stop me from listening commands")
            a = int(takeCommand())
            time.sleep(a)
            print(a)

        elif "camera" in command or "take a photo" in command:
            # Use OpenCV to capture a photo
            capture_photo()

        # elif "camera" in command or "take a photo" in command:
        #     ec.capture(0, "Jarvis Camera ", "img.jpg")
        
        elif 'shutdown system' in command:
          speak("Hold On a Sec ! Your system is on its way to shut down")
          subprocess.call(['shutdown', '/p', '/f'])


        elif "restart" in command:
            subprocess.call(["shutdown", "/r"])

        elif "sleep" in command:
            speak("Setting in sleep mode")
            subprocess.call("shutdown / h")

        elif "write a note" in command:
            speak("What should I write?")
            note = takeCommand()
    
            try:
                with open('sample.txt', 'w') as file:
                    speak("Should I include date and time?")
                    snfm = takeCommand()
                    if 'yes' in snfm or 'sure' in snfm:
                        strTime = datetime.datetime.now().strftime("%H:%M:%S")
                        file.write(strTime + " :- " + note)
                    else:
                        file.write(note)
                speak("Note written successfully!")
            except Exception as e:
                print("An error occurred while writing the note:", e)
                speak("Sorry, I couldn't write the note. Please try again later.")


#Creating the main window 
wn = tkinter.Tk() 
wn.title("Voice Assistant College MiniProject")
wn.geometry('700x300')
wn.config(bg='Pink')

showCommand = StringVar()
  
Label(wn, text='Welcome, this is a Voice Assistant', bg='Pink',
      fg='black', font=('Courier', 15)).place(x=50, y=10)

#Button to convert PDF to Audio form
Button(wn, text="Start", bg='gray',font=('Courier', 15),
       command=callVoiceAssistant).place(x=290, y=100)

showCommand=StringVar()
cmdLabel=Label(wn, textvariable=showCommand, bg='pink',
      fg='black', font=('Courier', 15))
cmdLabel.place(x=250, y=150)

#Runs the window till it is closed
wn.mainloop()