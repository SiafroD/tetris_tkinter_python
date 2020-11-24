/!\ Github : https://github.com/SiafroD/tetris_tkinter_python

==============================================================================================================

Le programme est constitué de deux fichiers :
-tetris.py
-tetris_class.py

Le premier est le fichier principal, celui qui a pour rôle primordial d'initialiser nos paramètres Tkinter,
créant donc le terrain de jeu, etc...
Il crée aussi le premier bloc ainsi que les paramètres initiaux du jeu, puis fais tourner en boucle la
fonction animer() qui constitue le déroulement du jeu.
C'est ici que seront lancées toutes les méthodes des class.

Les class justement, celles-ci sont stockées dans le fichier tetris_class.py. Ce fichier fais office de
bibliothèque dans laquelle tous nos objets types sont stockés, avec leurs attributs et méthodes. Le fichier
et son contenu sont importés vers tetris.py via un import python.

==============================================================================================================

Version 1 (12/11/20):

--> Ajouts :
-Création du projet
-Mise en place des deux fichiers tetris.py et tetris_class.py 
-Création des class Shapes, Block et Game

-Mise en place des leurs méthodes _init_, et de la méthode descendre pour la class Block.


--> Réflexions :
-Premières réflexions sur l'idée de rotation
-Mise en place d'un programme de chose à réaliser :
   -déplacement latéral du bloc
   -descente accélérée du bloc
   -rotation du bloc
   -collision avec les bordures et le fond du terrain
   -accumulation des blocs déjà tombés
   -suppression des lignes pleines


--> Difficultés :
-Aucunes

==============================================================================================================

Version 2 (17/11/20):

--> Ajouts :
-Mise en place de la méthode mouvement de la class Block, gérant les mouvements latéraux
-Mise en place de la fonction mouvements dans tetris.py, permettant une gestion des mouvements latéraux en
parallèle de la descente continue
-Notion de contrôles (touches q, d et, à l'avenir, s. Respectivement, gauche, droite et bas)


--> Réflexions :
-Préparation de matrices pour les rotations (se basant sur des coordonnées abstraites)
-Prévisions de modifications :
   -modifications du _init_ de la class Block, pour que self.corps = corps devienne self.corps = []
   -utilisation de la méthode créer de la class Block pour définir self.corps


--> Difficultés :
-Lors de la première réalisation des déplacements latéraux, ceci se basait sur un nouvel attribut de Block
alors nommé direction. Cependant, la manière dont la fonction était exécutée faisait que les déplacements
latéraux ne se faisaient qu'au moment des déplacements vers le bas. Ainsi, nous avons modifié la fonction
pour l'exécuter directement depuis tetris.py et nous faisons une actualisation du canvas parallèle à celle
de la boucle principale et de la fonction animer.

==============================================================================================================

Version 3 (23/11/20):

--> Ajouts :
-Collisions avec les bordures et le fond du terrain (gestions dans les méthodes mouvement et descendre de la
class Block)


--> Réflexions :
-Poursuite des réflexions sur l'idée de rotation (matrices, etc...).
-En lien avec la difficulté rencontrée, nous prévoyons, si cela est possible, de modifier le Game.step de 
sorte à ce que celui-ci s'adapte à la taille de l'écran de l'utilisateur.


--> Difficultés :
-Légère difficulté dans la verification de notre système de collision avec le fond du terrain. L'écran de
l'ordi région étant trop petit, la hauteur du terrain dépasse sa taille, et nous ne voyons pas la pièce sortir.
La difficulté a rapidement été surmontée, grâce u l'utilisation d'un print des coordonnées du corps qui nous
ont permis de voir l'arrêt effectif de la pièce en bas du terrain. 

==============================================================================================================

Version 4 (24/11/20):

--> Ajouts :
-Aucuns


--> Réflexions :
-Ajout d'un fichier texte décrivant les "Shapes" des rotations de chaque formes.


--> Difficultés :
-Légères difficultés sur la mise en place de ce schéma, et la visualiation des rotations, mais sans plus.

==============================================================================================================

Version 5 (../11/20):

[...]
