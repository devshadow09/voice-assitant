import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import wolframalpha as wolf
from googlesearch import search
listener = sr.Recognizer()
engine = pyttsx3.init()
wolf_id = "WXA8A7-H38W4TG8PJ"
client = wolf.Client(wolf_id)



name = input("Enter your name: ")

def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'robot' in command:
                command = command.replace('robot', '')
                print(command)
    except:
        print("error")
        pass
    return command


def run_robot():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)

    elif "search google" in command:
        question = command.replace("search google", "")
        search(question)
    elif "search" in command:
        replace = command.replace("search", "")
        res = client.query(replace)
        answer = next(res.results).text
        print(answer)
        talk(answer)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'give info on' in command:
        person = command.replace('give info on', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'hi' in command:
        talk("Hello " + name)
    elif "my name" in command:
        talk("I believe your name is " + name)
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk('Please say the command again.')


while True:
    run_robot()


#GUI
