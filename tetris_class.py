from random import randint

class Shapes:
    def __init__(self):
        self.formes = (
            [(0, 0), (1, 0), (0, 1), (1, 1)],     # Carre
            [(0, 0), (1, 0), (2, 0), (3, 0)],     # Ligne
            [(2, 0), (0, 1), (1, 1), (2, 1)],     # J
            [(0, 0), (0, 1), (1, 1), (2, 1)],     # L
            [(0, 1), (1, 1), (1, 0), (2, 0)],     # S
            [(0, 0), (1, 0), (1, 1), (2, 1)],     # Z
            [(1, 0), (0, 1), (1, 1), (2, 1)])     # T inversé



class Block:
    def __init__(self,corps,game):
        self.corps = corps
        self.game = game

    def descendre(self): #fonction continue, permettant à la pièce de descendre
        n = len(self.corps)
        for i in range(n):
            x,y = self.corps[i]
            y += self.game.step
            self.corps[i] = [x,y]

    def mouvement(self): #fonction lié à un event, permettant à la pièce d'aller à gauche ou à droite
        



class Game:
    def __init__(self,l,h,step,f_r):
        self.largeur = l
        self.hauteur = h
        self.step = step
        self.frame_rate = f_r

        self.score = 0
        self.coo_start = [self.largeur//2,0]
        self.plateau = [[0]*10]*22
        #Si une case = 0, elle n'est pas occupée. Sinon, elle l'est. A noter qu'on parle ici des blocs posés, pas des pièces qui
        #descendent


    def décaler(): #quand une ligne est pleine, décalage d'une ligne de tous les blocs "solides"
        pass
