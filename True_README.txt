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
-Lors de la première réalisation des déplacements latéraux, ceux-ci se basaient sur un nouvel attribut de Block
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
La difficulté a rapidement été surmontée, grâce à l'utilisation d'un print des coordonnées du corps qui nous
ont permis de voir l'arrêt effectif de la pièce en bas du terrain. 

==============================================================================================================

Version 4 (25/11/20):

--> Ajouts :
-Aucuns


--> Réflexions :
-Ajout d'un fichier texte décrivant les "Shapes" des rotations de chaque formes.


--> Difficultés :
-Légères difficultés sur la mise en place de ce schéma, et la visualiation des rotations, mais sans plus.

==============================================================================================================

Version 5 (26/11/20):

--> Ajouts :
-Ajout d'une TODO_list (TODO.txt)
-Système de collision avec les pièces déjà tombées, que ce soit latéralement ou dans la descente.
-Fonction permettant le remplissage du plateau. Lorsqu'une pièce se bloque, ses positions dans le tableaux
servent à changer les 0 du Game().plateau en 1.
-Système d'accélération de la descente de la pièce.
-Lorsque la pièce que l'on contrôle finit par se bloquer, génération d'une nouvelle pièce.
-Couleurs associées à chaque blocs.
-Changement de la couleur de fond.
-Modification de l'utilisation de tkinter. Désormais, on repeint avec la couleur du fond les cases quittées par
la pièce lors de ses mouvements, de sorte à ne pas faire de w.delete(ALL) et ainsi tout détruire, forçant donc
la disparition des pièces déjà tombées, notamment.


--> Réflexions :
-Préparation des quatre systèmes restant : 
   -Suppression d'une ligne pleine
   -Rotation
   -Game Over lorsqu'une colonne est pleine
   -Score


--> Difficultés :
-Pour tout ce qui concerne les collisions, quelques petites erreurs banales dans la formulation des demandes
etc... qui ont entraîné quelques erreurs plutôt bêtes, mais rapidement corrigées.
-De même pour le système des couleurs, avec quelques petits quiproquos entre noms de class et nom de l'objet
représentant cette classe (ici, "Block" et "block").
-Grandes réflexions sur la génération d'une nouvelle pièce. Deux solutions ont été envisagées, concernant la
méthodes reset_block(), à savoir de la placer dans la class Block ou dans la class Game. Finalement, nous
l'avons placé dans la class Block pour une gestion plus localisée de la chose et éviter trop d'échanges entre
les classes, mais l'autre solution reste évidemment envisageable.

==============================================================================================================

Version 6 / Version 1.0 (27/11/20):

--> Ajouts :
-Système de rotation via la fonction mouvements déjà présente dans tetris.py ainsi que la fonction rotation
ajoutée dans tetris_class.py
-Système de destruction des lignes pleines, ajouté via la fonction décaler dans la class Game().
-Système de score, simplement implémenté par un v.set(). Lorsqu'un bloc quelconque est posé, le score est
incrémenté de 10, et lorsqu'une ligne est détruite, le score est incrémenté de 100.
-Lorsque la case de coordonnées x quelconque et y=0 est occupée par une cell d'un bloc, c'est Game Over.
-Affichage graphique du Game Over sur le canvas de tkinter.
-Modification du fichier tetris_fonctionnement.txt. Les parties sur le score ont été mise à jour.
-Modification du fichier TODO.txt. Les idées ci-dessous ont été ajouté.


--> Réflexions :
-Idées d'ajouts supplémentaires pour embellir le projet qui, dans la technique, est d'ores et déjà terminé.
   -Sound design.
   -Musique.
   -Passage de toutes les procédures pour l'affichage graphique du "Game Over" dans la class Game(), avec
    une méthode créée pour l'occasion.
   -Sauvegarde des scores dans une base de donnée (.json, sql, etc...)
   -Ajout d'une identification via un pseudo et mot de passe, eux aussi stockés dans une base de donnée
   -Système de difficulté (se basant notamment sur une augmentation de la vitesse de chute des pièces)


--> Difficultés :
-La rotation a posé plusieurs problèmes, mais ceux-ci étant comme bien souvent des erreurs plutôt bêtes. 
Avec le système de rotation, nous avons enfin ajouté un intérêt à l'attribut cd (=coordonnées par défaut)
de la class Block(). En effet, celle-ci fait office de pivot pour la rotation, puisque c'est à partir de
celle-ci que sont déterminées les nouvelles coordonnées de chaque forme, par l'utilisation des coordonnées
"abstraites" contenues dans Shapes().formes. Cependant, il faut que cd suive les modifications que subit le
bloc lors de sa descente ou de ses déplacements latéraux. Un bug que nous avions était que les coordonnées
x de cd ne faisaient qu'augmenter constamment. Ceci était lié à une simple erreur : nous n'utilisions pas
la variable muette direction de la méthode mouvement (dans Block()) pour affecter les x de cd. Ainsi, dès
qu'un mouvement latéral était accompli, que ce soit à gauche ou à droite, les x de cd se déplaçait de
20 (1*Game().step) vers la droite.

-Légères difficultés dans la mise en place de la détection du Game Over. En effet, nous pensions jusque là
qu'il fallait voir si une collonne entière était pleine, alors qu'il suffit d'observer la case de coordonnées
x quelconque de y=0 pour enclencher ou non un Game Over.

-La mise en place de l'affichage du Game Over de manière graphique était simplement horrible. Le résultat
est maintenant plus que satisfaisant, mais il faudra optimiser la chose dans les futures versions, c'est 
certain.
