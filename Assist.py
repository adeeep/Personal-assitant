import pyttsx3 
import speech_recognition as sr 
import datetime
import wikipedia 
import webbrowser
import os
import smtplib
import wolframalpha 
from selenium import webdriver

main = pyttsx3.init('sapi5')
voices = main.getProperty('voices')
main.setProperty('voice', voices[0].id)


def speak(audio):
    main.say(audio)
    main.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am your Assistant. Please tell me how may I help you")       

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

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('ashwini.verma.564@gmail.com', 'your-password')
    server.sendmail('ashwini.verma.564@gmail.com', to, content)
    server.close()
def processtext(input):
    if "who are you" in input or "define yourself" in input: 
            speak = '''Hello, I am Person. Your personal Assistant. 
            I am here to make your life easier. You can command me to perform 
            various tasks such as calculating sums or opening applications etcetra'''
            assistant_speaks(speak) 
            return
    elif "who made you" in input or "created you" in input: 
            speak = "I have been created as college project by Amandeep."
            assistant_speaks(speak) 
            return
    elif "calculate" in input.lower(): 
              
            # write your wolframalpha app_id here 
            app_id = "WOLFRAMALPHA_APP_ID" 
            client = wolframalpha.Client(app_id) 
  
            indx = input.lower().split().index('calculate') 
            query = input.split()[indx + 1:] 
            res = client.query(' '.join(query)) 
            answer = next(res.results).text 
            assistant_speaks("The answer is " + answer) 
            return

if __name__ == "__main__":
    wishMe()
    while True:
   
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'open microsoft' in query:
            webbrowser.open("microsoft.com")
        elif 'open amazon' in query:
            webbrowser.open("Amazon.com")
        


        elif 'play music' in query:
            music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'email to ashu' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "ashwini.verma.564@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry,I am not able to send this email")    

        elif "exit" in str(text) or "bye" in str(text) or "sleep" in str(text): 
            assistant_speaks("Ok bye, "+ name+'.') 
            break

        else:
            speak("Application not found")



