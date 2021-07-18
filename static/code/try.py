'''
    Author: Aryan
    Date: Start at 21 march
    Purpose: Jarvis Al assistant for Me.
'''

# Path of startup = C:\Users\Admin\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup

import datetime,  time,  random,  wikipedia,  webbrowser,  winsound
from pickle import FRAME
import os
import speech_recognition as sr
from tkinter import *
import PIL.Image, PIL.ImageTk


def speak(s):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(s)

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <= 11:
        speak("Good morning sir!")
    elif hour > 11 and hour <= 18:
        speak("Good Afternoon sir!")
    else:
        speak("Good evening sir!")
    speak("Hello sir i am jarvis your AI ASSISTANT Sir do you want to open Work timer")
    yes_no = takeCommand()
    if "yes" in yes_no or "open" in yes_no:
        path = "C:\\Users\\Admin\\Desktop\\Mega projects\\Timer_For_Work.pyw"
        os.startfile(path)
        speak("Ok sir opening Work timer All the best for work")

def takeCommand():
    global Info
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        # Info.config(text="Listening...")
        # Info.update()
        print("Listeing....")

        audio=r.listen(source, phrase_time_limit=5)
    try:
        # Info.config(text="Tacking action...")
        # Info.update()
        print("Take action")
        str1 = r.recognize_google(audio,language='en-in')
    except Exception as e:
        # Info.config(text="Plese say again...")
        # Info.update()
        print("PLase say again")
        return "Can't capture it"
    return str1

count = 1
num = 0
first = 0
# HERE IS MATCHES

def match_the_user_input():

    global command,count,Info,list_Box,num,list_box,f,first,scrollbar
    print(num)
    if num==3:
        list_Box.destroy()
        window.update()
        num=0

    if num==0 and first!=0:
        list_Box = Listbox(f, yscrollcommand=scrollbar.set,height=20,font="bold 15",width=100)
        list_Box.pack()
        scrollbar.config(command=list_Box.yview)
        scrollbar.update()
    
    winsound.Beep(1000,500)
    str1=takeCommand().lower()
    if num!=0:window.Ladd("","S")
    window.Ladd(str1.title(),"Q")
    window.update()

    if 'wikipedia' in str1:
        speak("Ok searching....")
        str1 = str1.replace("wikipedia","")
        try:
            info = wikipedia.summary(str1, sentences=2)
            copy = ""
            for i in range(len(info)):
                if i%70==0 and i!=1 and i!=0:
                    copy+=info[i]
                    copy+="\n"
                else:
                    copy+=info[i]
            window.Ladd(copy,"A",size=9)
            window.update()
            speak("According to wikipedia")
            speak(info)
        except Exception as e:
            window.Ladd("Not found","A")
            window.update()
            speak("Not found")
    
    if 'google search' in str1:
     
        str1=str1.replace("google search","")
        print(str1)
        string = "https://www.google.com/search?q="+str1
        speak(f"Ok sir I am searching {str1} in google")
        webbrowser.open(string)
        window.Ladd(f"Ok sir I am searching {str1} in google","A",size=12)
        window.update()

        
    elif 'open youtube' in str1:
        window.Ladd("Ok sir opening You tube","A")
        window.update()
        speak("Ok opening you tube")
        webbrowser.open("https://www.youtube.com")
    
    # This Other program
    elif 'play song' in str1 or 'play music' in str1 or 'open music player' in str1:
        window.Ladd("Opening Music player","A")
        window.update()
        path = "C:\\Users\\Admin\\Documents\\Mega projects\\Music_player.pyw"
        os.startfile(path)
        speak("Ok sir opening Music player made by Aryan")
    
    elif 'shutdown' in str1 or 'close program' in str1:
        speak("Ok sir see you again closing program")
        exit()
    
    elif 'time now' in str1:
        time1=datetime.datetime.now().strftime("%H:%M:%S")
        window.Ladd(time1,"A")
        window.update()
        print(time1)
        speak(time1)
   
    elif 'date now' in str1:
        date1=datetime.datetime.now().strftime("%A %d %B")
        window.Ladd(date1,"A")
        window.update()
        print(date1)
        speak(date1)

    elif 'hello' in str1:
        speak("Hello sir what i can help for you?")
    
    elif 'mad' in str1:
        speak("No sir i am not mad i am intellegent AI assistant not a normal machine")
    
    elif 'about you' in str1:
        speak('''Hi sir i am intellegent AI desktop assistant . I was created by Aryan. My birth date is 1 march 2021 . I can do anything for you just speak''')
    
    elif 'how are you' in str1:
        speak("I am fine sir thanks")
    
    elif 'your hobby' in str1:
        speak("Sir my hobby is make easy your work and my mission make word workless")
    
    elif 'open timer' in str1:
        timer_path="C:\\Users\\Admin\\Documents\\Mega projects\\Timer_for_work.pyw"
        os.startfile(timer_path)
        speak("Opening programmer timer")
    
    elif 'tell news' in str1:
        Akhabar_path="C:\\Users\\Admin\\Documents\\Python programming\\Akhbar.py"
        speak("Ok sir top 5 news head lines from Alexa")
        speak("Opening new window")
        os.startfile(Akhabar_path)
        time.sleep(30)
    
    elif 'nonsense' in str1:
        speak("No sir i am ai assistant not humen because humen have sense computer not have sense computer have hard disk and ram")
    
    elif "human" in str1:
        speak('''Humen is intellengent animal who invent me i mean comuters. I love humans. they are very inventive and creative. 
        but in knowledge and work I am much better than humans''')

    num+=1
    first+=1

