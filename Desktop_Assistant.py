import pyttsx3 #pip install pyttsx3#Python text-to-speech,s a cross-platform wrapper that supports the native text-to-speech libraries of Windows and Linux
import datetime #inbuilt module
import speech_recognition as sr #to recognise human voice #pip install speechRecognition
import wikipedia #for wikipedia #pip install wikipedia
import webbrowser #inbult
import os
import random #for myself in play query
import smtplib

engine = pyttsx3.init('sapi5') # is the technology for voice recognition and synthesis provided by Microsoft
voices = engine.getProperty('voices') # getting property of voices
#print(voices[0].id) ""printing up name of voice id"""
engine.setProperty('voice',voices[0].id) #setting up voices that is david



def speak(audio):
    engine.say(audio) # engine will speak the audio string
    engine.runAndWait() # function for engine

#JArvis started speaking

def Wishme():
    hour=int(datetime.datetime.now().hour)
    if hour<0 and hour>12:
        speak("Good Morning")
    
    elif hour<=12 and hour>18:
        speak("Good Afternoon")

    else:
        speak("Good Evening")

    speak("I am Jarvis Sir. How I may help You ? ")




def takeCommand(): #It takes microphone input from user and returns string output
    r=sr.Recognizer() # this class will help us to recoginise voice
    with sr.Microphone() as source :
        print("listening....")
        r.pause_threshold = 1#it is pause time, for more press ctrl and click 'pause.threshold', u can change other full parameters
        audio = r.listen(source) #it  will listen our audio.. ctrl + click for more

    try:
        print("Recognizing...")
        query= r.recognize_google(audio, language='en-in') #recoginizing audio in eng-india
        print(f"User said : {query}\n")

    except Exception as e:
        print(e)
        print("please say  that again please..")
        return "None"

    return query

def sendEmail(to,content):
     #SMTP lib python package alredy installed,help us to use gmail.
                             #(google it)   #allow less secured apps in gmail

    server =smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('patilvishal4804@gmail.com','123456789wrong')
    server.sendmail('patilvishal4804@gmail.com',to, content)
    server.close() 

if __name__ == "__main__":
    Wishme()

    #while True:
    if 1:
        query = takeCommand().lower()
        #logic for executing tasks based on query

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com") #inbuilt module
        
        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open tech updates' in query:
            webbrowser.open("techupdate3.com")

        elif 'play music' in query:
            Songs = 'F:\\Videos\\Songs'
            v=os.listdir(Songs) #will list the content of Songs folder
            print(v) #will print the videos
            os.startfile(os.path.join(Songs, v[0])) #startfile will open up that song, and path.join will play

        elif 'the time' in query:
            Time=datetime.datetime.now().strftime('%H:%M:%S')
            speak(f"Sir The time is {Time}") 
            print(Time)
        
        elif 'the paint' in query:
            paintpath="C:\\WINDOWS\\system32\\mspaint.exe"
            os.startfile(paintpath)
            
        elif 'email to harry' in query:
            try:
                speak("what should i say")
                content=takeCommand()
                to ="abc@gmail.com"
                sendEmail(to,content)
                speak("email has been sent")

            except Exception as e:
                print(e)
                speak("I couldnot send email.. please try again")
        elif 'quit' in query:
            exit()

