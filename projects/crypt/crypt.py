#author :
#title :

from PIL import Image
import random
import os

def main():
    inpath = "tocrypt/"
    outpath = "crypted/"
    keypath = "key.png"


    print "Conversion .jpg -> .png ..."
    jpgs2pngs(inpath)
    print "Conversion .jpg -> .png finie."
    print ""

    print "Recherche des images ..."
    imgspaths = getpngimgs(inpath)
    print "Recherche des images finie."
    print ""

    print "Ouverture des images ..."
    imgs = [Image.open(inpath+imgpath) for imgpath in imgspaths]
    print "Ouverture des images finie."
    print ""

    print "Conversion des images en arrays ..."
    imgsarrays = [imgtoarray(img) for img in imgs]
    print "Conversion des images en arrays finie."
    print ""

    print "Ouverture de la cle ..."
    key = Image.open(keypath)
    print "Ouverture de la cle finie."
    print ""

    print "Redimensionnements de la cle ..."
    redimkeys = [resizez(key,imgs[i].size) for i in range(len(imgs))]
    print "Redimensionnements de la cle finis."
    print ""


    print "Conversion de la cle en array ..."
    keyarrays = [imgtoarray(redimkey) for redimkey in redimkeys]
    print redimkeys[0].size
    print imgs[0].size
    print "Conversion de la cle en array finie."
    print ""

    print "Cryptage des arrays ..."
    cryptedarrays = [crypt(imgsarrays[i], keyarrays[i]) for i in range(len(imgsarrays))]
    print "Cryptage des arrays fini"
    print ""

    print "Reconversion en images ..."
    cryptedimgs = [arraytoimg(cryptedarrays[i], imgs[i].size) for i in range(len(imgs))]
    print "Reconversion en images finie."
    print ""

    print "Enregistrement des images cryptees ..."
    for i in range(len(imgs)) : cryptedimgs[i].save(outpath+imgspaths[i])
    print "Enregistrement des images cryptees fini."
    print ""



def arraytoimg(imgarray, s):
    w = s[0]
    res = Image.new("RGB",s ,"black")
    respxs = res.load()
    for y in range(s[1]):
        for x in range(s[0]):
            index = w*3*y+x*3
            respxs[x,y] = tuple([imgarray[index], imgarray[index+1], imgarray[index+2]])
    return res

def imgtoarray(img):
    res = []
    imgpxs = img.load()
    for y in range(img.size[1]):
        for x in range(img.size[0]):
            for c in range(3):
                res.append(imgpxs[x,y][c])
    return res

def crypt(a,key):
    rana = randomlist(len(a), key[0])
    rankey = randomlist(len(a), key[1])
    print len(a), len(rana), len(rankey), len(key)
    res = [(a[rana[i]]+key[rankey[i]])%256 for i in range(len(a))]
    return res

def randomlist(length, seed):
    inds = [i for i in range(length)]
    random.seed(seed)
    random.shuffle(inds)
    return inds

def jpgs2pngs(path):
    imgspaths = []
    for filename in os.listdir(path):
        if filename[-4:] == ".jpg":
            imgspaths.append(filename)

    images = []
    for image in imgspaths:
        jpgimage = Image.open(path+image)
        jpgimage.save(path+image[:-4]+".png")

def getpngimgs(path):
    imgspaths = []

    for filename in os.listdir(path):
        if filename[-4:] == ".png":
            imgspaths.append(filename)
    return imgspaths


def resizez(img,size):
    imgpxs = img.load()
    newimg = Image.new("RGB",(size[0],size[1]),"black")
    newpxs = newimg.load()
    g = [img.size[i]/float(size[i]) for i in range(len(size))]
    for y in range(size[1]):
        for x in range(size[0]):
            newpxs[x,y] = imgpxs[x*g[0], y*g[1]]
    return newimg


if __name__=="__main__":
    main()
