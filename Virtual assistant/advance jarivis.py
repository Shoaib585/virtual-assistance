import time #pip install time
import  pyjokes #pip install pyjokes
import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install SpeechRecognition
import os #pip install os
import datetime #pip install datetime
# pip install opencv-contrib-python
import cv2 #pip install open-cv
import random #pip install random
from requests import get #pip install requests
import wikipedia #pip install wikipedia
import webbrowser #pip install webbrowser
import pywhatkit as kit #pip install pywhatkit
import smtplib #pip install smtplib
import sys #pip install sys
import  pyautogui #pip install pyautogui
import requests #pip install requests
import instaloader #pip install instaloader
import instadownloader #pip install instadownloader
import PyPDF2 #pip install PyPDF2  
import oprator #pip install operator
from bs4 import BeautifulSoup #pip install beautifulsoup4
from pywikihow import search_wikihow #pip install pywikihow
import psutil #pip install psutil
import speedtest #pip install speedtest-cli
import numpy #pip install numpy

# pip install twilio
# import pyaudio as audio
# Initialize the Text-to-Speech engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
default_voice = 1
engine.setProperty('voices', voices[default_voice].id)
print(voices[1].id)
#  speed manage
# engine.setProperty('rate',170)


# Text-to-Speech Function
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


# Convert Voice to Text
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1  # Corrected typo
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}")
    except Exception as e:
        # speak("Say that again, please.")
        return "none"
    query= query.lower()
    return query


# To Wish
def wish():
    hour = int(datetime.datetime.now().hour)
    tt =time.strftime("%I:%M:%p")
    if hour >= 0 and hour < 12:
        speak(f"Good Morning! its {tt}")
    elif hour >= 12 and hour < 18:
        speak(f"Good Afternoon! its {tt}")
    else:
        speak(f"Good Evening! its {tt}")
    speak("I am Jarvis Sir. Please tell me how I can help you.")


# Send Email
def sendEmail(to, content):
    EMAIL = os.environ.get("EMAIL")  # Use environment variables
    PASSWORD = os.environ.get("PASSWORD")
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(EMAIL, PASSWORD)
    server.sendmail(EMAIL, to, content)
    server.close()

# Function to Fetch and Speak News
def news():
        # News API URL (TechCrunch)
        main_url = "https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=4e7a48cae54b44b9b1b7515c00138aad"
        
        # Fetch news data
        main_page = requests.get(main_url).json()
        
        # Extract articles
        articles = main_page["articles"]
        
        # Prepare news headlines
        head = []
        day = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth"]

        # Loop through available articles and speak headlines
        for i, ar in enumerate(articles[:10]):  # Limit to 10 articles
            head.append(ar["title"])
            speak(f"Today's {day[i]} news is: {head[i]}")
# pdf reader
def pdf_reader():
    book=open('py3.pdf','rb')
    pdfReader=PyPDF2.PdfFileReader(book) #pip install PyPDF2
    pages=pdfReader.numPages
    speak(f"Total numbers of pages in this books{pages}")
    speak("Sir please enter the page number i have read")
    pg=int(input("please enter the page number::"))
    page=pdfReader.getPage(pg)
    text = page.extract_text()
    speak(text)

