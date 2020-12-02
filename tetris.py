from tkinter import *
from tetris_class import Game, Shapes, Block
from random import randint

controls = {
    's' : (0,1),    #accélération de la descente. Valeur associée inutile
    'd' : 1,        #mouvement à droite
    'q' : -1,       #mouvement à gauche
    'o' : -1,       #rotation -90°
    'p' : 1         #rotation 90°
    }

def mouvements(event):
    if event.char in controls:
        if event.char == "s":
            accelerer(event)
        else:
            if event.char in ['q','d']:
                block.mouvement(controls[event.char])
            elif event.char in ['o','p']:
                block.rotation(controls[event.char])
            for cell in block.corps_precedent:
                xc,yc = cell
                w.create_rectangle(xc,yc,xc+jeu.step,yc+jeu.step,fill="gray2", outline="")
            for cell in block.corps:
                xc,yc = cell
                w.create_rectangle(xc,yc,xc+jeu.step,yc+jeu.step,fill=f"{block.couleur}", outline="")
       

def accelerer(event):
    if event.char == "s":
        if jeu.frame_rate >= 200:
            jeu.frame_rate = jeu.frame_rate // 2

def ralentir(event):
    if event.char == "s":
        if jeu.frame_rate <= 200:
            jeu.frame_rate = 400


def animer():
    ver = 0
    for i in range(len(jeu.plateau)):
        if jeu.plateau[i][0] != 0:
            ver+=1

    if ver!=0:
        w.delete(ALL)
        for i in range(len(jeu.game_over)):
            for j in range(len(jeu.game_over[i])): #Les longues conditions ci-dessous pourront à terme être déplacé dans la class Game() pour rendre le tout plus propre et organisé.
                if (i==0 and jeu.game_over[i][j] in [(2,2),(3,2)]) or (i==3 and jeu.game_over[i][j] in [(2,17),(2,18),(2,19.5),(3,17),(3,19.5)]) or (i==6 and jeu.game_over[i][j] in [(7,12),(7,13),(7,14.5),(8,12),(8,14.5)]) or (i==1 and jeu.game_over[i][j] == (2,8.5)):
                    x,y = jeu.game_over[i][j]
                    w.create_rectangle(x*jeu.step,y*jeu.step,x*jeu.step+jeu.step,y*jeu.step+(0.5*jeu.step),fill="red",outline="")

                elif i==2 and jeu.game_over[i][j] in [(2,12.5),((2+2/3),12.5)]:
                    x,y = jeu.game_over[i][j]
                    w.create_rectangle(x*jeu.step,y*jeu.step,x*jeu.step+(1/3*jeu.step),y*jeu.step+jeu.step,fill="red",outline="")

                else:
                    x,y = jeu.game_over[i][j]
                    w.create_rectangle(x*jeu.step,y*jeu.step,x*jeu.step+jeu.step,y*jeu.step+jeu.step,fill="red",outline="")

        v.set(f"Your score was : {jeu.score}")
    
    else:
        ver2 = block.descendre()
        if ver2:
            for cell in block.corps_precedent:
                xc,yc = cell
                w.create_rectangle(xc,yc,xc+jeu.step,yc+jeu.step,fill="gray2", outline="")
            for cell in block.corps:
                xc,yc = cell
                w.create_rectangle(xc,yc,xc+jeu.step,yc+jeu.step,fill=f"{block.couleur}", outline="")
        else:
            jeu.remplir_plateau(block.corps,block.couleur)
            v.set(f"Score : {jeu.score}")
            ver3 = jeu.decaler(block.corps)
            if ver3:
                w.delete(ALL)
                v.set(f"Score : {jeu.score}")
                for i in range(len(jeu.plateau)):
                    for j in range(len(jeu.plateau[i])):
                        if jeu.plateau[i][j] != 0:
                            w.create_rectangle(i*jeu.step,j*jeu.step,i*jeu.step+jeu.step,j*jeu.step+jeu.step,fill=f"{jeu.plateau[i][j]}", outline="")

            block.reset_block()

        root.after(jeu.frame_rate,animer)


root = Tk()
root.title("Tetris")
#==================================
jeu = Game(200,440,20,400)
block = Block(jeu)
#==================================
root.bind("<KeyRelease>", ralentir)
root.bind("<Key>", mouvements)
w = Canvas(root, width=jeu.largeur, height=jeu.hauteur)
w.config(bg="gray2")
v = StringVar()
v.set(f"Score : {jeu.score}")
w.pack()
Label(root, textvariable=v).pack()
animer()
root.mainloop()
