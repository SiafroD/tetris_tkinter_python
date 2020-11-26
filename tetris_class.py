from random import randint

class Shapes:
    def __init__(self):
        self.formes = (
            [(0, 0), (1, 0), (0, 1), (1, 1)],     # Carre
            [(0, 0), (0, 1), (0, 2), (0, 3)],     # Ligne
            [(1, 0), (1, 1), (1, 2), (0, 2)],     # J
            [(0, 0), (0, 1), (0, 2), (1, 2)],     # L
            [(0, 1), (1, 1), (1, 0), (2, 0)],     # S
            [(0, 0), (1, 0), (1, 1), (2, 1)],     # Z
            [(1, 0), (0, 1), (1, 1), (2, 1)])     # T inversé
        self.couleurs = [
            "red",          #Carre
            "cyan",         #Ligne
            "purple4",      #J
            "blue2",        #L
            "dark orange",  #S
            "gold",         #Z
            "green2"]       #T inversé


class Block:
    def __init__(self, game):
        self.game = game #rajouter les paramètres de Game
        self.apparences = Shapes()
        self.cd = 0
        gen_rand = randint(0,len(self.apparences.formes)-1)
        apparence = self.apparences.formes[gen_rand]
        couleur = self.apparences.couleurs[gen_rand]
        self.cd = self.game.coo_start
        self.corps = [
            [(apparence[0][0]*self.game.step+self.cd[0]),(apparence[0][1]*self.game.step+self.cd[1])],
            [(apparence[1][0]*self.game.step+self.cd[0]),(apparence[1][1]*self.game.step+self.cd[1])],
            [(apparence[2][0]*self.game.step+self.cd[0]),(apparence[2][1]*self.game.step+self.cd[1])],
            [(apparence[3][0]*self.game.step+self.cd[0]),(apparence[3][1]*self.game.step+self.cd[1])]]
        self.couleur = couleur
        self.corps_precedent = []

    def reset_block(self):
        '''
        Quand un bloc finit bloqué dans sa descente, il devient partie du plateau/devient solide (/!\ à initialiser). Un nouveau
        bloc se génère donc, avec cette méthode reset_block.
        '''
        gen_rand = randint(0,len(self.apparences.formes)-1)
        apparence = self.apparences.formes[gen_rand]
        couleur = self.apparences.couleurs[gen_rand]

        self.cd = self.game.coo_start

        self.corps = [
            [(apparence[0][0]*self.game.step+self.cd[0]),(apparence[0][1]*self.game.step+self.cd[1])],
            [(apparence[1][0]*self.game.step+self.cd[0]),(apparence[1][1]*self.game.step+self.cd[1])],
            [(apparence[2][0]*self.game.step+self.cd[0]),(apparence[2][1]*self.game.step+self.cd[1])],
            [(apparence[3][0]*self.game.step+self.cd[0]),(apparence[3][1]*self.game.step+self.cd[1])]]
        self.couleur = couleur
        self.corps_precedent = []
        

    def descendre(self):
        '''
        Fonction appelée en continu dans le programme, elle ajoute au y de chaque case du corps de notre bloc le step de la partie
        contenu dans l'attribut game, faisant ainsi continuellement descendre la pièce sur le terrain de jeu.

        On utilise la liste initialement vide "corps_temp" dans laquelle on place les coordonnées de chaque case de notre bloc
        une fois le déplacement accompli. Si une case n'est pas valide (en dehors du plateau), elle n'entre pas dans corps_temp.
        On ne modifie self.corps que si corps_temp a une longueur de 4, soit si toutes les cases, une fois le déplacement
        accompli, ont une position valide.
        '''

        self.corps_precedent = self.corps
        n = len(self.corps)
        verif = True
        corps_temp = []
        #print(self.corps) --> utile pour analyser les coo des cases et vérifier que la collision avec le fond fonctionne.
        for i in range(n):
            x,y = self.corps[i]
            y += self.game.step
  
            if y<=self.game.hauteur-self.game.step:
                if self.game.plateau[x//self.game.step][y//self.game.step] == 0:
                    corps_temp.append([x,y])
            
        if len(corps_temp)==4:
            self.corps = corps_temp

        else:
            verif = False
        return verif

    def mouvement(self,direction):
        '''
        Fonction lié à un event dans le programme principal. Lorsque la touche q ou d (prochainement s) est pressé, la fonction
        se lance avec la valeur associé à la touche
        Si direction=1, l'ensemble des pièces formant le bloc se décallent de 1*step en x.
        Si direction=-1, l'ensemble des pièces formant le bloc se décallent de -1*step en x.

        On utilise la liste initialement vide "corps_temp" dans laquelle on place les coordonnées de chaque case de notre bloc
        une fois le déplacement accompli. Si une case n'est pas valide (en dehors du plateau), elle n'entre pas dans corps_temp.
        On ne modifie self.corps que si corps_temp a une longueur de 4, soit si toutes les cases, une fois le déplacement
        accompli, ont une position valide.
        '''

        self.corps_precedent = self.corps
        n = len(self.corps)
        corps_temp = []
        for i in range(n):
            x,y = self.corps[i]
            x += direction*self.game.step

            if 0<=x<=self.game.largeur-self.game.step:
                if self.game.plateau[x//self.game.step][y//self.game.step] == 0:
                    corps_temp.append([x,y])

        if len(corps_temp)==4:
            self.corps = corps_temp


class Game:
    def __init__(self,l,h,step,f_r):
        self.largeur = l
        self.hauteur = h
        self.step = step
        self.frame_rate = f_r

        self.score = 0
        self.coo_start = [self.largeur//2,0]
        #self.plateau = [[0]*22]*10
        self.plateau = [
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
        #Si une case = 0, elle n'est pas occupée. Sinon, elle l'est. A noter qu'on parle ici des blocs posés, pas des pièces qui
        #descendent


    def remplir_plateau(self,block):
        for cell in block:
            xc,yc = cell
            self.plateau[xc//self.step][yc//self.step] = 1


    def décaler():
        '''
        Lorsqu'une ligne de self.plateau est pleine, cette fonction vide celle-ci et décalle toute les lignes situées au-dessus
        d'un cran en y (= +step)

        /!\ à créer prochainement
        '''
        pass