def TaskExecution():
    pyautogui.press('ese')
    speak("verification Succesfull")
    speak("welcome back to shoaib sir")
    wish()
    while True:  # Continuous listening loop
        query = takecommand().lower()

        # Task logic
        if 'open notepad' in query:
            path = "C:\\WINDOWS\\system32\\notepad.exe"
            os.startfile(path)
        elif 'open command prompt' in query:
            os.system("start cmd")
        elif 'open camera' in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('Webcam', img)
                k = cv2.waitKey(50)
                if k == 27:  # Press 'Esc' to exit
                    break
            cap.release()
            cv2.destroyAllWindows()
        elif "play music" in query:
            music_dir = "E:\\Video\\audios\\"  # Set your music directory
            songs = os.listdir(music_dir)
            for song in songs:
                if song.endswith('.mp3'):
                    os.startfile(os.path.join(music_dir, song))
        elif "ip address" in query:
            ip = get('https://api.ipify.org').text
            speak(f"Your IP address is {ip}")
        elif 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak(results)
            print(results)
        elif 'open youtube' in query:
            webbrowser.open('youtube.com')
        elif 'open instagram' in query:
            webbrowser.open('instagram.com')
        elif 'open google' in query:
            speak("Sir, what should I search on Google?")
            cm = takecommand().lower()
            webbrowser.open(f"https://www.google.com/search?q={cm}")
        elif 'send message' in query:
            kit.sendwhatmsg("+92309600303", "I am testing here", 2, 25)
        elif 'play song on YouTube' in query or 'YouTube song' in query:
            takecommand().lower()
            kit.playonyt("295")
        elif 'email to shoaib' in query:
            try:
                speak("What should I say?")
                content = takecommand().lower()
                to = "malikshoaibsfnan@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent.")
            except Exception as e:
                print(e)
                speak("Sorry Sir, I am not able to send this email.")
        elif 'no thanks' in query:
            speak("Thanks for using me, Sir. Have a good day!")
            break
            
            # close any application
        elif 'close notepad'in query:
            speak("okay sir, closing notepad")
            os.system("taskkill /f /im notepad.exe")
        #     close command prompt
        elif 'close command prompt'in query:
            speak("okay sir , closing command prompt")
            os.system("taskkill /f /im cmd.exe")
        elif 'chat GPT'in query:
            speak("okay sir , opening ")
            webbrowser.open('chatgpt.com')
        elif 'you can sleep' in query:
            speak("okay sir , i am going to sleep you can call anytime")
            break
        #     set to alarm
        elif 'set alarm' in query:
            speak("Sir please tell me the time to set alarm. for , set alarm to 5:30 a.m")
            tt = takecommand()
            tt = tt.replace("set alarm to", "")  # set alarm to 5:30 a.m
            tt= tt.replace(".","") # 5:30 a.m
            tt=tt.upper() #5:30 AM
            # pip install soundplay
            import MyAlarm
            MyAlarm.alarm(tt)

            
        #         to find jokes
        elif 'tell me a joke' in query:
            joke=pyjokes.get_joke()
            speak(joke)
        #     shutdwon system
        elif'shutdown the system'in query:
            os.system("shutdown /s /t 1")
        #     restart system
        elif'restart the system'in query:
            os.system("restart/r /t 1")
        #     switch the window
        elif 'switch the window'in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")
        #  to check instagram profile check
        elif'instagram profile'in query or 'profile on instagram'in query:

            speak("Sir please enter the user name correctly.")
            name = input("Enter user name here:")
            webbrowser.open(f'instagram.com/{name}')
            speak(f"Sir here the profile of the user{name}")
            time.sleep(5)
            speak("Sir would you like to download profile picture of this account")
            condition = takecommand().lower()
            if"yes" in condition:
                mod = instaloader.instaloader() #pip install instadownloader
                mod.download_profile(name, profile_pic_only=True)
                speak("i am done sir, profile is saved in our main folder . now i am raedy")
        # news
        elif'tell me news'in query:
            speak("Please wait sir, feteching the latest news")
            news()
        # To find my location using IP address
        elif 'where I am 'in query or 'where we are'in query:
            speak("wait sir , let me check")
            try:
                # Get the public IP address
                
                ip_address = requests.get('https://api.ipify.org').text
                print(f"Your IP address is: {ip_address}")
                # Use ipinfo.io for geolocation data
                url = f'https://ipinfo.io/{ip_address}/json'
                response = requests.get(url).json()
                # Extract location details
                city, country = response.get('city', 'Unknown City'), response.get('country', 'Unknown Country')
                # Output the result
                speak(f"Based on your IP address, you are in {city}, {country}.")
            except Exception as e:
                speak(f"Sorry, there was an error: {e}")
        # take a screenshot
        elif'take screenshot'in query or 'take a screenshot'in query:
            speak("Sir, Please tell me the name for this screenshot file")
            name=takecommand().lower()
            speak("please sir hold the screen for few second, i am taking screenshot")
            time.sleep(3)
            img=pyautogui.screenshot()
            img.save(f"{name}.png")
            speak("i am done sir, the screenshot is saved in our main folder. now i am ready for next command")
        # to read a pdf
        elif 'read pdf'in query:
            pdf_reader()
        #  hide files and folder
        elif'hide all files'in query or 'hide this folder'in query or 'visible for everyone'in query:
            speak("sir please tell me you want to hide this folder or make it visible for everyone")
            condition = takecommand().lower()
            if "hide"in condition:
                os.system("attrib +h /s /d") #os module
                speak("sir, all the files in this folder are now hidden,")
            elif "visible" in condition:
                os.system("attrib -h /s /d")
                speak("sir, all the files in this folder are now visible to everyone")
            elif"leave it"in condition or "leave for now" in condition:
                speak("ok sir")
        #  Tempreature
        elif "today weather" in query:
            search="temperature near me"
            url =f"https://www.google.com/search?q={search}"
            r=requests.get(url)
            data =BeautifulSoup(r.text, "html.parser")
            temp = data.find("div", class_="BNeawe iBp4i AP7Wnd").text
            speak(f"Current temperature near you is {temp}")
        
        # internet speed
        elif "internet speed"in query:
            # st=speedtest.Speedtest()
            # dl = st.download()
            # up = st.upload()
            # speak(f"sir we have {dl} bit per second downloading speed and {up} bit per second uploading speed")

            try:
                os.system('cmd /k "speedtest"')
            except:
                speak("there is no internet connection")

        elif "volume up"in query:
            speak("ok sir volume up only 2 point")
            pyautogui.press("volumeup")
        
        elif "volume down"in query:
            speak("ok sir volume down 2 point")
            pyautogui.press("volumemute")
        
        elif "volume mute"in query:
            speak("ok sir volume is mute know")
            pyautogui.press("volumemute")
        

           
        # cooking 
        elif"activate how to do mod"in query:
            # from pywikihow import search_wikihow
            speak("How to do mode is activate")
            while True:
                speak("Please tell me what you want to know")
                how = takecommand()
                try:
                    if"exit"in how or "close"in how:
                        speak("okay sir , how to do mode closed")
                        break
                    else:
                     max_result= 1
                     how_to = search_wikihow(how,max_result)
                     assert len(how_to) == 1
                     how_to[0].print()
                     speak(how_to[0].summary)
                except Exception as e:
                    speak("sorry sir, i am not able to find this")
        #  power battrey
        elif "how much power left"in query or "how much power we have"in query or "battery"in query:
            battery = psutil.sensors_battery()
            percentage=battery.percent
            speak(f"sir our system here {percentage} percent battery")
            if percentage>=75:
                speak("we have enough power to continue our work")
            elif percentage>=40 and percentage<=75:
                speak("we should connect our system to charging point to charge our battery")
            elif percentage<=15 and percentage<=30:
                speak("we don't have enough power to work connect to charging")
            elif percentage<=15:
                speak("we have low power, please connect to charging the system will shutdown very soon")
        # calculation 
        elif ' do some calculations'in query or "can you calculate" in query or"calculate" in query:
            try:
             r=sr.Recognizer()
             with sr.Microphone() as source:
                speak("Say what you want to calculate , example 3 plus 3")
                print("listening....")
                r.adjust_for_ambient_noise(source)
                audio = r.listen(source)
             my_string=r.recognize_google(audio)
             print(my_string)
             def get_opreator_fn(op):
                return {
                    '+' : oprator.add,
                    '-' : oprator.div,
                    'x' : oprator.mul,
                    'divided' : oprator.divide,
                }[op]
             def eval_binary_expr(op1, oper, op2):
                op1,op2=int(op2),int(op2)
                return get_opreator_fn(oper)(op1, op2)
             speak("your result is")
             speak(eval_binary_expr(*(my_string.split())))
            except Exception as e:
                speak("it does not understand")
        # speak("Sir, do you have any other work?")
