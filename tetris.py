from tkinter import *
from tetris_class import *
from random import randint


def animer():
    #print(bloc.corps[0])
    bloc.descendre()
    w.delete(ALL)
    for cell in bloc.corps:
        xc,yc = cell
        w.create_rectangle(xc,yc,xc+jeu.step,yc+jeu.step,fill="green", outline="")
    
    root.after(jeu.frame_rate,animer) 



root = Tk()
root.title("Tetris")
#==================================
jeu = Game(400,880,40,750)
apparence = Shapes().formes[randint(0,len(Shapes().formes)-1)]
bloc = Block([
    [(apparence[0][0]*jeu.step+jeu.coo_start[0]),(apparence[0][1]*jeu.step+jeu.coo_start[1])],
    [(apparence[1][0]*jeu.step+jeu.coo_start[0]),(apparence[1][1]*jeu.step+jeu.coo_start[1])],
    [(apparence[2][0]*jeu.step+jeu.coo_start[0]),(apparence[2][1]*jeu.step+jeu.coo_start[1])],
    [(apparence[3][0]*jeu.step+jeu.coo_start[0]),(apparence[3][1]*jeu.step+jeu.coo_start[1])]],jeu)
#==================================
w = Canvas(root, width=jeu.largeur, height=jeu.hauteur)
v = StringVar()
v.set("")
w.pack()
Label(root, textvariable=v).pack()
animer()
root.mainloop()