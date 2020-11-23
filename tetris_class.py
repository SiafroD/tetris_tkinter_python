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

    def creer_corps(self):
        '''
        Une fois appelée dans le programme principal, cette fonction vient initialiser ou réinitialiser l'attribut corps de la
        class Block, à partir des coordonnées de départ de l'attribut game ainsi que d'une forme tiré au hasard dans la class
        Shapes. 
        /!\ Pour l'heure, cette fonction est inactive et le corps est défini directement dans le programme principal.
        '''
        pass

    def descendre(self):
        ''' 
        Fonction appelée en continu dans le programme, elle ajoute au y de chaque case du corps de notre bloc le step de la partie
        contenu dans l'attribut game, faisant ainsi continuellement descendre la pièce sur le terrain de jeu.

        On utilise la liste initialement vide "corps_temp" dans laquelle on place les coordonnées de chaque case de notre bloc
        une fois le déplacement accompli. Si une case n'est pas valide (en dehors du plateau), elle n'entre pas dans corps_temp.
        On ne modifie self.corps que si corps_temp a une longueur de 4, soit si toutes les cases, une fois le déplacement
        accompli, ont une position valide.
        '''
        n = len(self.corps)
        corps_temp = []
        #print(self.corps) --> utile pour analyser les coo des cases et vérifier que la collision avec le fond fonctionne.
        for i in range(n):
            x,y = self.corps[i]
            y += self.game.step
            if y<=self.game.hauteur-self.game.step:
                corps_temp.append([x,y])

        if len(corps_temp)==4:
            self.corps = corps_temp

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

        n = len(self.corps)
        corps_temp = []
        for i in range(n):
            x,y = self.corps[i]
            x += direction*self.game.step
            if 0<=x<=self.game.largeur-self.game.step:
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
        self.plateau = [[0]*22]*10 
        #Si une case = 0, elle n'est pas occupée. Sinon, elle l'est. A noter qu'on parle ici des blocs posés, pas des pièces qui
        #descendent


    def décaler():
        '''
        Lorsqu'une ligne de self.plateau est pleine, cette fonction vide celle-ci et décalle toute les lignes situées au-dessus
        d'un cran en y (= +step)

        /!\ à créer prochainement
        '''
        pass
