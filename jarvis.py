from tkinter import *
import cv2
import PIL.Image
import PIL.ImageTk
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import subprocess
import winshell
import ctypes
import pyjokes
import smtplib
import roman
from PIL import Image
import time

import wolframalpha
try:
    app=wolframalpha.Client('RPUW5A-7TW6VQ2T9P')
except Exception:
    print("Some error occured ")



numbers = {'hundred': 100, 'thousand': 1000, 'lakh': 100000}
a = {'Tejas': 'tejas.wakodkar9223@gmail.com'}
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

window = Tk()

global var
global var1

var = StringVar()
var1 = StringVar()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def sendemail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('twakodkar557@gmail.com', 'Tejas@04032001')
    server.sendmail('email id', to, content)
    server.close()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <= 12:
        var.set("Good Morning Tejas")
        window.update()
        speak("Good Morning Tejas!")
    elif hour >= 12 and hour <= 18:
        var.set("Good Afternoon Tejas!")
        window.update()
        speak("Good Afternoon Tejas!")
    else:
        var.set("Good Evening Tejas")
        window.update()
        speak("Good Evening Tejas!")
    speak("Myself Jarvis! How may I help you sir")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        var.set("Listening...")
        window.update()
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 400
        audio = r.listen(source)
    try:
        var.set("Recognizing...")
        window.update()
        print("Recognizing")
        query = r.recognize_google(audio, language='en-in')
    except Exception as e:
        return "None"
    var1.set(query)
    window.update()
    return query


