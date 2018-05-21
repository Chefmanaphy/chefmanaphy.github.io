#author :
#title :
from PIL import Image
from imgprocess import *
imgpath = "img.png"
imgrespath = "result.png"
strcolors = ["FFe4e4e4","FFa0a7a7","FF414141","FF181414","FF9e2b27","FFea7e35","FFc2b51c","FF39ba2e","FF364b18","FF6387d2","FF267191","FF253193","FF7e34bf","FFbe49c9","FFd98199","FF56331c"]

def main():
    img = Image.open(imgpath)
    colors = [hextocolor(color) for color in strcolors]

    img = resizez(img,(1024,768))
    echant(img,colors)

    img.show()
    img.save(imgrespath)

if __name__ == "__main__":
    main()
