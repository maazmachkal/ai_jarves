import pyaudio,os
import speech_recognition as sr

def excel():
        os.system("start excel.exe")

def internet():
        os.system("start chrome.exe")

def media():
        os.system("start wmplayer.exe")

def mainfunction(ads):
        user = r.recognize(ads)
        print(user)
        if user == "Excel":
                excel()
        elif user == "Internet":
                internet()
        elif user == "music":
                media()


r = sr.Recognizer()
with sr.Microphone() as source:
        print('lisy')
        audio = r.listen(source)

while 1:
        mainfunction(audio)