def play():
    btn2['state'] = 'disabled'
    btn0['state'] = 'disabled'
    btn1.configure(bg='orange')
    wishme()
    while True:
        btn1.configure(bg='orange')
        query = takeCommand().lower()
        if 'exit' in query:
            var.set("Bye sir")
            btn1.configure(bg='#5C85FB')
            btn2['state'] = 'normal'
            btn0['state'] = 'normal'
            window.update()
            speak("Bye sir")
            break

        elif 'wikipedia' in query:
            if 'open wikipedia' in query:
                webbrowser.open('wikipedia.com')
            else:
                try:
                    speak("searching wikipedia")
                    query = query.replace("according to wikipedia", "")
                    results = wikipedia.summary(query, sentences=2)
                    speak("According to wikipedia")
                    var.set(results)
                    window.update()
                    speak(results)
                except Exception as e:
                    var.set('sorry sir could not find any results')
                    window.update()
                    speak('sorry sir could not find any results')

        elif 'open youtube' in query:
            var.set('opening Youtube')
            window.update()
            speak('opening Youtube')
            webbrowser.open("youtube.com")

        elif 'open course error' in query:
            var.set('opening course era')
            window.update()
            speak('opening course era')
            webbrowser.open("coursera.com")

        elif 'open google' in query:
            var.set('opening google')
            window.update()
            speak('opening google')
            webbrowser.open("google.com")

        elif 'hello' in query:
            var.set('Hello Sir')
            window.update()
            speak("Hello Sir")

        elif 'open stackoverflow' in query:
            var.set('opening stackoverflow')
            window.update()
            speak('opening stackoverflow')
            webbrowser.open('stackoverflow.com')

        #elif ('play music' in query) or ('change music' in query):
            # var.set('Here are your favorites')
            # window.update()
            # speak('Here are your favorites')
            # music_dir = 'D:\\music'
            # songs = os.listdir(music_dir)
            # n = random.randint(0, 27)
            # os.startfile(os.path.join(music_dir, songs[n]))
           
            
        elif 'play music' in query or "play song" in query:
            music_dir = 'D:\\music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

            
        elif "restart" in query:
            subprocess.call(["shutdown", "/r"])

        elif "hibernate" in query or "sleep" in query:
            speak("Hibernating")
            subprocess.call("shutdown / h")

        elif "log off" in query or "sign out" in query:
            speak("Make sure all the application are closed before sign-out")
            time.sleep(5)
            subprocess.call(["shutdown", "/l"])

        elif "write a note" in query:
            speak("What should i write, sir")
            note = takeCommand()
            file = open('jarvis.txt', 'w')
            speak("Sir, Should i include date and time")
            snfm = takeCommand()
            if 'yes' in snfm or 'sure' in snfm:
                strTime = datetime.datetime.now().strftime("% H:% M:% S")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
            else:
                file.write(note)

        elif "show note" in query:
            speak("Showing Notes")
            file = open("jarvis.txt", "r")
            print(file.read())
            speak(file.read(6))


        elif 'the time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            var.set("Sir the time is %s" % strtime)
            window.update()
            speak("Sir the time is %s" % strtime)

        elif 'the date' in query:
            strdate = datetime.datetime.today().strftime("%d %m %y")
            var.set("Sir today's date is %s" % strdate)
            window.update()
            speak("Sir today's date is %s" % strdate)
            
        elif "don't listen" in query or "stop listening" in query:
            speak("for how much time you want to stop jarvis from listening commands")
            a = int(takeCommand())
            time.sleep(a)
            print(a)

        elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            speak("User asked to Locate")
            speak(location)
            webbrowser.open(
                "https://www.google.nl / maps / place/" + location + "")


        elif 'thank you' in query:
            var.set("Welcome Sir")
            window.update()
            speak("Welcome Sir")
            
        elif "i love you" in query:
            speak("It's hard to understand")

        elif 'can you do for me' in query:
            var.set(
                'I can do multiple tasks for you sir. tell me whatever you want to perform sir')
            window.update()
            speak(
                'I can do multiple tasks for you sir. tell me whatever you want to perform sir')

        elif 'old are you' in query:
            var.set("I am a little baby sir")
            window.update()
            speak("I am a little baby sir")
            
        elif 'search' in query or 'play' in query:

            query = query.replace("search", "")
            query = query.replace("play", "")
            webbrowser.open(query)
        
        elif "who i am" in query:
            speak("If you talk then definitely your human.")

        elif "why you came to world" in query:
            speak("Thanks to Tejas. further It's a secret")

        elif 'is love' in query:
            speak(
                "It is 7th sense that destroy all 6th senses and make the person nonsense")

        elif 'lock window' in query:
            speak("locking the device")
            ctypes.windll.user32.LockWorkStation()

        elif 'open media player' in query:
            var.set("opening VLC media Player")
            window.update()
            speak("opening V L C media player")
            # Enter the correct Path according to your system
            path = "C:\\Program Files (x86)\\VideoLAN\\VLC\\vlc.exe"
            os.startfile(path)

        elif 'your name' in query:
            var.set("Myself Jarvis Sir")
            window.update()
            speak('myself Jarvis sir')

        elif 'who creates you' in query:
            var.set('My Creator is Mr. Tejas Wakodkar')
            window.update()
            speak('My Creator is Mr. Tejas Wakodkar')

        elif 'say hello' in query:
            var.set('Hello Everyone! My self Jarvis')
            window.update()
            speak('Hello Everyone! My self Jarvis')
            
        elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you, Sir")
            
        elif 'fine' in query or "good" in query:
            speak("It's good to know that your fine")
            
        elif 'joke' in query:
            speak(pyjokes.get_joke())
            
        elif 'shutdown system' in query:
            speak("Hold On a Sec ! Your system is on its way to shut down")
            subprocess.call('shutdown / p /f')

        elif 'empty recycle bin' in query:
            winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
            speak("Recycle Bin Recycled")

        elif 'open chrome' in query:
            var.set("Opening Google Chrome")
            window.update()
            speak("Opening Google Chrome")
            path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(path)

        elif 'email to me' in query:
            try:
                var.set("What should I say")
                window.update()
                speak('what should I say')
                content = takeCommand()
                to = a['tejas.wakodkar9223@gmail.com']
                sendemail(to, content)
                var.set('Email has been sent!')
                window.update()
                speak('Email has been sent!')

            except Exception as e:
                print(e)
                var.set("Sorry Sir! I was not able to send this email")
                window.update()
                speak('Sorry Sir! I was not able to send this email')

        elif "open python" in query:
            var.set("Opening Python Ide")
            window.update()
            speak('opening python Ide')
            os.startfile(
                'C:\\Users\\Tejas Wakodkar\\AppData\\Local\\Programs\\Microsoft VS Code\\code.exe')

        elif 'calculation' in query:
            sum = 0
            var.set('Yes Sir, please tell the numbers')
            window.update()
            speak('Yes Sir, please tell the numbers')
            while True:
                query = takeCommand()
                if 'answer' in query:
                    var.set('here is result'+str(sum))
                    window.update()
                    speak('here is result'+str(sum))
                    break
                elif query:
                    if query == 'x**':
                        digit = 30
                    elif query in numbers:
                        digit = numbers[query]
                    elif 'x' in query:
                        query = query.upper()
                        digit = roman.fromRoman(query)
                    elif query.isdigit():
                        digit = int(query)
                    else:
                        digit = 0
                    sum += digit

        elif 'click photo' in query:
            stream = cv2.VideoCapture(0)
            grabbed, frame = stream.read()
            if grabbed:
                cv2.imshow('pic', frame)
                cv2.imwrite('pic.jpg', frame)
            stream.release()

        elif 'record video' in query:
            cap = cv2.VideoCapture(0)
            out = cv2.VideoWriter('output.avi', -1, 20.0, (640, 480))
            while(cap.isOpened()):
                ret, frame = cap.read()
                if ret:

                    out.write(frame)

                    cv2.imshow('frame', frame)
                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        break
                else:
                    break
            cap.release()
            out.release()
            cv2.destroyAllWindows()
            
        elif 'temperature' in query:
            try:
                res=app.query(query)
                print(next(res.results).text)
                speak(next(res.results).text)
            except:
                print("Internet connection Error")
                
        else:
            try:
                res=app.query(query)
                print(next(res.results).text)
                speak(next(res.results).text)
            except:
                print("Internet connection Error")
                


def update(ind):
    frame = frames[(ind) % 100]
    ind += 1
    label.configure(image=frame)
    window.after(100, update, ind)


label2 = Label(window, textvariable=var1, bg='#FAB60C')
label2.config(font=("Courier", 20))
var1.set('User Said:')
label2.pack()

label1 = Label(window, textvariable=var, bg='#ADD8E6')
label1.config(font=("Courier", 20))
var.set('Welcome')
label1.pack()

frames = [PhotoImage(file='Assistant.gif', format='gif -index %i' % (i))
          for i in range(100)]
window.title('JARVIS')

label = Label(window, width=500, height=500)
label.pack()
window.after(0, update, 0)

btn0 = Button(text='WISH ME', width=20, command=wishme, bg='#5C85FB')
btn0.config(font=("Courier", 12))
btn0.pack()
btn1 = Button(text='PLAY', width=20, command=play, bg='#5C85FB')
btn1.config(font=("Courier", 12))
btn1.pack()
btn2 = Button(text='EXIT', width=20, command=window.destroy, bg='#5C85FB')
btn2.config(font=("Courier", 12))
btn2.pack()


window.mainloop()
