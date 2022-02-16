from random import randint

class Shapes:
    def __init__(self):
        self.formes = (
            [[(0, 0), (1, 0), (0, 1), (1, 1)],     # Carre
            [(1, 0), (1, 1), (0, 0), (0, 1)],
            [(1, 1), (0, 1), (1, 0), (0, 0)],
            [(0, 1), (0, 0), (1, 1), (1, 0)]],

            [[(0, 0), (0, 1), (0, 2), (0, 3)],     # Ligne
            [(3, 0), (2, 0), (1, 0), (0, 0)],
            [(0, 3), (0, 2), (0, 1), (0, 0)],
            [(0, 0), (1, 0), (2, 0), (3, 0)]],

            [[(1, 0), (1, 1), (1, 2), (0, 2)],     # J
            [(2, 1), (1, 1), (0, 1), (0, 0)],
            [(0, 2), (0, 1), (0, 0), (1, 0)],
            [(0, 0), (1, 0), (2, 0), (2, 1)]],

            [[(0, 0), (0, 1), (0, 2), (1, 2)],     # L
            [(2, 0), (1, 0), (0, 0), (0, 1)],
            [(1, 2), (1, 1), (1, 0), (0, 0)],
            [(0, 1), (1, 1), (2, 1), (2, 0)]],

            [[(0, 1), (1, 1), (1, 0), (2, 0)],     # S
            [(0, 0), (0, 1), (1, 1), (1, 2)],
            [(2, 0), (1, 0), (1, 1), (0, 1)],
            [(1, 2), (1, 1), (0, 1), (0, 0)]],

            [[(0, 0), (1, 0), (1, 1), (2, 1)],     # Z
            [(1, 0), (1, 1), (0, 1), (0, 2)],
            [(2, 1), (1, 1), (1, 0), (0, 0)],
            [(0, 2), (0, 1), (1, 1), (1, 0)]],

            [[(1, 0), (0, 1), (1, 1), (2, 1)],     # T inversé
            [(1, 1), (0, 0), (0, 1), (0, 2)],
            [(1, 1), (2, 0), (1, 0), (0, 0)],
            [(0, 1), (1, 2), (1, 1), (1, 0)]])


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
        self.game = game #rajoute les paramètres de Game
        self.apparences = Shapes()
        gen_rand = randint(0,len(self.apparences.formes)-1)
        apparence = self.apparences.formes[gen_rand]
        couleur = self.apparences.couleurs[gen_rand]

        self.apparence = apparence
        self.id_f = 0

        self.cd = self.game.coo_start
        self.corps = [
            [(self.apparence[self.id_f][0][0]*self.game.step+self.cd[0]),(self.apparence[self.id_f][0][1]*self.game.step+self.cd[1])],
            [(self.apparence[self.id_f][1][0]*self.game.step+self.cd[0]),(self.apparence[self.id_f][1][1]*self.game.step+self.cd[1])],
            [(self.apparence[self.id_f][2][0]*self.game.step+self.cd[0]),(self.apparence[self.id_f][2][1]*self.game.step+self.cd[1])],
            [(self.apparence[self.id_f][3][0]*self.game.step+self.cd[0]),(self.apparence[self.id_f][3][1]*self.game.step+self.cd[1])]]
        self.couleur = couleur
        self.corps_precedent = []


    def reset_block(self):
        '''
        Quand un bloc se bloque dans sa descente, il devient partie du plateau/devient solide. Un nouveau
        bloc se génère donc, avec cette méthode reset_block.
        '''
        gen_rand = randint(0,len(self.apparences.formes)-1)
        apparence = self.apparences.formes[gen_rand]
        couleur = self.apparences.couleurs[gen_rand]
        self.apparence = apparence
        self.id_f = 0

        self.cd = self.game.coo_start

        self.corps = [
            [(self.apparence[self.id_f][0][0]*self.game.step+self.cd[0]),(self.apparence[self.id_f][0][1]*self.game.step+self.cd[1])],
            [(self.apparence[self.id_f][1][0]*self.game.step+self.cd[0]),(self.apparence[self.id_f][1][1]*self.game.step+self.cd[1])],
            [(self.apparence[self.id_f][2][0]*self.game.step+self.cd[0]),(self.apparence[self.id_f][2][1]*self.game.step+self.cd[1])],
            [(self.apparence[self.id_f][3][0]*self.game.step+self.cd[0]),(self.apparence[self.id_f][3][1]*self.game.step+self.cd[1])]]
        self.couleur = couleur
        self.corps_precedent = []


    def descendre(self):
        '''
        Fonction appelée en continu dans le programme, elle ajoute au y de chaque case du corps de notre bloc le step de la partie
        contenu dans l'attribut game, faisant ainsi continuellement descendre la pièce sur le terrain de jeu.

        On utilise la liste initialement vide "corps_temp" dans laquelle on place les coordonnées de chaque case de notre bloc
        une fois le déplacement réalisé. Si une case n'est pas valide (en dehors du plateau), elle n'entre pas dans corps_temp.
        On ne modifie self.corps que si corps_temp a une longueur de 4, soit si toutes les cases, une fois le déplacement
        accompli, ont une position valide.
        '''

        self.corps_precedent = self.corps
        n = len(self.corps)
        verif = True
        corps_temp = []
        for i in range(n):
            x,y = self.corps[i]
            y += self.game.step

            if y<=self.game.hauteur-self.game.step:
                if self.game.plateau[x//self.game.step][y//self.game.step] == 0:
                    corps_temp.append([x,y])

        if len(corps_temp)==4:
            self.corps = corps_temp
            x,y = self.cd
            y+=self.game.step
            self.cd = [x,y]

        else:
            verif = False
        return verif

    def mouvement(self,direction):
        '''
        Fonction liée à un event dans le programme principal. Lorsque la touche q ou d est pressée, la fonction
        se lance avec la valeur associée à la touche
        Si direction=1, l'ensemble des pièces formant le bloc se décalent de 1*step en x.
        Si direction=-1, l'ensemble des pièces formant le bloc se décalent de -1*step en x.

        On utilise la liste initialement vide "corps_temp" dans laquelle on place les coordonnées de chaque case de notre bloc
        une fois le déplacement réalisé. Si une case n'est pas valide (en dehors du plateau), elle n'entre pas dans corps_temp.
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
            x,y = self.cd
            x += direction*self.game.step
            self.cd = [x,y]


    def rotation(self,angle):
        '''
        Fonction liée à un event dans le programme principal. Lorsque la touche o ou p est pressée, la fonction se lance
        avec la valeur associée à la touche (1 pour P, -1 pour O)

        Si angle=1, l'ensemble des pièces subira une rotation de 90° dans le sens des aiguilles d'une montre. Cela se traduira
        par un changement d'apparence de la pièce, piochée dans les apparences contenues dans Block().apparence, en prenant la 
        forme "d'indice" suivant.
        Si angle=-1, même concept, mais ce sera une rotation de 90° dans le sens inverse des aiguilles d'une montre, et la
        prise de la forme "d'indice" précédent

        Dans la même idée que pour les déplacements latéraux, nous utilisons un corps_temp pour ne pas modifier directement
        self.corps.
        '''

        self.corps_precedent = self.corps
        n = len(self.corps)
        corps_temp = []
        corps_temp2 = []
        id_temp = self.id_f + angle

        if id_temp > 3:
            id_temp = 0
        elif id_temp < 0:
            id_temp = 3

        corps_temp = [
        [(self.apparence[id_temp][0][0]*self.game.step+self.cd[0]),(self.apparence[id_temp][0][1]*self.game.step+self.cd[1])],
        [(self.apparence[id_temp][1][0]*self.game.step+self.cd[0]),(self.apparence[id_temp][1][1]*self.game.step+self.cd[1])],
        [(self.apparence[id_temp][2][0]*self.game.step+self.cd[0]),(self.apparence[id_temp][2][1]*self.game.step+self.cd[1])],
        [(self.apparence[id_temp][3][0]*self.game.step+self.cd[0]),(self.apparence[id_temp][3][1]*self.game.step+self.cd[1])]]

        for cell in corps_temp:
            verif = 0
            xc,yc = cell

            if 0<=xc<=self.game.largeur-self.game.step:
                if 0<=yc<=self.game.hauteur-self.game.step:
                    if self.game.plateau[xc//self.game.step][yc//self.game.step] == 0:
                        verif += 1

            if verif==1:
                corps_temp2.append([xc,yc])

        if len(corps_temp2)==4:
            self.corps = corps_temp
            self.id_f = id_temp



class Game:
    def __init__(self,l,h,step,f_r):
        self.largeur = l
        self.hauteur = h
        self.step = step
        self.frame_rate = f_r

        self.score = 0
        self.coo_start = [self.largeur//2,0]

        #Si une case = 0, elle n'est pas occupée. Sinon, elle l'est. A noter qu'on parle ici des blocs posés, pas des pièces qui
        #descendent
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


        #Petite touche décorative, le "Game Over" se dessine dans le plateau en fin de partie. Voici les coo de chacune des lettres
        self.game_over = [
            [(1,2),(2,2),(3,2),(1,3),(1,4),(2,4),(3,4),(3,3)],                                       #G
            [(1,7),(1,8),(1,9),(2,7),(3,7),(3,8),(3,9)],                                             #A
            [(1,12),(1,13),(1,14),(2,12.5),((2+2/3),12.5),(2,13),(3,12),(3,13),(3,14),(2,8.5)],      #M
            [(1,17),(1,18),(1,19),(2,17),(2,18),(2,19.5),(3,17),(3,19.5)],                           #E
            [(6,2),(6,3),(6,4),(7,2),(7,4),(8,2),(8,3),(8,4)],                                       #O
            [(6,7),(6,8),(7,9),(8,7),(8,8)],                                                         #V
            [(6,12),(6,13),(6,14),(7,12),(7,13),(7,14.5),(8,12),(8,14.5)],                           #E
            [(6,17),(7,17),(8,17),(6,18),(6,19),(7,18),(8,19)]]                                      #R


    def accelerer(self):
        if self.frame_rate >= 200:
            self.frame_rate = self.frame_rate // 2

    def ralentir(self):
        if self.frame_rate <= 200:
            self.frame_rate = 400

    def remplir_plateau(self,block,couleur):
        '''
        Lorsqu'un bloc est arrêté dans sa descente, il rejoint le "tas", soit les blocs faisant partie du plateau. Alors, dans
        self.plateau, on remplace les 0 dans les cases correspondant aux coordonnées de chaque cell du bloc par la couleur du bloc,
        de sorte à garder cette couleur en réseve lors des décalages de lignes entraînés par la méthode décaler.
        '''
        for cell in block:
            xc,yc = cell
            self.plateau[xc//self.step][yc//self.step] = couleur
        self.score += 10


    def decaler(self,block):
        '''
        Lorsque x lignes de self.plateau sont pleines, cette fonction vide celles-ci et décale toutes les lignes situées au-dessus
        de x cran en y
        '''
        ver = False
        l = []                  #Lignes déjà vérifiées.
        nb_ligne = 0
        for cell in block:
            xc,yc = cell
            verif = 0
            if yc//self.step not in l:
                for i in range(self.largeur//self.step):
                    if self.plateau[i][yc//self.step] != 0:
                        verif += 1
                if verif == 10:
                    nb_ligne += 1
                    l.append(yc//self.step)
                    ver = True

        if len(l)>0:
            self.score += 100*len(l)
            X = max(l)
            while X >= 0:
                if X-nb_ligne>=0:
                    for i in range(10):
                        self.plateau[i][X] = self.plateau[i][X-nb_ligne]
                else:
                    for i in range(10):
                        self.plateau[i][X] = 0

                X = X-1

        return ver
