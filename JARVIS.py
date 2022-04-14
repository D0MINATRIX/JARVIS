import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import sys
import webbrowser
from datetime import date

engine=pyttsx3.init()
engine.setProperty("rate",150)
voices=engine.getProperty("voices")
engine.setProperty('voice',voices[0].id)
recognizer=sr.Recognizer()

def engine_talk(text):
  engine.say(text)
  engine.runAndWait()

def run_jarvis():
  with sr.Microphone() as source:
    recognizer.adjust_for_ambient_noise(source,duration=1)
    print('\n')
    print('Start Speaking !!')
    engine_talk('listening...')
    recordedaudio=recognizer.listen(source)

  try:
    command=recognizer.recognize_google(recordedaudio,language='en-in')
    command=command.lower()
    
    if 'jarvis' in command:
      command=command.replace('jarvis','')
      print('You said',command)
    else:
      print('You said',command)

    if 'hello' in command:
      print('Hello, How can I help you ?')
      engine_talk('hello, how can i help you ?')

    elif 'who are you' in command:
      print('I am JARVIS a k a your virtual assistant')
      engine_talk('I am jarvis a k a your virtual assistant. how can i help you ?')

    elif 'can you do' in command:
      print('''I can play songs on youtube, tell you a joke, search on wikipedia, tell date and time, find your location, locate area on map, open different websites like instagram, youtube, gmail, github, stackoverflow and searches on google. How may i help you ?''')
      engine_talk('''i can play songs on youtube, tell you a joke, search on wikipedia, tell date and time, find your location, locate area on map, open different websites like instagram, youtube, gmail, github, stackoverflow and searches on google. How may i help you ?''')
    
    elif 'play' in command:
      song=command.replace('play','')
      print('Playing'+song)
      engine_talk('playing'+song)
      pywhatkit.playonyt(song)

    elif 'date and time' in command:
      today=date.today().strftime('%B %d %Y')
      time=datetime.datetime.now.strftime('%I:%M %p')
      print("Today's date is",today,'and current time is',time)
      engine_talk("today is"+today)
      engine_talk('and current time is'+time)
    elif 'time and date' in command:
      today=date.today().strftime('%B %d %Y')
      time=datetime.datetime.now.strftime('%I:%M %p')
      print('Current time is',time,"and today's date is",today)
      engine_talk('Current time is'+time)
      engine_talk(" and today is"+today)
    elif 'time' in command:
      time=datetime.datetime.now.strftime('%I:%M %p')
      print('The current time is'+time)
      engine_talk('the current time is')
      engine_talk(time)
    elif 'date' in command:
      today=date.today()
      print("Today's date :",today)
      d2=today.strftime('%B %d %Y')
      print("Today's date is ",d2)
      engine_talk('todays date is')
      engine_talk(d2)

    elif 'tell me about' in command:
      name=command.replace('tell me about','')
      info=wikipedia.summary(name,1)
      print(info)
      engine_talk(info)
    elif 'wikipedia' in command:
      name=command.replace('wikipedia','')
      info=wikipedia.summary(name,1)
      print(info)
      engine_talk(info)
    elif 'who is' in command:
      name=command.replace('who is','')
      info=wikipedia.summary(name,1)
      print(info)
      engine_talk(info)

    elif 'what is' in command:
      search="https://www.google.com/search?q="+command
      print('Here is what i found on the internet')
      engine_talk('searching... here is what i found on the internet...')
      webbrowser.open(search)
    elif 'search' in command:
      search="https://www.google.com/search?q="+command.replace('search','')
      print('Searching...')
      engine_talk('searching')
      webbrowser.open(search)

    elif 'joke' in command:
      _joke=pyjokes.get_joke()
      print(_joke)
      engine_talk(_joke)

    elif 'my location' in command:
      url="htps://www.google.com/maps/search/Where+am+I+?/"
      webbrowser.get().open(url)
      engine_talk('you must be somewhere near here as per google maps')
    elif 'locate' in command:
      print('Locating...')
      engine_talk('locating...')
      location=command.replace('locate','')
      if 'on map' in location:
        location=location.replace('on map','')
      url = 'https://google.nl/maps/place/'+location+'/&amp;'
      webbrowser.get().open(url)
      print('Here is location of'+location)
      engine_talk('here is the location of'+location)
    elif 'location of' in command:
      print('Locating...')
      engine_talk('locating...')
      location=command.replace('find location of','')
      url = 'https://google.nl/maps/place/'+location+'/&amp;'
      webbrowser.get().open(url)
      print('Here is location of'+location)
      engine_talk('here is the location of'+location)
    elif 'where is' in command:
      print('Locating...')
      engine_talk('locating...')
      location=command.replace('where is','')
      url = 'https://google.nl/maps/place/'+location+'/&amp;'
      webbrowser.get().open(url)
      print('Here is location of'+location)
      engine_talk('here is the location of'+location)

    elif 'open' in command:
      site=command.replace('open','')
      url="https://www."+site
      url=url+".com/"
      print('Opening',site)
      engine_talk('opening'+site)
      webbrowser.open_new(url)

    elif 'thank you' in command:
      print("You're Welcome")
      engine_talk("you're welcome")
    
    elif 'bye' in command:
      print('Good Bye, Have a nice day!!')
      engine_talk('good bye, have a nice day!')
      sys.exit()
    elif 'tata' in command:
      print('Good Bye, Have a nice day!!')
      engine_talk('good bye, have a nice day!')
      sys.exit()
    elif 'stop' in command:
      print('Good Bye, Have a nice day!!')
      engine_talk('good bye, have a nice day!')
      sys.exit()

    else:
      print('Here is what I found on the internet...')
      engine_talk('here is what i found on the internet')
      search="htps://www.google.com/search?q="+command
      webbrowser.open(search)

  except Exception as ex:
    print(ex)

print('Clearing background noise... Please wait')
engine_talk('clearing background noise please wait')
print('\n')
print('Hello, I am JARVIS. How can I help you?')
engine_talk('hello, i am jarvis how can i help you?')

while True:
  run_jarvis()
