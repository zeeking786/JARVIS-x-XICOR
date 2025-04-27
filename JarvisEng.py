import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import turtle
from gtts import gTTS
import smtplib
import pyglet
import sounddevice as sd
from scipy.io.wavfile import write

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

import cv2
import playsound
import time
import random
import wolframalpha
from tkinter import *
import tkinter
from PIL import ImageTk, Image
import PIL.Image
import socket
import getmac
from textblob import TextBlob
import nltk
from newspaper import Article
import matplotlib.pyplot as plt

from JarvisHindi import *
import JarvisHindi as h

client = wolframalpha.Client('WKLYVP-EEEU5E533T')
root = ""

num = 1


def speak(output):
    global num
    num += 1
    print(output)
    toSpeak = gTTS(text=output, lang='en', slow=False)
    file = str(num) + ".mp3 "
    toSpeak.save(file)
    playsound.playsound(file, True)
    os.remove(file)


def get_audio():
    rObject = sr.Recognizer()
    audio = ''
    with sr.Microphone() as source:
        print("Speak...")
        audio = rObject.listen(source, phrase_time_limit=0)
        print("Stop.")

        try:
            text = rObject.recognize_google(audio, language='en-US')
            print("You : " + text)

            return text

        except:
            speak("Could not understand your audio...PLease try again !")
            return 0


def greetMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")


def shutdown():
    speak("understood Sir")
    speak('connecting to command prompt')
    speak('shutting down your computer')
    os.system('shutdown -s')


def gooffline():
    speak('ok Sir')
    speak('closing all systems')
    speak('disconnecting to servers')
    speak('going offline')
    quit()


