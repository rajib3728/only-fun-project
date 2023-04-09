import speech_recognition as sr
import pyaudio,socket
import pyttsx3
def test():
    try:
        socket.create_connection(("google.com",80))
        return True
    except OSError:
        return False
if test():
    a=sr.Recognizer()
    with sr.Microphone() as source:
        print("say something")
        audio=a.listen(source)
        try:
            text=a.recognize_google(audio)
            text_speech=pyttsx3.init()
            text_speech.say(text)
            text_speech.runAndWait()
        except:
            print("sorry could not recognize")
else:
    print("please check internert connection")