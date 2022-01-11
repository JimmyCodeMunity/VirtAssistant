import pyttsx3
import sys
from tkinter import *
from tkinter.ttk import *
root = Tk()
root.geometry("550x250")
root.attributes('-fullscreen', True)


response = pyttsx3.init()
voices = response.getProperty('voices')
response.setProperty('voice', voices[1].id)

def getvals():
    response.say('listening')
    command = take_command()
    response.runAndWait()

Label(root, text="Ghost Assistant", font="ar 15 bold").pack(side= TOP, pady = 10)
Label(root,text="am here to help...kindly initialize me").pack(side = BOTTOM, pady = 10)

#submit data button
Button(root,text="Initialize Ghost",command=root.destroy).pack(side=TOP)




import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia


listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('listening....')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'ghost' in command:
                command = command.replace('ghost', '')

                print(command)
    except:
        pass
    return command

def run_ghost():
    command = take_command()
    if 'play' in command:
        print(command)
        song = command.replace('play','')
        pywhatkit.playonyt('playing...' +song)

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%H:%M %p')
        print(time)
        talk('current time is' +time)

    elif 'day' in command:
        print(command)
        talk(command)

    elif 'hey' in command:
        print('yes sir. How may i help you?')
        talk('yes sir.How may i help?')

    elif 'morning' in command:
        talk('morning too sir')

    elif 'who the hell is' in command:
        person = command.replace('who the hell is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)

    elif '' in command():
        print()



root.mainloop()
while True:
    run_ghost()
