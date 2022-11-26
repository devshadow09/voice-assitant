import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import wolframalpha as wolf

listener = sr.Recognizer()
engine = pyttsx3.init()
wolf_id = "YOUR WOLFRAM ID" #app id from wolfram alpha
client = wolf.Client(wolf_id)



name = input("Enter your name: ") #your name of course

def talk(text): #text to speech engine
    engine.say(text)
    engine.runAndWait()


def take_command():
    try: #microphone
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'robot' in command:
                command = command.replace('robot', '')
                print(command)
    except: #mic error
        print("error")
        pass
    return command


def run_robot():
    command = take_command()
    print(command)
    if 'play' in command: #play a song
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)


    elif "search" in command: #requires wolfram app id to work
        replace = command.replace("search", "")
        res = client.query(replace)
        answer = next(res.results).text
        print(answer)
        talk(answer)
    elif 'time' in command: #tell the time
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'give info on' in command: #scour wikipedia
        person = command.replace('give info on', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'hi' in command: #say hi with name given at start of program
        talk("Hello " + name)
    elif "my name" in command: #says your name
        talk("I believe your name is " + name)
    elif 'joke' in command: #says a joke
        talk(pyjokes.get_joke())
    else: #inaudible/disturbance/unavailable command
        talk('Please say the command again.')


while True:
    run_robot()


#GUI