class Widget:
    def __init__(self):
        global root
        root = Tk()
        root.title('Xicor')
        root.config(background='Red')
        root.geometry('225x600')
        root.resizable(0, 0)

        root.iconbitmap(r'D:\Jarvis\check\Untitled-1.ico')
        img = ImageTk.PhotoImage(PIL.Image.open(r"download.png"))
        panel = Label(root, image=img)
        panel.pack(side="bottom", fill="both", expand="no")

        self.compText = StringVar()
        self.userText = StringVar()
        self.userText.set('Click \'Start Listening\' to Give myCommands')
        userFrame = LabelFrame(root, text="User", font=('Black ops one', 10, 'bold'))
        userFrame.pack(fill="both", expand="yes")
        left2 = Message(userFrame, textvariable=self.userText, bg='dodgerBlue', fg='white')
        left2.config(font=("Comic Sans MS", 10, 'bold'))
        left2.pack(fill='both', expand='yes')
        compFrame = LabelFrame(root, text="Xicor", font=('Black ops one', 10, 'bold'))
        compFrame.pack(fill="both", expand="yes")
        left1 = Message(compFrame, textvariable=self.compText, bg='Red', fg='white')
        left1.config(font=("Comic Sans MS", 10, 'bold'))
        left1.pack(fill='both', expand='yes')
        btn = Button(root, text='Start Listening!', font=('Black ops one', 10, 'bold'), bg='deepSkyBlue', fg='white',
                     command=self.assistant).pack(fill='x', expand='no')
        btn2 = Button(root, text='Close!', font=('Black Ops One', 10, 'bold'), bg='deepSkyBlue', fg='white',
                      command=root.destroy).pack(fill='x', expand='no')
        btn3 = Button(root, text='Change Language', font=('Black Ops One', 10, 'bold'), bg='deepSkyBlue', fg='white',
                      command=self.changeLang).pack(fill='x', expand='no')
        speak('Hello... I am Xikor ! What can I do for You?')
        self.compText.set('Hello... I am Xikor ! What can I do for You?')
        root.bind("<Return>", self.assistant)
        root.mainloop()

    def changeLang(self):
        speak("Select Language between English or Hindi")
        text = get_audio().lower()
        if text == 0:
            self.checkLang()
        elif "english" in text:
            speak("Language Change to English")
        elif "hindi" in text:
            speak("Language Change to Hindi")
            root.destroy()
            h.Widget()
        else:
            speak("Language Not Supported")
            self.changeLang()

    def assistant(self):
        while True:
            speak("What can i do for you?")
            self.compText.set("What can i do for you?")
            self.compText.set("okkkkk......")
            text = get_audio().lower()
            self.userText.set(text)
            if text == 0:
                continue
            elif "exit" in text or "bye" in text or "sleep" in text:
                self.compText.set("Ok bye")
                speak("Ok bye")
                exit()
                break
            elif 'what is my ip address' in text:
                speak("Just a minute...")
                ip_address = socket.gethostbyname(socket.gethostname())
                self.compText.set(ip_address)
                print(ip_address)
                speak(ip_address)
                break

            elif 'what is my mac address' in text:
                macaddress = getmac.get_mac_address()
                self.compText.set(macaddress)
                print(macaddress)
                speak(macaddress)
                break

            elif 'open youtube' in text:
                self.compText.set("opening youtube")
                speak("opening youtube")
                webbrowser.open("https://www.youtube.com")
                break

            elif 'open google' in text:
                self.compText.set("opening google")
                speak("opening google")
                webbrowser.open("https://www.google.com")
                break

            elif 'how do you manage everything' in text:
                self.compText.set("I can't show you my backprocess but in image i can show you")
                speak("I can't show you my backprocess but in image i can show you")
                ag_file = "ts1.gif"
                animation = pyglet.resource.animation(ag_file)
                sprite = pyglet.sprite.Sprite(animation)

                win = pyglet.window.Window(width=sprite.width, height=sprite.height)

                green = 0, 1, 0, 1
                pyglet.gl.glClearColor(*green)

                @win.event
                def on_draw():
                    win.clear()
                    sprite.draw()

                def on_close(event):
                    win.on_close()

                pyglet.clock.schedule_once(on_close, 8.0)
                pyglet.app.run()
                pyglet.app.exit()

                speak("In this way I manage everything with :)")
                break

            elif 'show me the analysis' in text:
                self.compText.set("Analyzing...")
                speak("Analyzing...")
                url = 'https://www.researchgate.net/publication/220355311_Unsupervised_Multilingual_Sentence_Boundary_Detection'
                article = Article(url)
                article.download()
                article.parse()
                # nltk.download('punkt')
                article.nlp()
                text = article.summary
                print(text)
                obj = TextBlob(text)
                sentiment = obj.sentiment.polarity
                ans = float('{0:.2g}'.format(sentiment * 100))
                speakData = str(ans) + '%'
                print(speakData)
                speak(speakData)
                if ans == 0:
                    self.compText.set('The text is neutral')
                    speak('The text is neutral')
                elif ans > 0:
                    self.compText.set('The text is positive')
                    speak('The text is positive')
                else:
                    self.compText.set('The text is negative')
                    speak('The text is negative')
                break

            elif 'open gmail' in text:
                self.compText.set("opening mail")
                speak("opening mail")
                webbrowser.open("https://mail.google.com//mail//u//0//?tab=km#inbox")
                break

            elif 'shutdown' in text:
                self.compText.set("Wait")
                shutdown()
                break

            elif 'open cmd' in text or 'open command prompt' in text:
                self.compText.set("opening command shell")
                speak("opening command shell")
                os.system("start cmd")
                break

            elif 'open notepad' in text:
                self.compText.set("opening pad...")
                speak("opening pad...")
                os.system("notepad.exe")
                break

            elif 'the time' in text:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                self.compText.set("Sir the time is" + strTime)
                speak("Sir the time is" + strTime)
                break

            elif 'open chrome' in text:
                self.compText.set("opening chrome")
                speak("opening chrome")
                webbrowser.open('https://www.google.com/chrome/')
                break

            elif 'hi how are you' in text:
                self.compText.set('Hey am all set to be your assistant')
                speak('Hey am all set to be your assistant')
                break

            elif 'What is your name ' in text:
                self.compText.set('I am Xicor...I am the high level project for university and college.')
                speak('I am Xicor...I am the high level project for university and college.')
                break

            elif 'click my picture' in text:
                self.compText.set('Working...')
                speak('working...')
                camera_port = 0

                ramp_frames = 1

                camera = cv2.VideoCapture(camera_port)

                def get_image():
                    retval, im = camera.read()
                    return im

                for i in range(ramp_frames):
                    temp = get_image()
                    speak("Taking image...")

                camera_capture = get_image()
                file = r"C:\Users\dell\OneDrive\Desktop\YourImg.jpg"

                cv2.imwrite(file, camera_capture)

                del (camera)
                speak("completed")
                break

            elif 'draw pie chart' in text:
                self.compText.set('Ok Creating....')
                speak('Ok Creating')
                activities = ['eat', 'sleep', 'work', 'play']
                slices = [3, 7, 8, 6]
                colors = ['r', 'y', 'g', 'b']
                plt.pie(slices, labels=activities, colors=colors,
                        startangle=90, shadow=True, explode=(0, 0, 0.1, 0),
                        radius=1.2, autopct='%1.1f%%')
                plt.legend()
                plt.show()
                break

            elif 'how is my voice' in text:
                speak("You just record it and listen by own")
                fs = 44100  # this is the frequency sampling; also: 4999, 64000
                seconds = 10  # Duration of recording

                myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
                print("Starting: Speak now!")
                sd.wait()  # Wait until recording is finished
                print("finished")
                write('output.mp4', fs, myrecording)  # Save as WAV file
                os.startfile("output.mp4")
                speak("Now listen and thought about it ")
                break

            elif 'draw bar graph' in text:
                self.compText.set('Ok ...')
                speak('Ok ...')
                x = [1, 2, 3]
                y = [2, 4, 1]
                plt.plot(x, y)
                plt.xlabel('x - axis')
                plt.ylabel('y - axis')
                plt.show()
                break

            elif 'go offline' in text:
                self.compText.set('Yups')
                gooffline()
                break

            elif 'open tutorialspoint' in text:
                self.compText.set("opening tutorialspoint")
                speak("opening tutorialspoint")
                webbrowser.open('https://www.tutorialspoint.com')
                break

            elif 'open geeksforgeeks' in text:
                self.compText.set("opening geeksforgeeks")
                speak("opening geeksforgeeks")
                webbrowser.open('https://www.geeksforgeeks.org')
                break

            elif 'open javatpoint' in text:
                self.compText.set("opening javatpoint")
                speak("opening javatpoint")
                webbrowser.open('https://www.javatpoint.com')
                break

            elif 'play online song ' in text:
                self.compText.set("playing song ...")
                speak("playing song ...")
                webbrowser.open('https://gaana.com/search/' + text)
                break

            elif 'play song' in text:
                speak("Which song u have to play ??")
                m = get_audio().lower()
                file = ('D:\\music\\')
                d = file + m + ".mp3"
                s = os.listdir(file)
                os.startfile(os.path.join(file, d))
                break

            elif 'open code' in text:
                self.compText.set("Wait")
                speak("Wait")
                codePath = "D:\Jarvis\check\JarvisEng1.txt"
                os.startfile(codePath)
                break

            elif 'youtube videos of' in text:
                self.compText.set("searching....")
                speak("searching....")
                webbrowser.open("http://www.youtube.com/results?search_query=" + text)
                break

            elif 'image of' in text:
                self.compText.set("Preparing...")
                speak("Preparing...")
                webbrowser.open("https://www.google.com/search?q=" + text)
                break

            elif 'pentagon' in text:
                self.compText.set("Making...")
                speak("Making...")
                colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
                t = turtle.Pen()
                turtle.bgcolor('black')
                t.hideturtle()
                t.speed(0)
                for x in range(360):
                    t.pencolor(colors[x % 6])
                    t.width(x / 100 + 1)
                    t.forward(x)
                    t.left(59)
                time.sleep(2)
                turtle.Screen().bye()
                break

            elif 'send email' in text:
                fromaddr = "zeeshaansiddique8@gmail.com"
                toaddr = "usmansiddique602@gmail.com"
                msg = MIMEMultipart()
                msg['From'] = fromaddr
                msg['To'] = toaddr
                speak("what will be the subject ?")
                msg['Subject'] = get_audio().lower()
                speak("what will be the body")
                body = get_audio().lower()
                msg.attach(MIMEText(body, 'plain'))
                speak("which file u want to send ?")
                filename = get_audio().lower()
                attachment = open("C:\\Users\\dell\\Downloads\\" + filename + ".docx", "rb")
                p = MIMEBase('application', 'octet-stream')
                p.set_payload((attachment).read())
                encoders.encode_base64(p)
                p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
                msg.attach(p)
                s = smtplib.SMTP('smtp.gmail.com', 587)
                s.starttls()
                s.login(fromaddr, "kinggoku")
                text = msg.as_string()
                s.sendmail(fromaddr, toaddr, text)
                print("sent")
                s.quit()
                break


            else:
                try:
                    try:
                        res = client.query(text)
                        output = next(res.results).text
                        self.compText.set(output)
                        print(output)
                        speak(output)
                        break
                    except:
                        results = wikipedia.summary(text, sentences=2)
                        self.compText.set('Got it.')
                        speak('Got it.')
                        self.compText.set('WIKIPEDIA says - ')
                        speak('WIKIPEDIA says - ')
                        speak(results)
                        break
                except:
                    webbrowser.open("https://www.google.com/search?q=" + text)
                    break


if __name__ == '__main__':
    greetMe()
    widget = Widget()