class GUI(Tk):
    def __init__(self,h,w,title,*argv) -> None:
        '''
        higth , width , Title , min , max
        '''
        super().__init__()
        self.geometry(f"{w}x{h}")
        self.title(title)
        try:
            self.maxsize(argv[0],argv[1])
            self.minsize(argv[2],argv[3])
        except:pass
  
    
    def image(self,filename,*argv):
        '''
        file name,resize x, resize y --> ruturn modified image

        '''
        F_image =  PIL.ImageTk.PhotoImage(PIL.Image.open(filename).resize((argv[0], argv[1]), PIL.Image.ANTIALIAS))
        return F_image

    def Ladd(self,s,type,size=18):
        if type=="Q":
            F = Frame(list_Box)
            F.pack(side=LEFT)
            l = Label(F,text=s,font=f"lucida {size} bold",relief=SUNKEN)
            l.pack(side=LEFT)
            list_Box.insert(END,l)
        if type=="A":
            F = Frame(list_Box)
            F.pack(side=RIGHT)
            l = Label(F,text=s,font=f"lucida {size} bold",relief=SUNKEN)
            l.pack(side=RIGHT)
            list_Box.insert(END,l)

def clear():
    global list_Box
    list_Box.destroy()

Always_state = True

def Always():
    global Always_state
    if Always_state == TRUE:
        speak("Always listing mode on")
        B['state'] = DISABLED
        B.update()
        Always_state=False
        L.config(text="On",fg="green")
        L.update()
        Taction("Always listing mode on")

    elif Always_state == FALSE:
        speak("Always listing mode off")
        B['state'] = NORMAL
        B.update()
        Always_state=TRUE
        L.config(text="Off",fg="red")
        L.update()
        Taction("Always listing mode off")

def Taction(command,colour=None,X1=200):
    global action
    action.config(text=command+".....",fg=colour)
    action.place(x=X1,y=480)
    action.update()

if __name__ == '__main__':

    window = GUI(580,500,"Assistant Jarvis")
    f = Frame(window,height=350,width=500)
    f.pack()
    # f.after(1000,wishMe)
    scrollbar = Scrollbar(f)
    scrollbar.pack(side=RIGHT,fill=Y)
    list_Box = Listbox(f, yscrollcommand=scrollbar.set,height=20,font="bold 15",width=100)
    list_Box.pack()
    scrollbar.config(command=list_Box.yview)
    scrollbar.update()

    L = Label(text="Off",font="lucida 14 bold",fg="red")
    L.place(x=32,y=480)

    action = Label(text="Welcome...",font="lucida 14 bold")
    action.place(x=200,y=480)

    # Always listion Button
    im1 = window.image("listion.jpg",60,60)
    B1 = Button(image=im1,command=Always)
    B1.pack(side=LEFT,padx=20,anchor=SW,pady=10)

    # Speak Button
    B = Button(window,text="Speak",font="lucida 22 bold",command=match_the_user_input,bg="red")
    B.pack(side=LEFT,padx=30,anchor=SW,pady=10)

    # Clear Button
    im2 = window.image("clear.jpg",60,60)
    B2 = Button(image=im2,command=clear)
    B2.pack(side=LEFT,padx=20,anchor=SW,pady=10)

    # Seting Button
    im3 = window.image("setting.jfif",60,60)
    B1 = Button(image=im3)
    B1.pack(side=LEFT,padx=20,anchor=SW,pady=10)

    window.mainloop()
    