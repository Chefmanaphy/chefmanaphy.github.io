#author :
#title :
import turtle

def main():
    turtle.setup()
    file = open("themepark.plt")
    i=0
    turtle.pu()
    turtle.speed(0)
    for line in file:
        if (i>0):
            coords = line[2:].replace(";","").replace("\n","").split(",")
            coords = [int(int(j)/25.0) for j in coords]
            turtle.speed(0)
            oldcoords = [int(turtle.pos()[0]),int(turtle.pos()[0])]
            if (oldcoords[0] != coords[0] or oldcoords[1] != coords[1]):
                turtle.goto(coords[0],coords[1])
            turtle.pd()
        i+=1








if __name__=="__main__":
    main()
