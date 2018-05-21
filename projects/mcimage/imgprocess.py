
from PIL import Image

def resizez(img,size):
    imgpxs = img.load()
    newimg = Image.new("RGB",(size[0],size[1]),"black")
    newpxs = newimg.load()
    g = [img.size[i]/float(size[i]) for i in range(len(size))]
    for y in range(size[1]):
        for x in range(size[0]):
            newpxs[x,y] = imgpxs[x*g[0], y*g[1]]
    return newimg

def echant(img, colors):
    imgpxs = img.load()
    for y in range(img.size[1]):
        for x in range(img.size[0]):
            closest = ((0,0,0),589824)
            for color in colors:
                thedist = colordist(color,imgpxs[x,y])
                if closest[1]>thedist:
                    closest = (color,thedist)
            imgpxs[x,y] = closest[0]
        print y


def pxperpx(img, pxfunction):
    imgpxs = img.load()
    for y in range(img.size[1]):
        for x in range(img.size[0]):
            imgpxs[x,y] = pxfunction(imgpxs[x,y])

def colordist(a,b):
    res = 0
    for i in range(3):
        res+=(a[i]-b[i])**2
    return res

def edge(img):
    imgpxs = img.load()
    for y in range(img.size[1]):
        for x in range(img.size[0]):
            if x!=img.size[0]-1 and y!=img.size[1]-1:
                imgpxs[x,y] = tuple([abs(imgpxs[x,y][i]-imgpxs[x+1,y][i])+abs(imgpxs[x,y][i]-imgpxs[x,y+1][i]) for i in range(3)])
        print str(y)+" / "+str(img.size[1])

def hextocolor(hex):
    r = hex[2:4]
    g = hex[4:6]
    b = hex[6:8]
    return((int(r,16),int(g,16),int(b,16)))
