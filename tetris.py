from tkinter import *
from tetris_class import *
from random import randint

controls = {
    's' : (0,1), #accélération de la descente --> /!\ à initialiser
    'd' : 1, #mouvement à droite
    'q' : -1 #mouvement à gauche
    }

def mouvements(event):
    if event.char in controls:
        #bloc.direction = controls[event.char]
        if event.char == "s":
            accelerer(event)
        else:
            bloc.mouvement(controls[event.char])
            w.delete(ALL)
            for cell in bloc.corps:
                xc,yc = cell
                w.create_rectangle(xc,yc,xc+jeu.step,yc+jeu.step,fill="green", outline="")

def accelerer(event):
    if event.char == "s":
        if jeu.frame_rate >= 400:
            jeu.frame_rate = jeu.frame_rate // 2

def ralentir(event):
    if event.char == "s":
        if jeu.frame_rate <= 400:
            jeu.frame_rate = 800

def animer():
    bloc.descendre()
    w.delete(ALL)
    for cell in bloc.corps:
        xc,yc = cell
        w.create_rectangle(xc,yc,xc+jeu.step,yc+jeu.step,fill="green", outline="")

    root.after(jeu.frame_rate,animer)



root = Tk()
root.title("Tetris")
#==================================
jeu = Game(400,880,40,800)
block = Block.remplir_corps()
#==================================
root.bind("<KeyRelease>", ralentir)
root.bind("<Key>", mouvements)
w = Canvas(root, width=jeu.largeur, height=jeu.hauteur)
v = StringVar()
v.set(f"{jeu.frame_rate}")
w.pack()
Label(root, textvariable=v).pack()
animer()
root.mainloop()
