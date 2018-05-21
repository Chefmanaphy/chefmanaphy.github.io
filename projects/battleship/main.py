from fenetre import *
import socket, sys

HOST='192.168.1.69'    # IP du Serveur
PORT=25000              # Port physique utilise par le Serveur


def main():
    mySocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    try :
        mySocket.connect((HOST,PORT))
    except socket.error:
        print("// connexion echouee")
        sys.exit
    print("// connexion reussie")
    print ""
    fen = Fenetre()
    fen.fen.title("Client - Bataille Navale")

    def arrtostring(arr):
        res = ""
        for a in range(len(arr)):
            for b in range(len(arr[a])):
                res+=str(arr[a][b])
                if (b<len(arr[a])-1):
                    res+=","
            if (a<len(arr)-1):
                res+=";"
        return res

    def dowhenready(boats):
        mySocket.send("r"+arrtostring(boats))
        print "pret"
        print ""
        print ""
        print ""
        playing()

    def clifeu():
        if fen.turn == 1:
            x = fen.coordxval.get()
            y = fen.coordyval.get()
            mySocket.send("p"+str(x)+","+str(y))
            print "tir du client en ("+str(x)+","+str(y)+") ..."

            msg = "w"
            while(msg[0] != "r"):
                msg = mySocket.recv(1024)
            msg = msg[1:]
            fen.changecolor(x,y,int(msg))
            fen.turn = 0
            print ["plouf", "touche", "coule"][int(msg)-1]
            print ""
            playing()
        else:
            print "pas ton tour"
            print ""


    def srvfeu():
        msg = "w"
        while(msg[0] != "p"):
            msg = mySocket.recv(1024)
        msg = msg[1:]
        fen.turn = 1
        msgsplit = msg.split(",")
        x = int(msgsplit[0])
        y = int(msgsplit[1])
        res = int(msgsplit[2])
        print "tir du serveur en ("+str(x)+","+str(y)+") ..."
        print ["plouf", "touche", "coule"][res-1]
        print ""
        fen.enemyattacks(x,y,res)

    def playing():
        fen.feu = clifeu
        if fen.turn == 0:
            print "tour adverse"
            print ""
            srvfeu()
        if fen.turn == 1:
            print "a ton tour"
            print ""




    fen.dowhenready = dowhenready

    fen.start()

if __name__=="__main__":
    main()
