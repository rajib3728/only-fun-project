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

Hey, ladies drop it down
Just want to see you touch the ground
Don't be shy girl go bananza (hey girl)
Shake ya body like a belly dancer
Yo, excuse me, beg your pardon girl
Do you have any idea what you starting girl
You got me tingiling, come to me mingiling
Steppin' off lookin' bootylicious and jingiling
When you walk, I see it baby girl
When you talk, I believe it baby girl
I like that, thick-petite n' pretty
Little touch is a ditty
Love to work the kitty like purrrrrrr
She loves to stirr it up, purrrrrr
I can hear her purring up
'Cause she's the type that'll get arousy up
Get you excited and call her boyfriend up (ohh)
What's the plan without the plan B
We can meet up at the hutter house for the t.v
So stand by like a butty pass
While I watch this beautiful thing shake that ass
Hey ladies, drop it down
Just want to see you touch the ground
Don't be shy girl go bananza
Shake ya body like a belly dancer
Hey ladies, drop it down
Just want to see you touch the ground
Don't be shy girl go bananza
Shake ya body like a belly dancer
Girl, I must say you the flyest thang in here
You're so hot we gon' need some rain in here
Type to make ex-gangstas bang in here
Girl, you could do anything you want in here
Clown if you want to, frown if you want to
You ain't even gotta drop down if you want to
'Cause I'd rather see you shake it standin'
Either way you do it, girl you look outstandin (uh-huh)
And now you got me spending (uh-huh)
The way you got that body bendin' (uh-huh)
An ass like that girl you gotta be kickin'
Had me goin' to church, next day repentant
Lap dancing for my FA crew
Slide it over to boo 'cause he want some too
Up in the VIP with no fee
Blessing you with the G even though we gettin' it free so
Hey ladies, drop it down
Just want to see you touch the ground
Don't be shy girl go bananza
Shake ya body like a belly dancer
Hey ladies, drop it down
Just want to see you touch the ground
Don't be shy girl go bananza
Shake ya body like a belly dancer
Girl, shake ya body-body
With somebody-body
Whatever you do don't break your body, body
After the party-party
Grab a hottie-hottie
In the back seat of your Maseratti-ratti
Jiggle-jiggle it to the left (ah ah ah)
Jiggle-jiggle it to the right (ah ah ah)
Jiggle it to the front, then jiggle it to the back
And jiggle -iggle it all-all night (ah ah ah)
Hey ladies, drop it down
Just want to see you touch the ground
Don't be shy girl go bananza
Shake ya body like a belly dancer
Hey ladies, drop it down
Just want to see you touch the ground
Don't be shy girl go bananza
Shake ya body like a belly dancer
Hey ladies, drop it down
Just want to see you touch the ground
Don't be shy girl go bananza
Shake ya body like a belly dancer
Hey ladies, drop it down
Just want to see you touch the ground
Don't be shy girl go bananza
Shake ya body like a belly dancer
Hey ladies, drop it down
Just want to see you touch the ground
Don't be shy girl go bananza
Shake ya body like a belly dancer
Hey ladies, drop it down
Just want to see you touch the ground
Don't be shy girl go bananza
Shake ya body like belly dancer
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
