from tkinter import *
from stt import *
import speech_recognition as sr
import pyaudio
root =Tk()

def text_eng():
    Head['text']='Start talking'
    Head.pack()
    text=""
    r  = sr.Recognizer()
    with sr.Microphone() as source:
        r.energy_threshold = 4000
        try:
            while(text!='enter'):
                print(text)
                otpt.insert(INSERT,text)
                otpt.insert(INSERT,'\n')
                otpt.pack()
                audio = r.listen(source) 
                text = r.recognize_google(audio)  
        except: 
            Head['text']='Sorry, couldnt hear you! Try again'
            Head.pack()

                
    
def text_hin():
    Head['text']='Start talking'
    Head.pack()
    text=""
    r  = sr.Recognizer()
    with sr.Microphone() as source:
        text=""
        r.energy_threshold = 1000
        try:
            while(text!='रुक'):
                print(text)
                otpt.insert(INSERT,text)
                otpt.insert(INSERT,'\n')
                otpt.pack()
                audio = r.listen(source) 
                text = r.recognize_google(audio,language='hi-IN')
        except: 
            Head['text']='Sorry, couldnt hear you! Try again'
            Head.pack()

def text_mar():
    Head['text']='Start talking'
    Head.pack()
    text=""
    r  = sr.Recognizer()
    with sr.Microphone() as source:
        text=""
        r.energy_threshold = 1000
        try:
            while(text!='थांब'):
                print(text)
                otpt.insert(INSERT,text)
                otpt.insert(INSERT,'\n')
                otpt.pack()
                audio = r.listen(source) 
                text = r.recognize_google(audio,language='mr-in')
        except: 
            Head['text']='Sorry, couldnt hear you! Try again'
            Head.pack()

def create_file():
    #name=str(E.get('1',END))
    name=E1.get()
    name=name+'.txt'
    stuff=otpt.get("1.0",END)
    f=open(name,'w+')
    f.write(stuff)
    f.close
    Head['text']='Created'
    Head.pack()
    
def copy():
    stuff=otpt.get("1.0",END)
    

bottomFrame=Frame(root)
bottomFrame.pack()


#Heading
Head=Label(root,text="Talk to type",bg="Black",fg="white")
Head.pack(fill=X,pady=10)

canvas=Canvas(root,width=900,height=300)
canvas.pack()
canvas.create_text(350, 30, anchor=W, font="Algerian",
    text="SPEECH TO TEXT CONVERTER")

#creating graphics
greenbox=canvas.create_rectangle(175,125,300,180,fill="#03E80D")
purplebox=canvas.create_rectangle(350,125,475,180,fill="purple")
pinkbox=canvas.create_rectangle(525,125,650,180,fill="#1303E8")
#graybox=canvas.create_rectangle(35,225,165,570,fill="#E8E2C7")

#creating button

button1 = Button(root, text = "  ENGLISH", anchor = W,command=text_eng)
button1.configure(width = 10,fg="black",bg="#FFEF4B" ,activebackground = "#33B5E5", relief = FLAT)
button1_window = canvas.create_window(200, 140, anchor=NW, window=button1)


button2 = Button(root, text = "  HINDI", anchor = W,command=text_hin)
button2.configure(width = 10,fg="black",bg="#AC77E8" ,activebackground = "#33B5E5", relief = FLAT)
button2_window = canvas.create_window(375, 140, anchor=NW, window=button2)



button3 = Button(root, text = "MARATHI", anchor = W,command=text_mar)
button3.configure(width = 10,fg="black",bg="#6FCFE8" ,activebackground = "#33B5E5", relief = FLAT)
button3_window = canvas.create_window(550, 140, anchor=NW, window=button3)


button4 = Button(root, text = "TEXT FILE", anchor = W,bg="pink",command=create_file)
button4.place(x=450,y=320)

#checkbox

#c1=Checkbutton(bottomFrame,text="COPY")
#c1.pack(padx=10,pady=10)

#c2=Checkbutton(root,text="Convert into text file")
#c2.pack(padx=10,pady=10)

#ctf=Button(bottomFrame,text="Convert to txt file",fg="red",command= lambda :  create_file())
#ctf.pack(side="left",padx=10,pady=10)

E1 = Entry(root, bd =5)
E1.place(x=550,y=320)

l1=Label(root,text="(Enter Textfile name)")
l1.place(x=680,y=320)

#text-field

otpt = Text(root)
otpt.pack(side="bottom")


root.mainloop()



