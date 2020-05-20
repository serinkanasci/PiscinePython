from tkinter import *
from PIL import ImageTk, Image
import pandas as pd

def EnterPlayer():
    file = open("Game.txt","a") 
    file.write(saisie.get() + "-")
    saisie.set("")
    file.close()

# def EnterScore():
#     file = open("Game.txt","a") 
#     file.write(score.get() + "\n")
#     file.close()

def GetTopThree():
    data = pd.read_csv('Game.txt', sep="-", header=None)
    data.columns = ["Username", "Score"]
    ScoreBoardList.insert(END, data.nlargest(3, columns=['Score']))


fen = Tk()
fen.geometry("800x300")
saisie = StringVar()

image = Image.open("game-logo.jpg") 
image = image.resize((500, 500), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(image) 
 
canvas = Canvas() 
canvas.create_image(180,150, image=photo)

Scoreboard = Label(fen, text="Score", font = ("Arial",14,"bold"))
ScoreBoardList = Text(fen, width=40, height=5)
Play = Button(fen, text="JOUER", command=EnterPlayer)
# Logo = Label(fen, image="game-logo.jpg")
text = Entry(textvariable=saisie, width=30)

GetTopThree()
# Scoreboard.grid(row = 0, column = 1, columnspan = 1, rowspan = 1)
# ScoreBoardList.grid(row = 1, column = 1, columnspan = 1, rowspan = 1)
# text.grid(row = 2, column = 1, columnspan = 1, rowspan = 1)
# Play.grid(row = 3, column = 1, columnspan = 1, rowspan = 1)
# canvas.grid(row = 0, column = 0, columnspan = 1, rowspan = 1)
Scoreboard.place(x = 535, y = 10)
ScoreBoardList.place(x = 420, y = 50)
text.place(x = 475, y = 150)
Play.place(x = 535, y = 175)
canvas.place(x = 10, y = 10)  
fen.mainloop()
