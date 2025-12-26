import pyttsx3 #for voice audio
import datetime #inbuilt
import speech_recognition as sr
import wikipedia 
import webbrowser #inbuilt-include websites
import os #inbuilt to access files
import subprocess
import smtplib #smtblib is used to send email-inbuilt

engine=pyttsx3.init('nsss')
voices = engine.getProperty('voices')
#print(voices)
engine.setProperty('volume', 1)  # 0.0 to 1.0
engine.setProperty('rate', 160) # 150 is default
engine.setProperty('voice',voices[14].id) #167

def speak (audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>0 and hour<12:
        speak("good morning")
    elif hour>=12 and hour<18:
        speak("good afternoon!")
    else:
        speak("good evening!")
    speak("hii i am jarvis how can i help you")

def takeCommand():#takes microphone input and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source: #you need PyAudio for sr.Microphone() to work.
        print("Listning...")
        r.pause_threshold = 1 # seconds of non-speaking audio before a phrase is considered complete can use energy thorost hold to make limit of sound volume
        audio = r.listen(source)

    try:
        print("recognizing..")
        query = r.recognize_google(audio,language='en-in')
        print(f"user said: {query}\n")# print("user said:",query) is written in f string

    except Exception as e:
        print(e) #it prints error so if you want to print it u can or not
        print("said that again please")
        return "None"
    return query

def sendEmail(to,content): #smtblib is used to send email
    #1st have to dec sequre using smpt see code harr again at this
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login('Pythoncp25@gmail.com', 'pgcy pslo xnms lgai')
        server.sendmail('Pythoncp25@gmail.com', to, content)
        server.close()
        print("Email has been sent.")

if __name__=="__main__": #if this program was imported from other program then program below this will not exicute
    speak("hello anvit gupta kya kar rahe ho")
    wishme()
    while True:
        query =takeCommand().lower()
        if 'wikipedia' in query:
            speak('searching wikipedia...')
            query = query.replace("wikipedia","") #remove wikipedia
            result = wikipedia.summary(query, sentences=2) #retunrn 2 sentences from wikipedia
            speak("According to wikipedia")
            print(result)
            speak(result)

        elif 'open youtube' in query:
            webbrowser.open("https://www.youtube.com")

        elif 'open google' in query:
            webbrowser.open("https://www.google.com")

        elif 'play music' in query:
            music_dir= "/Users/amangupta/Downloads/Music"
            songs = os.listdir(music_dir) #make list of all files
            print(songs)
            #os.startfile(os.path.join(music_dir,songs[0])) #-for windows ,can also use random module to generate random song by using random index
            song_path = os.path.join(music_dir, songs[2])
            subprocess.call(["open", "-a", "Music",song_path])

        elif 'current time' in query:
            strtime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir the time is {strtime}")
            print(f"sir the time is {strtime}")

        elif 'apple store' in query:
            codePath="/System/Applications/App Store.app"
            subprocess.call(["open", "-a",codePath])

        elif 'email to aman' in query:
            try:
                speak("what to send??")
                content=takeCommand()
                to="cbsemrps1@gmail.com"
                sendEmail(to,content)
                speak("email sended")
            except Exception as e:
                print(e)
                speak("cant send this message")
        elif 'make a note' in query:
            speak("What should I write?")
            note = takeCommand()
            with open("note.txt", "a") as f:
                f.write(f"{datetime.datetime.now()} - {note}\n")
            speak("Note saved.")

        elif 'stop' in query:
            break