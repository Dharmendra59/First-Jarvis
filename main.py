import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia 
import requests
import json
import webbrowser
import os
import datetime
import pyautogui
import pywhatkit as kit
import time



engine = pyttsx3.init('sapi5')

voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
# print(voices[0].id)

author = "Mickey"
def speak(audio):
      engine.say(audio)
      engine.runAndWait()

def wishMe():
      hour = int(datetime.datetime.now().hour)

      if hour>=0 and hour<12:
            speak(f"Good Morning {author}")     
      elif hour>=12 and hour<18:
            speak(f"Good Afternoon {author}")           
      else:
            speak(f"Good Evening {author}")
      speak(f" Hello {author}, I am Zarvis. Please tell me how may I help you")


def takeCommand():
      r = sr.Recognizer()
      with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1.5
            audio = r.listen(source)

      try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")

      except Exception as e:
            # print(e)
            print("Sorry {author}, Say that again please...")
            return "None"
      return query

if __name__ == "__main__":
      # speak(f"Welcome {author}, I am Zarvis")
      wishMe()
      # takeCommand()
      if 1:
            query=takeCommand().lower()
            print(query)
            if 'wikipedia' and 'who' in query:
                  speak('Searching Wikipedia...')
                  query = query.replace("wikipedia", "")
                  results = wikipedia.summary(query, sentences=2)
                  speak("According to Wikipedia")
                  print(results)
                  speak(results)
                  
            elif 'news' in query:
                  speak('News Headlines')
                  query = query.replace("news", "")
                  url = "https://newsapi.org/v2/top-headlines?country=in&apiKey=a6ce67e0f29f48da9a08cb9a9888caa5"
                  news = requests.get(url).text
                  news_dict = json.loads(news)
                  art = news_dict['articles']
                  if art:
                        for article in art:
                              print(article['title'])
                              speak(article['title'])
                        
                              print(article['description'])
                              speak(article['description'])
                        
                              speak("Moving on to the next news")
                  else:
                        print("No articles found.")
                        speak("No articles found.")
                        
            elif 'open youtube' in query:
                  speak("Opening Youtube")
                  webbrowser.open("youtube.com")
            elif 'open google' in query:
                  speak("Opening Google")
                  webbrowser.open("google.com")
            elif 'search browser' in query:
                  speak("What should I search ?")
                  search = takeCommand().lower().replace("/", "")
                  speak(f"Searching {search}")                  
                  webbrowser.open(f"{search}")  
            elif 'ip address' in query:
                  ip = requests.get('https://api.ipify.org').text
                  print(f"Your IP address is {ip}")
                  speak(f"Your IP address is {ip}")
            elif 'open command prompt'and 'open cmd' in query:
                  speak("Opening Command Prompt")
                  os.system("start cmd")
            elif 'open notepad' in query:
                  speak("Opening Notepad")
                  os.system("start notepad")
            elif 'open calculator' in query:
                  speak("Opening Calculator")
                  os.system("start calc")
            elif 'open paint' in query:
                  speak("Opening Paint")
                  os.system("start mspaint")
            elif 'open word' in query:
                  speak("Opening Word")
                  os.system("start winword")
            elif 'open excel' in query:
                  speak("Opening Excel")
                  os.system("start excel")
            elif 'open powerpoint' in query:
                  speak("Opening Powerpoint")
                  os.system("start powerpnt")
            elif 'open chrome' in query:
                  speak("Opening Chrome")
                  os.system("start chrome")
            elif 'open code' in query:
                  speak("Opening Visual Studio Code")
                  os.system("start code")
            elif 'date' in query:
                  date = datetime.datetime.now().date()
                  print(f"Today's date is {date}")
                  speak(f"Today's date is {date}")
            elif 'time' in query:
                  time = datetime.datetime.now().strftime("%H:%M:%S")
                  print(f"The time is {time}")
                  speak(f"The time is {time}")
            elif 'play music' in query:
                  music_dir = "D:\\Song"
                  songs = os.listdir(music_dir)
                  print(songs)
                  os.startfile(os.path.join(music_dir, songs[0]))
            elif 'stop music' in query:
                  speak("Music stopped")  
                  os.system("TASKKILL /F /IM Media.exe")
            elif 'play youtube' in query:
                  speak("what should i search in youtube ?")
                  search = takeCommand().lower()
                  kit.playonyt(f"{search}")
            elif 'stop youtube' in query:
                  speak("youtube stopped")  
                  os.system("TASKKILL /F /IM chrome.exe")
            elif 'take screenshot' in query:
                  speak("Taking screenshot")
                  img = pyautogui.screenshot()
                  img.save("screenshot.png")
            elif 'send message' in query:
                  speak("Who do you want to send message ?")
                  number = input("Enter number : \n")
                  speak("What do you want to send?")
                  message = input("Enter Message : \n")
                  speak("Please Enter Time Sir.")
                  H = int(input("Enter Hours : ?\n"))
                  M = int(input("Enter Minutes : ?\n"))
                  kit.sendwhatmsg(f"+91{number}",message, H, M+1,5)