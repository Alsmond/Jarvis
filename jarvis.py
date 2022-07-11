import random
import datetime
import pyttsx3
import speech_recognition as sr
import webbrowser as wb
import wikipedia
import subprocess
import pyjokes
import pyautogui
import os

engine=pyttsx3.init()

voices= engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)

voices_speed=140
engine.setProperty('rate',voices_speed)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

speak('hello master himanshu  Jarvis welcomes you')

def takeCommand():
    print("command function running")
    r= sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio= r.listen(source)
        
        
    try:
        print("Recognising....")
        query = r.recognize_google(audio,language='en-in')
    except Exception as e:
        print(e)
        speak("OK BYE HIMANSHU IF YOU NEED ANY HELP PLEASE CALL ME OUT ")
        return ""
    if query=="":
        return ""
    
    return str(query)




def time():
    time= datetime.datetime.now().strftime("%H:%M:%S")
    speak(time)
    print(time)



def date():
    day=int(datetime.datetime.now().day)
    month=int(datetime.datetime.now().month)
    year=int(datetime.datetime.now().year)
    speak("the current date is")
    print(day,month,year)
    speak(day)
    speak(month)
    speak(year)


def wishes():
    hour= datetime.datetime.now().hour
    if hour>=6 and hour<=12:
        speak("good morning himanshu")
    elif hour>=12 and hour<=18:
        speak("good afternoon himanshu")
    elif hour>=18 and hour<=24:
        speak("good evening himanshu")
    else:
        speak("good night")
    speak("how may i help you")








def open_chrome():
    url= "https://www.google.co.in/"
    chrome_path= "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
    wb.get(chrome_path).open(url)

        


def chrome_search():
    #speak("what should i search?")
    chromepath = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"  # location
    search = takeCommand().lower()
    wb.get(chromepath).open_new_tab(search + ".com")



def jokes():
    speak(pyjokes.get_joke())



def thankyou():
   my_grammer=['welcome master himanshu','when you greeds me it makes me feel special','its my pleasure master','am happy to help you out']
   greeds=random.choice(my_grammer) 
   speak(greeds)



def hidden_menu():
    speak("opening hidden menu")
    pyautogui.hotkey('winleft','x')

def task_manager():
    speak("opening task manager")
    pyautogui.hotkey('ctrl','shift','esc')

def task_view():
    speak("opening task view")
    pyautogui.hotkey('winleft','tab')


def setting():
    speak("opening setting")
    pyautogui.hotkey('winleft','i')


def screenshot():
    speak("taking screenshot")
    pyautogui.hotkey('winleft', 'prtscr')
    speak('screenshot done')



def snif():
    speak("open snif")
    pyautogui.hotkey("winleft","shift","s")
    speak("done")

def game_bar():
    speak("opening game bar")
    pyautogui.hotkey('winleft','g')

def close_game_bar():
    speak("closing game bar")
    pyautogui.hotkey('winleft','g')


def new_folder():
    speak("creating new folder")
    pyautogui.hotkey('ctrl','shift','n')
    speak("new folder done")


def run():
    speak("opening run")
    pyautogui.hotkey('winleft','r')

def close_the_app():
    speak("closing")
    pyautogui.hotkey('alt','f4')

def lock_pc():
    speak("your pc has been locked")
    pyautogui.hotkey('winleft','L')

def minimize_window():
    speak("all windows has been minimized")
    pyautogui.hotkey("winleft","m")

def restore_window():
    speak("all windows has been restored")
    pyautogui.hotkey("winleft","shift","m")


if __name__=="__main__":

    wishes()
    



    while True:
        query=takeCommand()
        print(query.lower())

        if "goodmorning jarvis" in query:
            speak("Happy to see you master himanshu")
        elif "goodafternoon jarvis" in query:
            speak("Happy to see you master himanshu")
        elif "goodevening jarvis" in query:
            speak("Happy to see you himanshu")
        elif "goodnight jarvis" in query:
            speak("very good night master himanshu am feeling very sleepy so am going for sleep see you tommrow morning take care master")
            close_the_app()

    



        elif "time" in query:
            time()
        elif "date" in query:
            date()
        elif "open chrome" in query:
            open_chrome()


        elif " task manager" in query:
            task_manager()
        

        elif "setting" in query:
            setting()


        elif "wikipedia" in query:
                speak("Searching...")
                query = query.replace("wikipedia", "")
                result = wikipedia.summary(query, sentences=2)
                speak(result)
                print(result)


    


        elif "search" in query:
            chrome_search()
        
        elif "open vs" in query:
            speak("opening vscode")
            location = "C:/Users/Alsmond/AppData/Local/Programs/Microsoft VS Code/Code.exe"
            vs = subprocess.Popen(location)
        
        elif "close vs" in query:
            speak("closing vs code")
            vs.terminate()
        

        elif "joke" in query:
            jokes()

        elif "thank you" in query:
            thankyou()

        elif "hidden menu" in query:
            hidden_menu()
        elif "task view" in query:
            task_view()

        elif "screenshot" in query:
            screenshot()

        elif "snif" in query:
            snif()

        elif "close the app" in query:
           close_the_app()


        elif "open virtual desktop" in query:
            speak("opening new virtual desktop ")
            pyautogui.hotkey('winleft', 'ctrl', 'd')

        elif"close virtual desktop" in query:
            speak("closing new virtual desktop ")
            pyautogui.hotkey('winleft','ctrl','f4')


        elif "lock the pc" in query:
            lock_pc()


        elif "open game bar" in query:
            game_bar()


        elif "close game bar" in query:
            close_game_bar()


        elif "new folder" in query:
            new_folder()

        elif "open run" in query:
            run()

        elif "minimise windows" in query:
            minimize_window()

        elif "restore windows" in query:
            restore_window()


        else:
            break










