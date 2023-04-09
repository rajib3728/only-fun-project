import pyjokes
import pyttsx3
import random

# using get_joke() to generate a single joke
#language is english
#category is neutral
My_joke = pyjokes.get_joke(language="en", category="neutral")
print(My_joke)
x=random.randint(0,1)
text_speech=pyttsx3.init()
voice = text_speech.getProperty('voices')
if x==0:
    text_speech.setProperty('voice', voice[0].id)
    text_speech.setProperty('rate',random.randint(100,200))
    text_speech.setProperty('volume',random.uniform(0.5,0.9))
    text_speech.say(My_joke)
else:
        #voice = text_speech.getProperty('voices') #get the available voices
    text_speech.setProperty('voice', voice[1].id)
    text_speech.setProperty('rate',random.randint(100,200))
    text_speech.setProperty('volume',random.uniform(0.5,0.9))
    text_speech.say(My_joke)
text_speech.runAndWait()