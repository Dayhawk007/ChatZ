from tkinter import *
from tkinter import messagebox
from chatterbot import ChatBot
import datetime
from chatterbot.conversation import Statement
from chatterbot.trainers import ChatterBotCorpusTrainer
import speech_recognition as sr
import webbrowser
import requests
from bs4 import BeautifulSoup
import wikipedia
from threading import Thread
from question_model import Question
from quiz_data import question_data
from quiz_brain import QuizBrain
from quiz_ui import quiz
from random import shuffle
import random
import html
import pyttsx3
import io
from pexels_api import API
from PIL import ImageTk,Image
API_KEY="563492ad6f91700001000001a8c33420b1aa4db68fca0324878fe129"


question_bank = []
for question in question_data:
    choices = []
    question_text = html.unescape(question["question"])
    correct_answer = html.unescape(question["correct_answer"])
    incorrect_answers = question["incorrect_answers"]
    for ans in incorrect_answers:
        choices.append(html.unescape(ans))
    choices.append(correct_answer)
    shuffle(choices)
    new_question = Question(question_text, correct_answer, choices)
    question_bank.append(new_question)
quizBrain=QuizBrain(question_bank)



def temp(temp):
    
    url=f'https://www.google.com/search?q=Temperature of {temp}'
    c=requests.get(url)
    data=BeautifulSoup(c.text,"html.parser")
    temperature=data.find('div',class_ = 'BNeawe').text
    temperature_string=f'The temperature of {temp} is {temperature}'
    speak(temperature_string)
    return temperature_string

def wiki(search_query):
    result=wikipedia.summary(search_query,sentences=2)
    speak(result)
    return result

a=pyttsx3.init('sapi5')
voice=a.getProperty('voices')
a.setProperty('voice',voice[0].id)



def speak(audio):
    a.say(audio)
    t=Thread(target=a.runAndWait)
    t.start()

# create ChatBot
chatBot = ChatBot('ChatBot')
trainer = ChatterBotCorpusTrainer(chatBot)
chatBot.storage.drop()
trainer.train("chatterbot.corpus.english")
# create ChatBot trainer


# Train ChatBot with English language corpus
# you can train with different language
# or with your custom .yam file


# Greeting from chat bot
#print("Hi, I am ChatBot")
def abcd(msg):
    
    a=chatBot.get_response(Statement(text=msg, search_text=msg))
   
    return a
  
BG_GREY= '#ABB2B9'
BG_COLOR='#17202A'
TEXT_COLOR='#EAECEE'

FONT='Helvetica 14'
FONT_BOLD='Helvetica 13 bold'


def showImage(search):
    # Create an instance of tkinter window
    win = Tk()

    api=API(API_KEY)
    api.search(search,page=1,results_per_page=10)
    photos=api.get_entries()
    photo=random.choice(photos)
    # Define the geometry of the window
    win.geometry("700x500")

    frame = Frame(win, width=600, height=400)
    frame.pack()
    frame.place(anchor='center', relx=0.5, rely=0.5)
    img=requests.get(photo.medium)
    # Create an object of tkinter ImageTk
    img = ImageTk.PhotoImage(Image.open(io.BytesIO(img.content)),master=win)

    # Create a Label Widget to display the text or Image
    label = Label(frame, image = img)
    label.pack()

    win.mainloop()



