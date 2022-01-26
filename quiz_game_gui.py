from tkinter import *
from tkinter import font


def start_again():
    global Score,Question_no
    
    Score = 0
    Question_no = 1
    next_b.config(text="next")
    val1.set(0)
    val2.set(0)
    val3.set(0)
    question.config(text=Questions[Question_no-1])
    option1.config(text=Options[Question_no-1][0])
    option2.config(text=Options[Question_no-1][1])
    option3.config(text=Options[Question_no-1][2])
    play_again.place_forget()
    score_output.place_forget()
    root.pack()
    
def next():
    global Score,Question_no
    if(val1.get()):
        selected_option = 1
    elif(val2.get()):
        selected_option = 2
    elif(val3.get()):
        selected_option = 3
    else:
        selected_option = -1

    if(Answers[Question_no-1] == selected_option):
        Score += 1

    if(Question_no == Total_No_Questions-1):
        next_b.config(text="Submit")
    Question_no = Question_no + 1

    

    if(Question_no > Total_No_Questions):
        root.pack_forget()
        score_output.place(relx=.45,rely=.45)
        play_again.place(relx = .45)
        score_output.config(text = "Score: " +str(Score))

    else:
        val1.set(0) 
        val2.set(0) 
        val3.set(0) 
        question.config(text=Questions[Question_no-1])
        option1.config(text=Options[Question_no-1][0])
        option2.config(text=Options[Question_no-1][1])
        option3.config(text=Options[Question_no-1][2])

def Check(Option):
    if(Option == 1):
        # val1.set(1)
        val2.set(0)
        val3.set(0)
        
        
    elif(Option == 2):
        val1.set(0)
        # val2.set(1)
        val3.set(0)
      
    elif(Option == 3):
        val1.set(0)
        val2.set(0)
        # val3.set(1)

Questions = ["What technology is used to record cryptocurrency transactions?" , 
            "What tool would you use to reduce the digital image size?" , 
            "Which computer language is the most widely used?"]
Options = [["Digital wallet","Mining", "Blockchain"],
            ["Filter","Crop", "Rotate"],
            ["C++","Python", "Javascript"]]

Answers = [3 , 2 , 3]

Score = 0
Total_No_Questions = 3
Question_no = 1

Win= Tk()
Win.title("Quiz Game")

root = Frame(Win)
root.pack()

question = Label(root,width = 60,font=(10),text=Questions[0])
question.pack(fill=X)

val1 = IntVar()
val2 = IntVar()
val3 = IntVar()

option1 = Checkbutton(root,variable=val1,text=Options[0][0],command=lambda:Check(1))
option1.pack()

option2 = Checkbutton(root,variable=val2,text=Options[0][1],command=lambda:Check(2))
option2.pack()

option3 = Checkbutton(root,variable=val3,text=Options[0][2],command=lambda:Check(3))
option3.pack()

next_b = Button(root , text = "Next",command=next)
next_b.pack()

score_output = Label(Win,font=(50))
score_output.place_forget()

play_again = Button(Win,text= "Play Again",command=start_again)
play_again.place_forget()

Win.mainloop()