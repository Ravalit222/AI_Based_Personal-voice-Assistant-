# Loading different python packages
import pyttsx3 # text to speech conversion
import speech_recognition as sr # speech recognition
import datetime # date and time information
import wikipedia # wikipedia search
import webbrowser # web browsing
import os # system calls
import cv2 # webcam use
import requests # HTTP library for online crawling and surfing
import pywhatkit as kit # Whatsapp and You-Tube automation
import random # Random selection, here use for random music play
import pyautogui # GUI automation for mouse and keyboard
import sys # Access to system specfic parameters and functions
import time # Time information
import operator # Mathematic operations
from bs4 import BeautifulSoup # Information scraping from web pages

agent = pyttsx3.init('sapi5') # microsoft speech API called 'sapi5'
voice = agent.getProperty('voices') # setting voice parameter
agent.setProperty('voice', voice[1].id) # '0' for male and '1' for female
agent.setProperty('rate', 180) # rate of speaking by speech agent

def speak(audio): # function for personal assistant to speak
    agent.say(audio) # for personal assistant to say
    agent.runAndWait() # personal assistant is waiting for user response

def greet(): # function for greeting users
    daytime = int(datetime.datetime.now().hour) # time fetching
    if daytime >= 0 and daytime < 12: # till noon
        speak("Good Morning!")
    elif daytime >= 12 and daytime < 16: # till 4 pm
        speak("Good Afternoon!")
    else:
        speak("Good Evening!") # after 4 pm

    speak("I am your Assistant Sophia, Ready To Comply. What can I do for you ?")

def userCommand(): # function to take command/query given by user to the personal assistant
    r = sr.Recognizer()
    with sr.Microphone() as source: # microphone source for communication
        print("Listening...")
        r.pause_threshold = 1 # pause for personal assistant to think and act
        audio = r.listen(source) # user query will be pass to the personal assistant through microphone
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in') # user audio recognised by the personal assistant
                                                            # 'en-in' is english with indian region
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again please...") # saying pardon if user voice is not recognize by the personal assistant
        return "None"
    return query

def weather(city): # function for weather report for any city
    head = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    city=city.replace(" ","+")
    res = requests.get(f'https://www.google.com/search?q={city}&oq={city}&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8',headers=head)
    bs = BeautifulSoup(res.text,'html.parser')
    location = bs.select('#wob_loc')[0].getText().strip()
    info = bs.select('#wob_dc')[0].getText().strip()
    weather = bs.select('#wob_tm')[0].getText().strip()
    speak("Here is current weather report" + "\nLocation: " + str(location) + "\nInfo: "+ str(info)
          + "\nTemperature" + str(weather)+"°C")
    print("Here is current weather report" + "\nLocation: " + str(location) + "\nInfo: " + str(info)
          + "\nTemperature: " + str(weather) + "°C")