def TicTacToe():
    root=Tk()
    #root.geometry('452x485')
    root.title("Tic Tac Toe")
    root.resizable(width=FALSE,height=FALSE)


    count=0
    clicked=True


    a=Label(root,text='Player 1: X',bg='white',font='comicsans')
    a.grid(row=0,column=0)

    c=Label(root,text='Player 2: O',bg='white',font='comicsans')
    c.grid(row=0,column=2)
    def disable():
        b1.config(state=DISABLED)
        b2.config(state=DISABLED)
        b3.config(state=DISABLED)
        b4.config(state=DISABLED)
        b5.config(state=DISABLED)
        b6.config(state=DISABLED)
        b7.config(state=DISABLED)
        b8.config(state=DISABLED)
        b9.config(state=DISABLED)


    def check():
        if b1['text'] == 'X' and b2['text'] == 'X' and b3['text'] == 'X':
            b1.config(bg='green')
            b2.config(bg='green')
            b3.config(bg='green')
            messagebox.showinfo('Tic Tac Toe', 'Hurray!! X won...')
            disable()
        elif b1['text'] == 'X' and b4['text'] == 'X' and b7['text'] == 'X':
            b1.config(bg='green')
            b4.config(bg='green')
            b7.config(bg='green')
            messagebox.showinfo('Tic Tac Toe', 'Hurray!! X won...')
            disable()

        elif b2['text'] == 'X' and b5['text'] == 'X' and b8['text'] == 'X':
            b2.config(bg='green')
            b5.config(bg='green')
            b8.config(bg='green')
            messagebox.showinfo('Tic Tac Toe', 'Hurray!! X won...')
            disable()
        elif b3['text'] == 'X' and b6['text'] == 'X' and b9['text'] == 'X':
            b3.config(bg='green')
            b6.config(bg='green')
            b9.config(bg='green')
            messagebox.showinfo('Tic Tac Toe', 'Hurray!! X won...')
            disable()
        elif b4['text'] == 'X' and b5['text'] == 'X' and b6['text'] == 'X':
            b4.config(bg='green')
            b5.config(bg='green')
            b6.config(bg='green')
            messagebox.showinfo('Tic Tac Toe', 'Hurray!! X won...')
            disable()
        elif b7['text'] == 'X' and b8['text'] == 'X' and b9['text'] == 'X':
            b7.config(bg='green')
            b8.config(bg='green')
            b9.config(bg='green')
            messagebox.showinfo('Tic Tac Toe', 'Hurray!! X won...')
            disable()

        elif b1['text'] == 'X' and b5['text'] == 'X' and b9['text'] == 'X':
            b1.config(bg='green')
            b5.config(bg='green')
            b9.config(bg='green')
            messagebox.showinfo('Tic Tac Toe', 'Hurray!! X won...')
            disable()


        elif b1['text'] == 'O' and b2['text'] == 'O' and b3['text'] == 'O':
            b1.config(bg='green')
            b2.config(bg='green')
            b3.config(bg='green')
            messagebox.showinfo('Tic Tac Toe', 'Hurray!! O won...')
            disable()
        elif b1['text'] == 'O' and b4['text'] == 'O' and b7['text'] == 'O':
            b1.config(bg='green')
            b4.config(bg='green')
            b7.config(bg='green')
            messagebox.showinfo('Tic Tac Toe', 'Hurray!! O won...')
            disable()

        elif b2['text'] == 'O' and b5['text'] == 'O' and b8['text'] == 'O':
            b2.config(bg='green')
            b5.config(bg='green')
            b8.config(bg='green')
            messagebox.showinfo('Tic Tac Toe', 'Hurray!! O won...')
            disable()
        elif b3['text'] == 'O' and b6['text'] == 'O' and b9['text'] == 'O':
            b3.config(bg='green')
            b6.config(bg='green')
            b9.config(bg='green')
            messagebox.showinfo('Tic Tac Toe', 'Hurray!! O won...')
            disable()
        elif b4['text'] == 'O' and b5['text'] == 'O' and b6['text'] == 'O':
            b4.config(bg='green')
            b5.config(bg='green')
            b6.config(bg='green')
            messagebox.showinfo('Tic Tac Toe', 'Hurray!! O won...')
            disable()
        elif b7['text'] == 'O' and b8['text'] == 'O' and b9['text'] == 'O':
            b7.config(bg='green')
            b8.config(bg='green')
            b9.config(bg='green')
            messagebox.showinfo('Tic Tac Toe', 'Hurray!! O won...')
            disable()

        elif b1['text'] == 'O' and b5['text'] == 'O' and b9['text'] == 'O':
            b1.config(bg='green')
            b5.config(bg='green')
            b9.config(bg='green')
            messagebox.showinfo('Tic Tac Toe', 'Hurray!! O won...')
            disable()
        
        elif count == 9:
            messagebox.showinfo('Tic Tac Toe',"It's a Tie \n No one wins!!" )
            disable()
    def b_click(b):
        global clicked, count

        if b["text"] == " " and clicked == True:
            b["text"] = "X"
            clicked = False
            count += 1
            check()
        elif b["text"] == " " and clicked == False:
            b["text"] = "O"
            clicked = True
            count += 1
            check()
        else:
            messagebox.showerror("Tic Tac Toe")
            
    def reset():
        global b1,b2,b3,b4,b5,b6,b7,b8,b9
        global clicked,count
        clicked = True
        count = 0
        b1 = Button(root, text=" ", font=("comicsans", 20), height=3, width=6, bg="white", command=lambda: b_click(b1))
        b2 = Button(root, text=" ", font=("comicsans", 20), height=3, width=6, bg="white", command=lambda: b_click(b2))
        b3 = Button(root, text=" ", font=("comicsans", 20), height=3, width=6, bg="white", command=lambda: b_click(b3))

        b4 = Button(root, text=" ", font=("comicsans", 20), height=3, width=6, bg="white", command=lambda: b_click(b4))
        b5 = Button(root, text=" ", font=("comicsans", 20), height=3, width=6, bg="white", command=lambda: b_click(b5))
        b6 = Button(root, text=" ", font=("comicsans", 20), height=3, width=6, bg="white", command=lambda: b_click(b6))

        b7 = Button(root, text=" ", font=("comicsans", 20), height=3, width=6, bg="white", command=lambda: b_click(b7))
        b8 = Button(root, text=" ", font=("comicsans", 20), height=3, width=6, bg="white", command=lambda: b_click(b8))
        b9 = Button(root, text=" ", font=("comicsans", 20), height=3, width=6, bg="white", command=lambda: b_click(b9))

        # Grid our buttons to the screen
        b1.grid(row=1, column=0)
        b2.grid(row=1, column=1)
        b3.grid(row=1, column=2)

        b4.grid(row=2, column=0)
        b5.grid(row=2, column=1)
        b6.grid(row=2, column=2)

        b7.grid(row=3, column=0)
        b8.grid(row=3, column=1)
        b9.grid(row=3, column=2)

    my_menu = Menu(root)
    root.config(menu=my_menu)

    # Create Options Menu
    options_menu = Menu(my_menu, tearoff=False)
    my_menu.add_cascade(label="Options", menu=options_menu)
    options_menu.add_command(label="Reset Game", command=reset)

    reset()

    root.mainloop()




