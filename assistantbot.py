
import os
import pygame
import tempfile
import time
from gtts import gTTS
import speech_recognition as sr
import playsound


#convert text to speech
def ava_listen():
    #create recognizer
    r = sr.Recognizer()
    #what microphone to use
    with sr.Microphone(device_index=0) as source:
        r.adjust_for_ambient_noise(source)
        print("Listening...")
        r.pause_threshold = 1
        #listen to microphone
        audio = r.listen(source)
        text = ''
    try:
        text = r.recognize_google(audio)
        
    except sr.RequestError as re:
        print(re)
        print("Sorry, I encountered an error. Please try again.")
    except sr.UnknownValueError as uve:
        print(uve)
        print("Sorry, I couldn't understand. Please try again.")
    except sr.WaitTimeoutError as wte:
        print(wte)
        print("Sorry, the operation timed out. Please try again.")
    text = text.lower()
    return text

#convert text to speech
def ava_speak(text):
    temp = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
    file_name = temp.name
    tts = gTTS(text=text, lang='en')
    temp.close()
    tts.save(file_name)
    playsound.playsound(file_name)
    os.remove(file_name)

    
    #you can #playsound.playsound(file.name) and use pygam mixer to play the sound just remove the # from the code below 
    
    #pygame.mixer.init()
    #pygame.mixer.music.load(temp.name)
    #print(text)
    #while pygame.mixer.music.get_busy(): 
        #pygame.time.Clock().tick(10)
    #pygame.mixer.quit()
    


#creat a function to reply based on input text
def ava_reply(text):
    if 'what' in text and 'name' in text:
        ava_speak("My name is Ava. I am your personal assistant.")
    elif 'why' in text and 'exist' in text:
        ava_speak("I was created to work for you. I don't need a break and I will not ask for a day off.")
    elif 'when' in text and 'exist' in text:
        ava_speak("I was created in 2023 to help you with your daily tasks.")
    elif 'when' in text and 'sleep' in text:
        ava_speak("I don't need to sleep. I am an AI assistant.")
    elif 'how are you' in text:
        ava_speak("I am fine. Thank you for asking.")
    elif 'stop' in text:
        ava_speak("It was a pleasure to help you. I wish you a wonderful day!")
        return False
    else:
        ava_speak("Excuse me, I did not get that. Can you please repeat?")

def execute_assistant():
    ava_speak("Hello, I am Ava at your service. Can you tell me your name?")
    listen_ava = ava_listen()
    ava_speak('Hello ' + listen_ava + 'How can I help you?')

    while True:
        listen_ava = ava_listen()
        print(listen_ava)
        ava_reply(listen_ava)



        # if we we use the 'stop' keyword,we want to end the lwhile loop and assistant should say goodbye
        if 'stop' in listen_ava:
            break
#call function
execute_assistant()

