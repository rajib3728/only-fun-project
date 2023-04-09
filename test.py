import pyttsx3
import random

''''text_speech=pyttsx3.init()
text_speech.setProperty('voice', 'english_rp+f4')
text_speech.say(a)
text_speech.runAndWait()

def voiceChange():
    eng = pyttsx3.init() #initialize an instance
    voice = eng.getProperty('voices') #get the available voices
    # eng.setProperty('voice', voice[0].id) #set the voice to index 0 for male voice
    eng.setProperty('voice', voice[1].id) #changing voice to index 1 for female voice
    eng.say(a) #say method for passing text to be spoken
    eng.runAndWait() #run and process the voice command
if __name__ == "__main__":
    voiceChange()'''
a='''hey lady drop it down 
i wanna see you touch the ground
don't be shy girl bopananza
shake your body like belley dancer
'''
f=a.split("\n")
for i in range(len(f)):
    x=random.randint(0,1)
    text_speech=pyttsx3.init()
    voice = text_speech.getProperty('voices')
    if x==0:
        text_speech.setProperty('voice', voice[0].id)
        text_speech.setProperty('rate',random.randint(100,200))
        text_speech.setProperty('volume',random.uniform(0.5,0.9))
        text_speech.say(f[i])
    else:
        #voice = text_speech.getProperty('voices') #get the available voices
        text_speech.setProperty('voice', voice[1].id)
        text_speech.setProperty('rate',random.randint(100,200))
        text_speech.setProperty('volume',random.uniform(0.5,0.9))
        text_speech.say(f[i])
    text_speech.runAndWait()
#print(a.split("\n"))