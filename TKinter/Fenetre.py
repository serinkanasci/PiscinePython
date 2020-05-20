from tkinter import Canvas,StringVar,Label,Text,Button,Entry,END,Toplevel,Frame,Tk
from PIL import ImageTk, Image
import pandas as pd

class GameMenu():
    def __init__(self, master):
        self.master = master
        self.master.geometry("800x300")
        self.saisie = StringVar()

        self.image = Image.open("game-logo.jpg") 
        self.image = self.image.resize((500, 500), Image.ANTIALIAS)
        self.photo = ImageTk.PhotoImage(self.image) 
        
        self.canvas = Canvas() 
        self.canvas.create_image(180,150, image=self.photo)

        self.Scoreboard = Label(self.master, text="Score", font = ("Arial",14,"bold"))
        self.ScoreBoardList = Text(self.master, width=40, height=8)
        self.Play = Button(self.master, text="JOUER", command=self.combine_funcs(self.EnterPlayer,self.hide, self.LaunchGame))
        self.text = Entry(textvariable=self.saisie, width=30)

        self.GetTopFive()
        self.Scoreboard.place(x = 535, y = 10)
        self.ScoreBoardList.place(x = 420, y = 50)
        self.text.place(x = 475, y = 200)
        self.Play.place(x = 535, y = 225)
        self.canvas.place(x = 10, y = 10)

    def EnterPlayer(self):
        file = open("Game.txt","a") 
        file.write(self.saisie.get() + "-")
        self.saisie.set("")
        file.close()

    # def EnterScore():
    #     file = open("Game.txt","a") 
    #     file.write(score.get() + "\n")
    #     file.close()

    def GetTopFive(self):
        data = pd.read_csv('Game.txt', sep="-", header=None)
        data.columns = ["Username", "Score"]
        self.ScoreBoardList.insert(END, data.nlargest(6, columns=['Score']))

    def combine_funcs(self,*funcs):
        def combined_func(*args, **kwargs):
            for f in funcs:
                f(*args, **kwargs)
        return combined_func
    
    def hide(self):
        self.master.iconify()
            
    def show(self):
        self.master.update()
        self.master.deiconify()

    def LaunchGame(self):
        MyGame = Toplevel(self.master)
        Game(MyGame)

class Game():
    def __init__(self, master):
        self.master = master
        self.master.geometry("500x135")

        F1 = Frame(self.master, bg='grey', width=450, height=50, pady=3)
        # F2 = Frame(self.master, bg='white', width=450, height=50, pady=3)
        # F3 = Frame(self.master, bg='grey', width=450, height=50, pady=3)
        # F4 = Frame(self.master, bg='white', width=450, height=50, pady=3)     

        model_label = Label(F1, text="Model")
        model_label.grid(row=0, rowspan=3, columnspan=3)
            
            
        # Label(F1, text="").grid(row = 0, column = 0, columnspan = 10, rowspan = 5)
        # Label(F2, text="", bg = 'white').grid(row = 5, column = 0, columnspan = 10, rowspan = 5)
        # Label(F3, text="", bg = 'grey').grid(row = 10, column = 0, columnspan = 10, rowspan = 5)
        # Label(F4, text="", bg = 'white').grid(row = 15, column = 0, columnspan = 10, rowspan = 5)

        # self.img = Image.open("skater.jpg") 
        # self.img = self.img.resize((10, 10), Image.ANTIALIAS)
        # self.pic = ImageTk.PhotoImage(self.img) 
        
        # self.canv = Canvas()
        # self.canv.create_image(0,0, image=self.pic)
        # self.canv.grid(row = 0, column = 0, columnspan = 5, rowspan = 3)
        # self.master.show()


class Main():
    fen = Tk()
    GameMenu(fen)
    fen.mainloop()


# Scoreboard.grid(row = 0, column = 1, columnspan = 1, rowspan = 1)
# ScoreBoardList.grid(row = 1, column = 1, columnspan = 1, rowspan = 1)
# text.grid(row = 2, column = 1, columnspan = 1, rowspan = 1)
# Play.grid(row = 3, column = 1, columnspan = 1, rowspan = 1)
# canvas.grid(row = 0, column = 0, columnspan = 1, rowspan = 1)