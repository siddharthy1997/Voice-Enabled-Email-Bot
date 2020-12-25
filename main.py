import smtplib
import speech_recognition as sr
import pyttsx3
from email.message import EmailMessage
listener = sr.Recognizer()
engine = pyttsx3.init()

def talk(text):
    engine.say(text)
    engine.runAndWait()
def get_message_info():
    try:
        with sr.Microphone() as source:
            print('I am Listening.......')
            voice = listener.record(source, duration=20)
            info = listener.recognize_google(voice,language="en-IN")
            print(info)
            return info.lower()
    except:
        pass

def get_info():
    try:
        with sr.Microphone() as source:
            print('I am Listening.......')
            voice = listener.record(source, duration=5)
            info = listener.recognize_google(voice,language="en-IN")
            print(info)
            return info.lower()
    except:
        pass

def send_email(receiver,subject,message):
    server = smtplib.SMTP('SMTP.gmail.com', 587)
    server.starttls()
    server.login('siddharth.y225990@gmail.com','#Yadav145')
    email = EmailMessage()
    email['From'] = 'siddharth.y225990@gmail.com'
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content(message)
    server.send_message(email)

email_list = {
    'sunny' : 'ay225990@gmail.com',
    'subhash' : 'yadavsubhash145@gmail.com'
}
def get_email_info():
    talk('To Whom you want to send email?')
    name = get_info()
    receiver = email_list[name]
    print(receiver)
    talk('What is the subject of your email?')
    subject = get_info()
    talk('What is the message of your email?')
    message = get_message_info()
    send_email(receiver,subject,message)
    talk('Your email has been sent')
    talk('Do you want to send more email?')
    send_more = get_info()
    if 'yes' in send_more:
        get_email_info()

get_email_info()
