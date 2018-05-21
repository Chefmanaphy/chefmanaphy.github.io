#author :
#title :


class Player:
    def __init__(self,game,ident,name):
        self.ident = ident
        self.game = game
        self.name = name
        self.turn = 0
        self.ships = []

    def setplate(self,plate):
        self.plate = plate

    def changename(self,name):
        self.name = name

    def addship(self,pos, direct, shiptype):
        ship = Ship(pos,direct,shiptype)
        ship.setplayer(self)
        self.ships.append(ship)
        if self.game.playersready()[0] and self.game.playersready()[1]:
            self.game.state = 2
        return ship

    def play(self,pos):
        if (self.game.state == 2):
            if (True in [len(player.ships) == 0 for player in self.game.players]):
                self.game.state = 3
            if (self.game.turn == self.ident):
                return self.game.players[(self.ident+1)%2].plate.grid[pos[0]][pos[1]].rocket()
            else:
                return "Pas ton tour"
        else:
            return "Pas tous les bateaux poses"
class Game:
    def __init__(self):
        self.state = 1
        self.turn = 0
        self.players = [Player(self,i,"untitled") for i in range(2)]
        self.plates = [Plate(i,self.players[i]) for i in range(2)]
        for i in range(len(self.players)):
            self.players[i].setplate(self.plates[i])

    def getplayers(self):
        return self.players

    def playersready(self):
        res = [len(self.players[i].ships) == 5 for i in range(2)]
        # print res
        return res

class Plate:
    def __init__(self,ident,player):
        self.id = ident
        self.player = player
        self.grid = []
        for y in range(10):
            line = []
            for x in range(10):
                line.append(Point(self,x,y))
            self.grid.append(line)


class Ship:
    def __init__(self, pos, direct, shiptype):
        self.pos = pos
        self.direct = direct

        self.points = []
        shiplengths = [2,3,3,4,5]
        self.length = shiplengths[shiptype]
        self.shiptype = shiptype

    def setplayer(self,player):
        x = self.pos[0]
        y = self.pos[1]
        dirx = diry = 0
        direct = self.direct
        if direct == 1:
            dirx = 1
        if direct == 3:
            dirx = -1
        if direct == 4:
            diry = 1
        if direct == 2:
            diry = -1
        self.player = player
        for i in range(self.length):
            # print x+i*dirx,y+i*diry
            self.points.append(player.plate.grid[x+i*dirx][y+i*diry])
        for point in self.points:
            player.plate.grid[point.y][point.x].setShip(self)

    def last(self):
        nb = 0
        ls = None
        for point in self.points:
            if point.answer == 2:
                nb+=1
                ls = point
        if nb==1:
            ls.answer = 3


class Point:
    def __init__(self,plate,x,y,ship = None):
        self.x = x
        self.y = y
        self.ship = ship
        self.plate = plate
        self.answer = 1

    def setShip(self,ship):
        self.ship = ship
        self.answer = 2

    def rocket(self):
        res = self.answer
        self.answer = 1
        if self.ship!=None:
            self.ship.last()
        self.plate.player.game.turn = (self.plate.player.game.turn+1)%2

        if res == 3:
            self.plate.player.ships.remove(self.ship)
        return(res)



def showgrid(grid):
    for y in range(10):
        line = ""
        for x in range(10):
            line+=str(grid[x][y].answer)+"  "
        print line
