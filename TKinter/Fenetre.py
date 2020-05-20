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
fen.geometry("800x800")
saisie = StringVar()

image = Image.open("game-logo.jpg") 
image = image.resize((500, 500), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(image) 
 
canvas = Canvas() 
canvas.create_image(180,150, image=photo)
canvas.pack(anchor="nw") 

Scoreboard = Label(fen, text="Score", font = ("Arial",14,"bold"))
ScoreBoardList = Text(fen, width=40, height=5)
Play = Button(fen, text="JOUER", command=EnterPlayer)
# Logo = Label(fen, image="game-logo.jpg")
text = Entry(textvariable=saisie, width=30)

GetTopThree()
# Logo.pack()
Scoreboard.pack(anchor="ne")
ScoreBoardList.pack()
text.pack()
Play.pack()
fen.mainloop()
