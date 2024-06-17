############################ COMPLETED THE BEGINNER TASK AND TRIED ADVANCE TASK BUT NOT FULLY COMPLETED###########################################################


import pyttsx3
import wikipedia
import webbrowser
import datetime
import speech_recognition as sr
import smtplib
import os
from time import ctime


# here i am using the api of windows for voice 
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[1].id)


def speak(audio):
    engine.say(audio)
    #Without this command, speech will not be audible to us.
    engine.runAndWait()

# hour =int(datetime.datetime.now().hour) 


def takeCommand():
    # here i will use recognizer class to take input from source mic from user 
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("give me a minute to recognize")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("now i am listening")  
        query = r.recognize_google(audio, language ='en-in') 
        print(f"user said {query}\n")

    except Exception as e:
        print("can u say it again....")
        return "none"
    return query.lower()

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('fromemail@gmail.com', 'your-password')
    server.sendmail('fromemail@gmail.com', to, content)
    server.close()





if __name__ == '__main__':
    speak("Welcome back sir")
    # while loop for working in loop and searching key words from query to function
    while True:
        
        query = takeCommand().lower()

        if 'hello' in query:
            speak("Hello , How are you doing ?")

        elif ' name' in query:
            speak("my name is edith")    
        
        elif 'wikipedia' in query:
              speak("Searching your request...")
              query = query.replace("wikipedia","")
              results = wikipedia.summary(query, sentences=3)
              speak("According to the Wikipedia")
              print(results)
              speak(results)
            
        elif 'date' in query:
            current_date = datetime.datetime.now().strftime("%B %d, %Y")
            speak(f"Today's date is: {current_date}")

        elif 'my github' in query:
            webbrowser.open('https://github.com/Endeavor-01')

        elif 'linkedin' in query:
            webbrowser.open('https://www.linkedin.com/in/mohammed-ibrahim-rahmath-786720288?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app')

        elif 'open youtube' in query:
            webbrowser.open('http://www.youtube.com')

        elif 'open google' in query:
            webbrowser.open('http://www.google.com')

        elif 'time' in query:
            time = datetime.datetime.now().strftime("%H : %M")
            speak(f"The time is : {time}")
        
        elif 'my internship file' in query:
            try:
                folder = "C:\\Users\\Adnan\\Downloads\\osisi"
                os.startfile(folder)
            
            except Exception as e:
                print(e)
                speak("sir i do not seem to find it")


     #  fixing required
        elif 'email me' in query:
            try:
                speak("what do i convey")
                content = takeCommand()
                to = "(GO HEAD AND PUT UR EMAIL TO  SEND MESSAGE)"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("the network has been compromised")
              

        elif 'sleep' in query:
            speak("Exiting. Have a great day!")
            print("Exiting...")
            exit(0)  
                   

        

