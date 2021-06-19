import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import smtplib
import speedtest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager 
from selenium.webdriver.common.keys import Keys
import time
import wolframalpha
import requests
import pyjokes
from bs4 import BeautifulSoup
from config import Chrome_Profile_Path
from config import Chrome_Profile_Path_1
from GoogleNews import GoogleNews

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)

engine.setProperty('voices',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
   


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good Morning!")

    elif hour>=12 and hour<=16:
        speak("Good Afternoon")

    elif hour>=16 and hour<=20:
        speak("Good Evening")   

    else:
        speak("Good Night")  

    speak("I am Suzi Sir. Please tell me how may i help you")                  

def voiceInput():
    #it takes microphone input from the user and returns string output
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....") 
        r.pause_threshold = 1
        #r.energy_threshold = 200
        audio = r.listen(source)

        try:
            print("Recognizing....")
            query = r.recognize_google(audio,language='en-in')
            print(f"User said: {query}\n")

        except Exception as e:
            print(e)
            speak("Say that again please.....")
            print("Say that again please.....")
            return "None"
        return query        

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('rahulguddu36@gmail.com', password)
    server.sendmail('rahulguddu36@gmail.com', to, content)
    server.close()

f = open('password.txt')
password = f.read()
f.close()    
p = open("Fb_password.txt")
enter = p.read()
p.close()

if __name__ == "__main__":
    wishMe()    
    while True:
        query = voiceInput().lower()

    #logic for executing tasks based on query
        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=3)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            speak("Opening youtube")
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak(" Sure Sir, what should i search on google")
            cn = voiceInput().lower()
            webbrowser.open(f"{cn}")  
            time.sleep(15)

        elif 'open gmail' in query:
            speak("Opening gmail")
            webbrowser.open("gmail.com") 

        elif 'open stack overflow' in query:
            speak("Opening stack overflow")
            webbrowser.open("stackoverflow.com") 
        
        elif 'open facebook' in query:
            speak("Ok sir Opening Facebook")
            driver = webdriver.Chrome("C:\\Users\\Rahul\\Downloads\\chromedriver_win32\\chromedriver.exe")
            # Go to the Facebook URL
            driver.get("http://www.facebook.com")
            email= driver.find_element_by_id('email')
            email.send_keys("8804605979")
            password = driver.find_element_by_id('pass')
            password.send_keys(enter)
            Login = driver.find_element_by_xpath("//button[@value='1' and @class='_42ft _4jy0 _6lth _4jy6 _4jy1 selected _51sy']")
            Login.submit() 
            time.sleep(15)
            driver.quit()

        elif 'open whatsapp' in query:
            speak("Ok sir Opening Whatsapp")
            options = webdriver.ChromeOptions()
            options.add_argument(Chrome_Profile_Path)
            driver = webdriver.Chrome("C:\\Users\\Rahul\\Downloads\\chromedriver_win32\\chromedriver.exe",options = options) 
            driver.get("https://web.whatsapp.com")
            
            time.sleep(15)
            driver.quit()
        
        elif 'open linkedin' in query:
            speak("Ok sir Opening LinkedIn")
            options = webdriver.ChromeOptions()
            options.add_argument(Chrome_Profile_Path_1)
            driver = webdriver.Chrome("C:\\Users\\Rahul\\Downloads\\chromedriver_win32\\chromedriver.exe",options = options)
            driver.get("https://www.linkedin.com")

            time.sleep(15)
            driver.quit()

        elif 'play music' in query: 
            music_dir = 'C:\\Users\\Rahul\\Music\\Songs'
            songs = os.listdir(music_dir)
            print(songs)
            d = random.randint(0,26)
            os.startfile(os.path.join(music_dir,songs[d])) 

            time.sleep(30)    

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is : {strTime}")    
            
        elif 'open code' in query:
            code_path = "C:\\Users\\Rahul\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe" 
            os.startfile(code_path)   

        elif 'email to rahul' in query:
            try:
                speak("What should I say,Sir")  
                content = voiceInput()
                to = "rahulguddu35@gmail.com"
                a = sendEmail(to,content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry Rahul Sir, I am not able to send this email because your less accessing feature icon  is not open") 

        elif 'tell me about yourself' in query:
            s = 'Hello Sir I am Suzy. I am your AI Personal Assistant. I can look up answers for you, or help you find the quickest way home. If you need anything just ask, your wish is my command '      
            print(s)
            speak(s)

        elif 'quit' in query:
            speak("Exiting from the code, Thankyou sir!.Have a nice day") 

            exit()   
        
        elif 'news' in query:
            googlenews = GoogleNews()
            googlenews = GoogleNews('en','d')
            googlenews.search('India')
            googlenews.getpage(1)
            googlenews.result()
            speak("According To Google")
            print(googlenews.gettext())
            speak(googlenews.gettext())
            
        elif 'search' in query:
            query = query.replace("search","")
            speak("Searching Sir....")
            webbrowser.open(query)
            time.sleep(10) 

        elif 'temperature' in query:
            search = "temperature in bolpur"
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text,"html.parser")
            temp = data.find("div",class_="BNeawe").text
            print(f"current {search} is {temp}")
            speak(f"current {search} is {temp}")    

        elif 'make a note' in query:
            speak("What should i note sir")
            note = voiceInput()
            remember = open("data.txt",'w')
            remember.write(note)
            remember.close()
            speak("I have noted that" + note)

        elif 'remind' in query:
            remember = open("data.txt", 'r').read()
            print(remember)
            speak("Yes Sir, You told me to remember that" + remember)    
        
        elif 'joke' in query:
            speak("Here your joke sir")
            my_jokes = pyjokes.get_joke('en',category='neutral')
            print(my_jokes)
            speak(my_jokes)
            speak(" Haha Hihi ")
            
        elif 'thank you' in query:
            speak("It's my pleasure Sir. I am always there to help you with my best efforts") 
            speak("Anything more Sir") 

        elif 'internet speed' in query:
            st = speedtest.Speedtest()
            d1 = st.download()
            up = st.upload()
            print(f"Sir we have {d1} bit per second downloading speed and {up} bit per second uploading speed")     
            speak(f"Sir we have {d1} bit per second downloading speed and {up} bit per second uploading speed")                                   




           

        
