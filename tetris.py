from tkinter import *
from tetris_class import *
from random import randint

controls = {
    #'s' : (0,1), #accélération de la descente --> /!\ à initialiser
    'd' : 1, #mouvement à droite
    'q' : -1 #mouvement à gauche
    }

def mouvements(event):
    if event.char in controls:
        #bloc.direction = controls[event.char]
        bloc.mouvement(controls[event.char])
        w.delete(ALL)
        for cell in bloc.corps:
            xc,yc = cell
            w.create_rectangle(xc,yc,xc+jeu.step,yc+jeu.step,fill="green", outline="")

def accélérer(event):
    if event.char == "s":
        if jeu.frame_rate >= 400:
            jeu.frame_rate = jeu.frame_rate // 2

def ralentir(event):
    if event.char == "s":
        if jeu.frame_rate <= 400:
            jeu.frame_rate = jeu.frame_rate * 2

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
apparence = Shapes().formes[randint(0,len(Shapes().formes)-1)]
bloc = Block([
    [(apparence[0][0]*jeu.step+jeu.coo_start[0]),(apparence[0][1]*jeu.step+jeu.coo_start[1])],
    [(apparence[1][0]*jeu.step+jeu.coo_start[0]),(apparence[1][1]*jeu.step+jeu.coo_start[1])],
    [(apparence[2][0]*jeu.step+jeu.coo_start[0]),(apparence[2][1]*jeu.step+jeu.coo_start[1])],
    [(apparence[3][0]*jeu.step+jeu.coo_start[0]),(apparence[3][1]*jeu.step+jeu.coo_start[1])]],jeu)
#==================================
root.bind("<Key>", mouvements)
root.bind("<KeyPress>", accélérer)
root.bind("<KeyRelease>", ralentir)
w = Canvas(root, width=jeu.largeur, height=jeu.hauteur)
v = StringVar()
v.set(f"{jeu.frame_rate}")
w.pack()
Label(root, textvariable=v).pack()
animer()
root.mainloop()
