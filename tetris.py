from tkinter import *
from tetris_class import Game, Shapes, Block
from random import randint

controls = {
    's' : (0,1), #accélération de la descente. Valeur associée inutile
    'd' : 1, #mouvement à droite
    'q' : -1 #mouvement à gauche
    }

def mouvements(event):
    if event.char in controls:
        #block.direction = controls[event.char]
        if event.char == "s":
            accelerer(event)
        else:
            block.mouvement(controls[event.char])
            for cell in block.corps_precedent:
                xc,yc = cell
                w.create_rectangle(xc,yc,xc+jeu.step,yc+jeu.step,fill="gray2", outline="")
            for cell in block.corps:
                xc,yc = cell
                w.create_rectangle(xc,yc,xc+jeu.step,yc+jeu.step,fill=f"{block.couleur}", outline="")

def accelerer(event):
    if event.char == "s":
        if jeu.frame_rate >= 400:
            jeu.frame_rate = jeu.frame_rate // 2

def ralentir(event):
    if event.char == "s":
        if jeu.frame_rate <= 400:
            jeu.frame_rate = 800

def animer():
    ver = block.descendre()
    if ver:
        for cell in block.corps_precedent:
            xc,yc = cell
            w.create_rectangle(xc,yc,xc+jeu.step,yc+jeu.step,fill="gray2", outline="")
        for cell in block.corps:
            xc,yc = cell
            w.create_rectangle(xc,yc,xc+jeu.step,yc+jeu.step,fill=f"{block.couleur}", outline="")
    else:
        jeu.remplir_plateau(block.corps)
        block.reset_block()
    root.after(jeu.frame_rate,animer)


root = Tk()
root.title("Tetris")
#==================================
jeu = Game(200,440,20,800)
block = Block(jeu)
#==================================
root.bind("<KeyRelease>", ralentir)
root.bind("<Key>", mouvements)
w = Canvas(root, width=jeu.largeur, height=jeu.hauteur)
w.config(bg="gray2")
v = StringVar()
v.set(f"{jeu.frame_rate}")
w.pack()
Label(root, textvariable=v).pack()
animer()
root.mainloop()
