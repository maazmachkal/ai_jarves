import pyttsx3
import datetime
import speech_recognition as sr


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voices',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if (hour <= 6):
        speak('Hii maaz, You are still awake !!!!, What i can do for you')
    elif (hour > 6 and hour <= 13):
        speak('Good morning maaz, What i can do for you')
        speak('Good morning maaz, Command Me')
    elif (hour > 13 and hour <= 17):
        speak('good afternoon maaz, what i can do for you')
    elif (hour > 17 and hour <= 24):
        speak('good evening maaz, what i can do for you')

def take():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('lisining  ....')
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print('recognising...')
        quiry = r.recognize_google(audio, language='en-in')
        #speak(f"you said {quiry}")
        print(quiry)
    except:
        pass





if __name__ == "__main__":
    #peak('maaz    hiii hello')
    wishMe()
    take()

