import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print("listening")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if "alexa" in command:
                command = command.replace("alexa", "")
                print(command)
    except:
        pass
    return command

def run_alexa():
    command = take_command()
    print(command)
    if "play" in command:
        song = command.replace("play", "")
        talk("playing" + song)
        pywhatkit.playonyt(song, use_api=True)

    elif "time" in command:
        time = datetime.datetime.now().strftime("%H:%M")
        print(time)
        talk("current time is " + time)

    elif "wikipedia" in command:
        wiki = command.replace("wikipedia", "")
        info = wikipedia.summary(wiki, 1)
        print(info)
        talk(info)

    elif "search" in command:
        search = command.replace("search", "")
        info = pywhatkit.search(search)
        print(info)
        talk(info)



    else:
        talk("please say the command again")


run_alexa()