class chatapplication:

    def __init__(self):
        self.window=Tk()
        self._setup_main_window()
        self.audio_input=""
        self.condition=0
        self.voice_bool=False
        t1=Thread(target=self.sr,name="Microphone")
        t1.start()
        

    def run(self):
        self.window.mainloop()


            
    
    def sr(self):
        self.a=sr.Recognizer()
        self.audio_input=""
        while(True):
            if(self.voice_bool==True):
                with sr.Microphone() as self.source:
                    self.a.pause_threshold=0.5
                    self.text_widget.configure(state=NORMAL)
                    self.text_widget.insert(END, "Listening\n\n")
                    self.audio=self.a.listen(self.source)
            
            
                try:
                    self.text_widget.configure(state=NORMAL)
                    self.text_widget.insert(END, "Recognizing\n\n")
                    self.input=self.a.recognize_google(self.audio)
                    self.audio_input=self.input
                    self._insert_message(self.audio_input,"You")
                    print(self.audio_input)
                    self.voice_bool=False
                    
                    

                except Exception as e:
                    print(e)
                    self.text_widget.configure(state=NORMAL)
                    self.text_widget.insert(END, "Say that again please\n\n")
                    speak("Say that again please")

            else:
                pass                


    def _setup_main_window(self):
        self.window.title("Chat")
        self.window.resizable(width=False,height=False)
        self.window.configure(width=500,height=500,bg=BG_COLOR)


        head_label=Label(self.window,bg=BG_COLOR,fg=TEXT_COLOR,
                        text='The GyaniBot',font=FONT_BOLD,pady=10)
        head_label.place(relwidth=1)

        line=Label(self.window,width=450,bg=BG_COLOR)
        line.place(relwidth=1,rely=0.07,relheight=0.012)


        self.text_widget=Text(self.window,width=20,height=2,bg=BG_COLOR,fg=TEXT_COLOR,font=FONT,padx=5,pady=5)
        self.text_widget.place(relheight=0.745,relwidth=1,rely=0.08)
        self.text_widget.configure(cursor='arrow',state=DISABLED)


        scrollbar=Scrollbar(self.text_widget)
        scrollbar.place(relheight=1,relx=0.975)
        scrollbar.configure(command=self.text_widget.yview)

        
        bottom_label=Label(self.window,bg=BG_GREY,height=60)
        bottom_label.place(relwidth=1,rely=0.825)
        

        self.msg_entry=Entry(bottom_label,bg='#2C3E50',fg=TEXT_COLOR,font=FONT)
        self.msg_entry.place(relwidth=0.70,relheight=0.06,relx=0.011,rely=0.008)
        self.msg_entry.focus()
        self.msg_entry.bind("<Return>",self._on_enter_pressed)

        voice_button=Button(bottom_label,text='Record',font=FONT_BOLD,width=10,bg=BG_GREY
                            ,command=lambda: self._on_voice(None))
        voice_button.place(relx=0.72,rely=0.008,relheight=0.06,relwidth=0.14)

        send_button=Button(bottom_label,text='Send',font=FONT_BOLD,width=10,bg=BG_GREY
                            ,command=lambda: self._on_enter_pressed(None))
        send_button.place(relx=0.87,rely=0.008,relheight=0.06,relwidth=0.11)


    def _on_voice(self,event):
        self.voice_bool=True
    def _on_enter_pressed(self,event):
        if(self.condition==1):
            search_query=self.msg_entry.get()
            self.text_widget.configure(state=NORMAL)
            self.text_widget.insert(END,f"You: {search_query}\n\n")
            self._insert_message(wiki(search_query),"GyaniBot")
            self.text_widget.see(END)

        elif(self.condition==4):
            t=self.msg_entry.get()
            self.text_widget.configure(state=NORMAL)
            self._insert_message(temp(t),"GyaniBot")
            self.text_widget.see(END)
        
        elif(self.condition==2):
            t=self.msg_entry.get()
            self.text_widget.configure(state=NORMAL)
            showImage(t)
            self.text_widget.see(END)

        


               
    def _insert_message(self,msg,sender):
        if not msg:
            return
        if(sender=="GyaniBot"):
            msg1=f"{sender}: {msg}\n\n"
            self.text_widget.configure(state=NORMAL)
            self.text_widget.insert(END, msg1)
            speak(msg1)
            self.text_widget.configure(state=DISABLED)
            self.text_widget.see(END)
            self.msg_entry.delete(0,END)
            self.condition=0

        elif(msg.lower() == "open wikipedia"):
            self.msg_entry.delete(0,END)
            msg1=f"{sender}: {msg}\n\n"
            self.text_widget.configure(state=NORMAL)
            self.text_widget.insert(END, msg1)
            self.text_widget.insert(END, f"GyaniBot: Type the search query in the box to search about it on wikipedia\n\n")
            speak("Type the search query in the box to search about it on wikipedia")
            self.msg_entry.configure(state=NORMAL)
            self.text_widget.see(END)
            self.condition=1
        elif(msg.lower() == "search image"):
            self.msg_entry.delete(0,END)
            msg1=f"{sender}: {msg}\n\n"
            self.text_widget.configure(state=NORMAL)
            self.text_widget.insert(END, msg1)
            self.text_widget.insert(END, f"GyaniBot: Type the search query for the image\n\n")
            speak("Type the search query for the image")
            self.msg_entry.configure(state=NORMAL)
            self.text_widget.see(END)
            self.condition=2
        elif(msg.lower()== "show weather"):
            self.condition=4
            self.msg_entry.configure(state=NORMAL)
            msg1=f"{sender}: {msg}\n\n"
            self.text_widget.configure(state=NORMAL)
            self.text_widget.insert(END, msg1)
            self.text_widget.insert(END, f"GyaniBot: Enter the location of which you want to find the weather\n\n")
            speak("Enter the location of which you want to find the weather")
            self.msg_entry.configure(state=NORMAL)
            self.text_widget.see(END)
        elif(msg.lower()=="quiz"):
            self.condition=2
            quiz_thread=Thread(target=quiz,args=(quizBrain,),name="Quiz")
            quiz_thread.start()
            self.msg_entry.delete(0,END)
            
        elif(msg.lower()=="open tic tac toe"):
            self.condition=5
            self.text_widget.configure(state=NORMAL)
            self.text_widget.insert(END,f"{sender}: {msg}\n\n")
            self.text_widget.insert(END,"GyaniBot: Tic Tac Toe Launched\n\n")
            speak("Tic Tac Toe Launched")
            self.text_widget.see(END)
            TicTacToe()
            self.condition=0
        elif(msg.lower()=="what is time"):
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            self.text_widget.configure(state=NORMAL)
            self.text_widget.insert(END,f"GyaniBot: Time is {strTime}\n\n")
            speak(f"GyaniBot: Time is {strTime}")
            self.text_widget.see(END)
        elif(msg.lower()=="open youtube"):
            self.text_widget.configure(state=NORMAL)
            self.text_widget.insert(END,f"GyaniBot: Opening youtube\n\n")
            speak(f"Opening youtube")
            self.text_widget.see(END)
            webbrowser.open("https://www.youtube.com/results?search_query=What+is+chatbot")
        elif(msg.lower()=="open google"):
            self.text_widget.configure(state=NORMAL)
            self.text_widget.insert(END,f"GyaniBot: Opening google\n\n")
            speak(f"Opening google")
            self.text_widget.see(END)
            webbrowser.open("https://www.google.com/search?q=IOToys")
        elif(msg.lower()=="can you please tell your advantages"):
            self.text_widget.configure(state=NORMAL)
            self.text_widget.insert(END,f"1)Proactice assistance\n2)24*7 Availability\n3)An instant help tool\n4)Acts like a learning medium.\n5)Acts like a mode of entertainment.")
            speak(f"1)Proactice assistance\n2)24 by 7 Availability\n3)An instant help tool\n4)Acts like a learning medium.\n5)Acts like a mode of entertainment.")
            self.text_widget.see(END)
        else:
            self.msg_entry.configure(state=DISABLED)    
            self.msg_entry.delete(0,END)
            msg1=f"{sender}: {msg}\n\n"
            self.text_widget.configure(state=NORMAL)
            self.text_widget.insert(END, msg1)
            self.text_widget.configure(state=DISABLED)

            response=abcd(msg)
            msg2=f"GyaniBot: {response}\n\n"
            speak(response)
            self.text_widget.configure(state=NORMAL)
            self.text_widget.insert(END, msg2)
            self.text_widget.configure(state=DISABLED)

            self.text_widget.see(END)

if __name__=="__main__":
    app=chatapplication()
    app.run()
    