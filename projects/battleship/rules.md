# Carnet de projet de la bataille navale :

>## _Jeu_ :

### bateaux :
* porte avion       ( 5 cases ) id:4
* croiseur          ( 4 cases ) id:3
* contre-torpilleur ( 3 cases ) id:2
* sous-marin        ( 3 cases ) id:1
* torpilleur        ( 2 cases) id:0

### déroulement :
* joueurs prets -> game.state = 1
* joueurs posent leur bateaux -> player.state = 1
* tour du joueur 1 et 2 alternés -> game.state = 2 ~ game.state = 3
* fin du jeu quand un joueur a tout ses bateaux touchés

>## _Code_ :
#### dir :
|valeur|direction|
|----|-----|
|0|Nord|
|1|Sud|
|2|Est|
|3|Ouest|


### communication :
* 1 : plouf
* 2 : touché
* 3 : coulé

## battleship.py :
|classes :|
|---|
|Player|
|Game|
|Plate|
|Ship|
|Point|
### utilisation :
* g = Game()
* p0, p1 = Game.getplayers()
* p0.addship([x,y],direction,type)
*
