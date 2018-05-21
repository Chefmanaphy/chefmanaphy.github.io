#author :
#title : Conway's game of life

from PIL import Image


def showgrid(grid, name):
    img = Image.new("RGB", (len(grid[0]), len(grid)), "white")
    imgpxs = img.load()
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == 1:
                # print x,y
                imgpxs[x,y] = (0,0,0)
    img.save(name)
    # img.show()

def step(grid):
    res = [[0 for i in range(len(grid[0]))] for j in range(len(grid))]
    for x in range(len(grid[0])):
        for y in range(len(grid)):
            c = 0
            for cx in range(-1, 2):
                for cy in range(-1, 2):
                    if (not(cx ==0 and cy == 0)):
                        if (grid[(y+cy)%len(grid)][(x+cx)%len(grid[0])]) == 1:
                            c+=1
            if grid[y][x] == 1 and (c==2 or c==3):
                res[y][x] = 1
            if c==3 and grid[y][x] == 0:
                res[y][x] = 1
    return res

initimage = Image.open("ini.png")
inipxs = initimage.load()

grid = [[int(inipxs[x,y] != (255,255,255)) for x in range(initimage.size[0])] for y in range(initimage.size[1])] #100*100 grid
showgrid(grid, "gens/gen0.png")
for i in range(16):
    print i+1
    grid = step(grid)
    showgrid(grid, "gens/gen"+str(i+1)+".png")
