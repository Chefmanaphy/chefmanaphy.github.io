from Tkinter import *

class Fenetre:
    def __init__(self):
        self.turn = 0
        self.gamestate = 0
        self.boats = ["porte avion","croiseur","contre-torpilleur","sous-marin","torpilleur"]
        self.boatsizes = [2,3,3,4,5]
        self.selectedship = 0
        self.fen = Tk()
        self.fen.title("Bataille navale")
        self.fen.geometry("610x500")
        self.feu = lambda : 0
        self.dowhenready = lambda : 0
        self.boat = lambda x,y:0
        self.cnv = Canvas(self.fen, width = 300, height = 300, background="black")
        w = 30
        h = 30
        self.squares = []
        self.colors = []
        for y in range(10):
            line = []
            colorline = []
            for x in range(10):
                line.append(self.cnv.create_rectangle(x*w,y*h,x+w+x*w,y+h+y*h, fill = "blue", outline = None))
                colorline.append(0)
            self.squares.append(line)
            self.colors.append(colorline)
        self.cnv.bind("<Button-1>",lambda x:self.changecolor(x,self.squares,self.colors,self.cnv))

        self.cnv2 = Canvas(self.fen,width = 300, height = 300, background="black")
        self.squares2 = []
        self.colors2 = []
        for y in range(10):
            line = []
            colorline = []
            for x in range(10):
                line.append(self.cnv2.create_rectangle(x*w,y*h,x+w+x*w,y+h+y*h, fill = "blue", outline = None))
                colorline.append(0)
            self.squares2.append(line)
            self.colors2.append(colorline)
        self.cnv2.bind("<Button-1>",lambda x:self.boat(x,self.cnv2))


        self.ships = [[0,0,1,self.cnv2.create_oval(0,0,w*self.boatsizes[i],h, outline=["brown","purple"][int(i==0)], width=3)] for i in range(5)]

        self.attack = Frame(self.fen)
        self.coordxval = IntVar(0)
        self.coordyval = IntVar(0)
        self.targetrect = self.cnv.create_rectangle(self.coordxval.get()*30,self.coordyval.get()*30,self.coordxval.get()*30+30,self.coordyval.get()*30+30, outline="red", width=3)
        self.coordx = Scale(self.attack,from_=0,to=9, variable = self.coordxval)
        self.coordy = Scale(self.attack,from_=0,to=9, variable = self.coordyval)
        self.commands = Frame(self.attack)
        self.coords = Label(self.commands,text="(x,y) = (A,0)")
        self.fire = Button(self.commands,text="FIRE !",command=lambda : self.feu())
        self.theframe = Frame(self.fen)
        self.listebateaux = Listbox(self.theframe)
        for i in range(len(self.boats)):
            self.listebateaux.insert(i+1,self.boats[i])
        self.listebateaux.bind("<<ListboxSelect>>", lambda event: self.changeselectedship(self.listebateaux.curselection()[0]))

        self.coordx.bind("<ButtonRelease-1>", lambda event: self.movetarget())
        self.coordy.bind("<ButtonRelease-1>", lambda event: self.movetarget())
        self.labelselectedship = Label(self.theframe, text="0")
        self.arrows = Frame(self.theframe)
        self.rotate = Button(self.arrows,text="rotation",command=lambda :self.dorotate())
        self.down = Button(self.arrows,text="down", command=lambda :self.moveship(4))
        self.up = Button(self.arrows,text="up", command=lambda :self.moveship(2))
        self.right = Button(self.arrows,text="right", command=lambda :self.moveship(1))
        self.left = Button(self.arrows,text="left", command=lambda :self.moveship(3))
        self.done = Button(self.theframe,text="DONE", command=lambda :self.submit())

        self.cnv.grid(row=1,column=1)
        self.cnv2.grid(row=1,column=2)
        self.theframe.grid(row=2,column=2)
        self.attack.grid(row=2,column=1)
        self.coordx.grid(row = 1, column = 1)
        self.coordy.grid(row = 1, column = 2)
        self.commands.grid(row = 1, column = 3)
        self.coords.pack({"side":"top"})
        self.fire.pack({"side":"bottom"})
        self.listebateaux.grid(row=1,column=1)
        self.arrows.grid(row=1,column=2)
        self.done.grid(row=2,column=3)
        self.rotate.grid(row = 2,column=2)
        self.right.grid(row = 2,column=3)
        self.left.grid(row = 2,column=1)
        self.up.grid(row = 1,column=2)
        self.down.grid(row = 3,column=2)


        #Button(fen,text="ok",command=lambda:cnv.itemconfig(squares[5][5], fill= "blue")).pack()
        self.fen.protocol("WM_DELETE_WINDOW", self.fen.destroy)

    def submit(self):
        ships = []
        for ship in self.ships:
            ships.append(ship[:3])
        self.dowhenready(ships)
    def movetarget(self):
        self.coords.config(text="(x,y) = ("+unichr(65+self.coordxval.get())+","+str(self.coordyval.get())+")")
        self.cnv.coords(self.targetrect,self.coordxval.get()*30,self.coordyval.get()*30,self.coordxval.get()*30+30,self.coordyval.get()*30+30)
    def moveship(self,direct):
        dirx = int(direct==1 or direct==3)*-1+2*int(direct==1)
        diry = int(direct==2 or direct == 4)*-1+2*int(direct==4)
        self.ships[self.selectedship][0]+=dirx
        self.ships[self.selectedship][1]+=diry
        l = self.boatsizes[self.selectedship]
        x = self.ships[self.selectedship][0]
        y = self.ships[self.selectedship][1]
        d = self.ships[self.selectedship][2]
        if (d == 1):
            self.cnv2.coords(self.ships[self.selectedship][3],x*30,y*30+30,x*30+l*30,y*30)
        elif (d == 2):
            self.cnv2.coords(self.ships[self.selectedship][3],x*30,y*30+30,x*30+30,y*30-30*l+30)
        elif (d == 3):
            self.cnv2.coords(self.ships[self.selectedship][3],x*30+30,y*30,x*30-30*l+30,y*30+30)
        elif (d == 4):
            self.cnv2.coords(self.ships[self.selectedship][3],x*30,y*30,x*30+30,y*30+l*30)

    def enemyattacks(self,x,y,res):
        if (res-1 == 0):
            self.colors2[y][x] = 1
            self.cnv2.itemconfig(self.squares2[y][x],fill="green")
        if (res-1 == 1):
            self.colors2[y][x] = 2
            self.cnv2.itemconfig(self.squares2[y][x],fill="yellow")
        if (res-1 == 2):
            self.colors2[y][x] = 3
            self.cnv2.itemconfig(self.squares2[y][x],fill="red")



    def changeselectedship(self,index):
        self.selectedship = index
        for i in range(5):
            if (i != index):
                self.cnv2.itemconfig(self.ships[i][3],outline="brown")
            else:
                self.cnv2.itemconfig(self.ships[index][3],outline="purple")
    def dorotate(self):
        self.ships[self.selectedship][2] = (self.ships[self.selectedship][2])%4+1
        l = self.boatsizes[self.selectedship]
        x = self.ships[self.selectedship][0]
        y = self.ships[self.selectedship][1]
        d = self.ships[self.selectedship][2]
        if (d == 1):
            self.cnv2.coords(self.ships[self.selectedship][3],x*30,y*30+30,x*30+l*30,y*30)
        elif (d == 2):
            self.cnv2.coords(self.ships[self.selectedship][3],x*30,y*30+30,x*30+30,y*30-30*l+30)
        elif (d == 3):
            self.cnv2.coords(self.ships[self.selectedship][3],x*30+30,y*30,x*30-30*l+30,y*30+30)
        elif (d == 4):
            self.cnv2.coords(self.ships[self.selectedship][3],x*30,y*30,x*30+30,y*30+l*30)
    def start(self):
            self.fen.mainloop()

    def changecolor(self,x,y,color):
        elem = self.squares[y][x]
        self.colors[y][x] = color
        if color == 1:
            self.cnv.itemconfig(elem,fill="green")
        elif color == 2:
            self.cnv.itemconfig(elem,fill="yellow")
        elif color == 3:
            self.cnv.itemconfig(elem,fill="red")

def printshow(elem):
    print elem

def signe(nombre):
    if nombre >= 0:
        return 1
    else:
        return -1