if __name__ == "__main__": # main function for all user defined tasks
    greet()
    while True:
        query = userCommand().lower()
        if 'wikipedia' in query: # wikipedia search
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2) # crawling wikipedia of the query
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open google' in query: # googling out
            speak("what should I search ?")
            qry = userCommand().lower()
            webbrowser.open(f"{qry}") # opeing default web browser of your system
            results = wikipedia.summary(qry, sentences=2) # crawling wikipedia of the query
            speak(results)

        elif 'close google' in query: # closing web engine
            os.system("taskkill /f /im msedge.exe")

        elif "who are you" in query: # voice assistant introducing himself/herself
            print('My Name Is Sofia')
            speak('My Name Is Sofia')
            print('I can Do Everything that my creator has assigned me to do')
            speak('I can Do Everything that my creator has assigned me to do')

        elif "who created you" in query: # inventor of a voice assistant
            print('I am created by Miss Ravali using Python Language in Pycharm.')
            speak('I am created by Miss Ravali using Python Language in Pycharm.')

        elif 'open youtube' in query: # you-tube playing
            speak("what you will like to watch ?")
            qrry = userCommand().lower()
            kit.playonyt(f"{qrry}")

        elif 'search on youtube' in query: # you-tube searching
            query = query.replace("search on youtube", "")
            webbrowser.open(f"www.youtube.com/results?search_query={query}")

        elif 'close youtube' in query: # closing you-tube
            os.system("taskkill /f /im msedge.exe")

        elif 'play music' in query: # turn on system music player
            music_player_directory = 'C:\\Users\\tsaik\\Music'
            songs = os.listdir(music_player_directory)
            os.startfile(os.path.join(music_player_directory, random.choice(songs)))

        elif 'close music' in query: # turn off system music player
            os.system("taskkill /f /im Music.UI.exe")

        elif 'play kgf 2 movie' in query: # turn on system movie player
            movie_directory = "C:\\Users\\tsaik\\Videos"
            os.startfile(movie_directory)

        elif 'close movie' in query: # turn off system music player
            os.system("taskkill /f /im VLC.UNIVERSAL.exe")

        elif "volume up" in query: # increasing system volume
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")

        elif "volume down" in query: # decreasing system volume
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")

        elif "mute" in query: # muting the system volume
            pyautogui.press("volumemute")

        elif 'the time' in query: # telling current time
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {current_time}")

        elif "open command prompt" in query: # opening command prompt
            os.system("start cmd")

        elif "close command prompt" in query: # closing command prompt
            os.system("taskkill /f /im cmd.exe")

        elif "shut down the system" in query: # turn off your PC
            os.system("shutdown /s /t 5")

        elif "restart the system" in query: # restart your PC
            os.system("shutdown /r /t 5")

        elif "Lock the system" in query: # lockdown your PC
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

        elif "go to sleep" in query: # put your PC to sleep
            speak('alright then, I am switching off for a while')
            sys.exit()

        elif "what is my ip address" in query: # IP Address information
            speak("Checking")
            try:
                ip_address = requests.get('https://api.ipify.org').text # getting IP address from api
                print(ip_address)
                speak("your ip address is")
                speak(ip_address)
            except Exception as e:
                speak("network is weak, please try again some time later")

        elif "open camera" in query: # open and close webcam
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam', img)
                k = cv2.waitKey(1)
                if k == 27: # ascii value of ESC Key is 27
                    break;  # pressing esc button on keyboard to close the camera
            cap.release()
            cv2.destroyAllWindows()

        elif "take screenshot" in query: # taking window screenshot
            speak('tell me a name for the file')
            filename = userCommand().lower()
            time.sleep(3)
            image = pyautogui.screenshot()
            image.save(f"{filename}.png") # saving screenshot in image file
            speak("screenshot saved")

        elif "calculate" in query:
            srg = sr.Recognizer()
            with sr.Microphone() as source:
                speak("Ready")
                print("Listening...")
                srg.adjust_for_ambient_noise(source)
                audio = srg.listen(source)
            final_string = srg.recognize_google(audio)
            print(final_string)

            def get_operator_fn(op): # basic mathematics operation
                return {
                    '+': operator.add,
                    '-': operator.sub,
                    'x': operator.mul,
                    'divided': operator.__truediv__,
                }[op]

            def eval_bianary_expr(op1, oper, op2): # calculating expression
                op1, op2 = int(op1), int(op2)
                return get_operator_fn(oper)(op1, op2)

            speak("your result is")
            speak(eval_bianary_expr(*(final_string.split())))

        elif "open notepad" in query: # opening notepad
            pyautogui.hotkey('win')
            time.sleep(1)
            pyautogui.write('notepad')
            time.sleep(1)
            pyautogui.press('enter')
            time.sleep(1)
            speak('tell me what to write in the file')
            file_contents = userCommand().lower()
            pyautogui.write(file_contents, interval=0.1) # writing into the file

        elif "save notepad file" in query: # file save
            pyautogui.hotkey('ctrl', 's')
            time.sleep(3)
            path = os.getcwd()
            speak('tell me a name for the file')
            fname = userCommand().lower()
            pyautogui.typewrite(fname + '.txt') # saving the file
            pyautogui.press('enter')
            speak("notepad file saved")

        elif "close notepad" in query: # closing notepad
            os.system("taskkill /f /im notepad.exe")

        elif "weather report" in query: # weather report
            speak('tell me the city name')
            print("tell me the city name")
            city = userCommand().lower()
            city = city + " weather"
            weather(city) # calling weather function

        elif "good bye" in query or "ok bye" in query or "goodbye" in query: # for exit of an agent to stop communication
            speak('your friend Sophia is shutting down, Good bye')
            print('your friend Sophia is shutting down, Good bye')
            break







