from fenetre import *
from battleship import *
import socket, sys

HOST='192.168.1.69'    # IP du serveur
PORT=25000              # port utilise par le serveur

def main():
    mySocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    try :
        mySocket.bind((HOST,PORT))
        print("// liaison socket reussie ("+HOST+","+str(PORT)+")")

    except socket.error:
        print("// liaison socket echouee ...")
        sys.exit()
    connectid = 0

    mySocket.listen(2)
    connexion, adresse = mySocket.accept()

    print("// client connecte ("+str(adresse[0])+","+str(adresse[1])+")")
    print ""
    ok = [False, False]
    boats = [[],[]]

    def unparsearray(strarray):
        res = []
        asplit = strarray.split(";")
        for a in asplit:
            bsplit = a.split(",")
            bsplit = [int(b) for b in bsplit]
            res.append(bsplit)
        return res

    def serdowhenready(ships):
        ok[0] = True
        boats[0] = ships
        print "serveur pret"
        if ok[1]:
            initboats()

    def clidowhenready(ships):
        ok[1] = True
        boats[1] = ships
        print "client pret"
        if ok[0]:
            initboats()

    def initboats():
        print boats
        for i in range(len(boats[0])):
            p0.addship((boats[0][i][0], boats[0][i][1]),boats[0][i][2], i)
        for i in range(len(boats[1])):
            s = p1.addship((boats[1][i][0], boats[1][i][1]),boats[1][i][2], i)
        print ""
        print ""
        print ""
        playing()

    def srvfeu():
        if (fen.turn == 0):
            x = fen.coordxval.get()
            y = fen.coordyval.get()
            res = p0.play((x,y))
            fen.changecolor(x,y,res)
            connexion.send("p"+str(x)+","+str(y)+","+str(res))
            print "tir du serveur en ("+str(x)+","+str(y)+") ..."
            print ["plouf", "touche", "coule"][res-1]
            print ""
            fen.turn = 1
            playing()
        else:
            print "pas ton tour"
            print ""

    def clifeu():
        msg = "w"
        while(msg[0] != "p"):
            msg = connexion.recv(1024)
        msg = msg[1:]
        msgsplit = msg.split(",")
        x = int(msgsplit[0])
        y = int(msgsplit[1])
        res = p1.play((x,y))
        connexion.send("r"+str(res))
        print "tir du client en ("+str(x)+","+str(y)+") ..."
        print ["plouf", "touche", "coule"][res-1]
        print ""
        fen.turn = 0
        fen.enemyattacks(x,y,res)
        playing()


    def playing():
        fen.feu = srvfeu
        if g.state == 3:
            print "partie finie"
        if g.turn == 0:
            print "a ton tour"
        if g.turn == 1:
            print "tour adverse"
            clifeu()




    fen = Fenetre()
    fen.fen.title("server")
    fen.dowhenready = serdowhenready
    g = Game()
    p0, p1 = g.getplayers()
    while(True):
        msg = connexion.recv(1024)
        if msg[0] == "r":
            clidowhenready(unparsearray(msg[1:]))
            break
    fen.start()


if __name__ == "__main__":
    main()