# Main Functionality
if __name__ == "__main__":
    import cv2
import os
recognizer = cv2.face.LBPHFaceRecognizer_create() # Local Binary Patterns Histograms
recognizer.read('trainer/trainer.yml')   #load trained model
cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath) #initializing haar cascade for object detection approach

font = cv2.FONT_HERSHEY_SIMPLEX #denotes the font type


id = 2 #number of persons you want to Recognize


names = ['','avi']  #names, leave first empty bcz counter starts from 0


cam = cv2.VideoCapture(0, cv2.CAP_DSHOW) #cv2.CAP_DSHOW to remove warning
cam.set(3, 640) # set video FrameWidht
cam.set(4, 480) # set video FrameHeight

# Define min window size to be recognized as a face
minW = 0.1*cam.get(3)
minH = 0.1*cam.get(4)

# flag = True

while True:

    ret, img =cam.read() #read the frames using the above created object

    converted_image = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  #The function converts an input image from one color space to another

    faces = faceCascade.detectMultiScale( 
        converted_image,
        scaleFactor = 1.2,
        minNeighbors = 5,
        minSize = (int(minW), int(minH)),
       )

    for(x,y,w,h) in faces:

        cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2) #used to draw a rectangle on any image

        id, accuracy = recognizer.predict(converted_image[y:y+h,x:x+w]) #to predict on every single image

        # Check if accuracy is less them 100 ==> "0" is perfect match 
        if (accuracy < 100):
            id = names[id]
            accuracy = "  {0}%".format(round(100 - accuracy))
            takecommand()

        else:
            id = "unknown"
            accuracy = "  {0}%".format(round(100 - accuracy))
        
        cv2.putText(img, str(id), (x+5,y-5), font, 1, (255,255,255), 2)
        cv2.putText(img, str(accuracy), (x+5,y+h-5), font, 1, (255,255,0), 1)  
    
    cv2.imshow('camera',img) 

    k = cv2.waitKey(5) & 0xff # Press 'ESC' for exiting video
    if k == 27:
        break

# Do a bit of cleanup
speak("Thanks for using this program, have a good day.")
cam.release()
cv2.destroyAllWindows()

    
while True:
    Permission = takecommand()
    # if "wake up jarvis" in Permission:
    TaskExecution()
    speak("Thanks for using me")
    # elif "goodbye"in Permission:
    sys.exit()
    