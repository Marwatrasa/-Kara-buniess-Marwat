from tkinter import*
from PIL import Image,ImageTk
from random import randint

root = Tk()
root.title("game")
root.configure(background="#9b59b6")

rock_img =ImageTk.PhotoImage(Image.open("rock-user.Png"))
paper_img =ImageTk.PhotoImage(Image.open("paper-user.Png"))
scissor_img =ImageTk.PhotoImage(Image.open("scissor-user.Png"))
rock_img_comp =ImageTk.PhotoImage(Image.open("rock.Png"))
paper_img_comp =ImageTk.PhotoImage(Image.open("paper.Png"))
scissor_img_comp =ImageTk.PhotoImage(Image.open("scissor.Png"))

user_label = Label(root,image=scissor_img,bg="#9b59b6")
comp_label= Label(root,image=scissor_img_comp,bg="#9b59b6")
comp_label.grid(row=1,column=0)
user_label.grid(row=1,column=4)

#scores
playerscore = Label(root,text=0,font=100,bg="#9b59b6",fg="white")
computerscore= Label(root,text=0,font=100,bg="#9b59b6",fg="white")
computerscore.grid(row=1,column=1)
playerscore.grid(row=1,column=3)

#Indicator
user_indicator= Label(root,font=50,text="USER",bg="#9b59b6",fg="white")
comp_indicator= Label(root,font=50,text="CCOMPUTER",bg="#9b59b6",fg="white")
user_indicator.grid(row=0,column=3)
comp_indicator.grid(row=0,column=1)

#messages

msg=Label(root,font=50,bg="#9b59b6",fg="white")
msg.grid(row=3,column=2)
#update messages
def updateMessage(x):
    msg["text"]=x
#update user score

def updateUserScore():
    score =int(playerscore["text"])
    score +=1
    playerscore ["text"]=str(score)
#update computer score
def updateCompscore():
    score =int (computerscore["text"])
    score +=1
    computerscore ["text"]=str(score)
#check winner
def checkWin(player,computer):
    if player== computer:
        updateMessage("Its a tie!!!")
    elif player== "rock":
        if computer == "paper":
            updateMessage("You Loose")
            updateCompscore()
        else:
            updateMessage("You Win")
            updateUserScore ()
    elif player == "paper":
        if computer== "scissor":
            updateMessage("you loose")
            updateCompscore()
        else:
            updateMessage("You Win")
            updateUserScore()
    elif player== "scissor":
        if computer =="rock":
            updateMessage("you Loose")
            updateCompscore()
        else:
            updateMessage("You Win")
            updateUserScore()
    else:
        pass       


choices =["rock","paper","scissor"]



def updateChice(x):
    
    if x=="rock":
        user_label.configure(image=rock_img)
    elif x=="paper":
        user_label.configure(image=paper_img)
    else: 
        user_label.configure(image=scissor_img)





    compChoice= choices[randint(0,2)]
    if compChoice =="rock":
        comp_label.configure(image=rock_img_comp)
    elif compChoice =="paper":
        comp_label.configure(image=paper_img_comp)
    else:
        comp_label.configure(image=scissor_img_comp)
    checkWin(x,compChoice)



#buttons
rock=Button(root,width=20,height=2,text="ROCK",bg="#FF3E4D",fg="white",command= lambda: updateChice("rock")).grid(row=2,column=1)
paper=Button(root,width=20,height=2,text="PAPER",bg="#FAD02E",fg="white",command= lambda: updateChice("paper")).grid(row=2,column=2)
scissor=Button(root,width=20,height=2,text="SCISSOR",bg="#0ABDE3",fg="white",command= lambda: updateChice("scissor")).grid(row=2,column=3)

root.mainloop()
