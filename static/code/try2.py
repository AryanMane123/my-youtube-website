import datetime,time
from bs4 import BeautifulSoup
from win32com.client import Dispatch
import random
import requests
import wikipedia
import webbrowser
from pygame import mixer
import smtplib
import os
import speech_recognition as sr
from tkinter import *
# from PIL import PIL.Image , ImageTk
import PIL.Image, PIL.ImageTk
'''
Time , speak , listion , sendEmail , getfiles , playMusic , google , GUI class ,
'''
def Time(c):
    """
    1. half day name = d , full day name = D , day in number = N
    2. Hour = H , Minute = M , Second = S
    3. half Month name = mo , Full month name = MO
    4. Year = Y , week name in decimal foramat = W 
    """
    if c=="d":
        return datetime.datetime.now().strftime("%a")
    elif c=="D":
        return datetime.datetime.now().strftime("%A")
    elif c=="N":
        return datetime.datetime.now().strftime("%d")
    elif c=="H":
        return int(datetime.datetime.now().strftime("%H"))
    elif c=="M":
        return int(datetime.datetime.now().strftime("%M"))
    elif c=="S":
        return int(datetime.datetime.now().strftime("%S"))
    elif c=="W":
        return datetime.datetime.now().strftime("%w")
    elif c=="mo":
        return datetime.datetime.now().strftime("%b")
    elif c=="MO":
        return datetime.datetime.now().strftime("%B")

def speak(s):
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(s)

def listion():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        print("Listening.........")
        audio=r.listen(source, phrase_time_limit=5)
    try:
        print("Take action......")
        str1 = r.recognize_google(audio,language='en-in')
        print(f"Ok you are saying ===>  {str1}\n")
    except Exception as e:
        print(e)
        print("Please say again......\n")
        print("==========================\n")
        return "None"
    return str1

def sendEmail(sender_id,password,reciver_id,message):
    """
    Sender id , password , reciver id , message
    """
    try:
        s = smtplib.SMTP('smtp.gmail.com', 587)  
        s.starttls()  
        s.login(sender_id,password)  
        s.sendmail("manearyan4321@gmail.com'",reciver_id, message) 
        s.quit()
    except:
        return False
  
def getfiles(path):
    """
    take path of folder
    """
    return [f for f in os.listdir(path)]

def playMusic(name,next):
    """
    Music Full path, what is next = True then continue and also you give a time
    """
    mixer.init() 
    mixer.music.set_volume(5) 
    mixer.music.load(name) 
    mixer.music.play()
    if next == True:
        while 1:
            if mixer.music.get_busy() == False:
                break
    else:
        time.sleep(next)
        return 0

def google(s,*argv):
    '''
    string , total link , 1 for open and 0 for not
    '''
    from googlesearch import search
    import requests
    url = []
    for i in search(s,tld="com",num=argv[0],stop=argv[0]):
        url.append(i)

        try:
            if argv[1]==1:webbrowser.open(i)
        except:pass

    return url

# All GUI functions
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

    def CreateLable(self,*argv):
        '''
        1) text, font, x position ,y position , bg, fg
        2) text,padx,pady, font, x position ,y position ,bg,fg 
        3) text, font 
        '''
        a=0
        try:
            variable = Label(text=argv[0],font=argv[1],bg=argv[4],fg=argv[5])
            variable.place(x=argv[2],y=argv[3])
            a=1
        except:
            pass
        if a == 0:
            try:
                variable=Label(text=argv[0],padx=argv[1],pady=argv[2],font=argv[3])
                variable.place(x=argv[4],y=argv[5])
                a=1
            except:
                pass
        if a == 0:
                variable=Label(text=argv[0],font=argv[1])
                variable.pack()  
        return variable
    
    def B(self,line,Font,func,master=None,x=None,y=None,ima = None,**argv):
        '''
        Create Button
        text, font, command,optional(master , padx , pady , image) , extra **argv
        
        '''
        try:
            try:
                return Button(master,argv,text=line,font=Font,command=func,padx=x,pady=y,image=ima)
            except:
                return Button(self,argv,text=line,font=Font,command=func,padx=x,pady=y,image=ima)
        except:
            try:
                return Button(master,text=line,font=Font,command=func,padx=x,pady=y,image=ima)
            except:
                return Button(self,text=line,font=Font,command=func,padx=x,pady=y,image=ima)
          
    def jpg(self,filename,*argv):
        '''
        file name,resize x, resize y
        '''
        Final_image =  PIL.ImageTk.PhotoImage(PIL.Image.open(filename).resize((argv[0], argv[1]), PIL.Image.ANTIALIAS))

        return Label(image=Final_image)

    def image(self,filename,*argv):
        '''
        file name,resize x, resize y --> ruturn modified image

        '''
        F_image =  PIL.ImageTk.PhotoImage(PIL.Image.open(filename).resize((argv[0], argv[1]), PIL.Image.ANTIALIAS))
        return F_image

    def CreateMenu(self,Font,name,*argv):
        '''
        1.font,(,enu name set),(text1,func1,text2,fun2.. for add seperater , for cut write c),(...)
        2.
        '''
        myMenu = Menu(self)
        m = Menu(myMenu, tearoff=0)
        i = 0
        b = 0
        count=0
        for i in name:
            for i in range(len(argv)):
                if argv[i+2] == "s":
                    m.add_separator()
                    i+=1
                if argv[i+2] == "c" or argv[i+3] == "c":
                    myMenu.add_cascade(label=name[count],menu=m)
                    count+=1
                else:
                    m.add_command(label=argv[i],command=argv[i+1],font=Font)
                    i+=2
                # except:pass
                if count == len(name):
                    break
        # window.config(menu=myMenu)
        return myMenu

def clear(*argv):
    for i in argv:
        i.destroy()



if __name__ == '__main__':
    
    window = GUI(500,500,"Aryan",500,500,500,500)

    c = window.B("Aryan","lucida 13 bold",lambda:print("Click"),10,10)
    c.pack()

    ig = window.image("icon.png",50,50)

    c = Label(text="",font="lucida 13 bold",command=lambda:print("Click"),padx=10,pady=10)
    c.pack()
    
    window.mainloop()  