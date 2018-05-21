#author :
#title :
from PIL import Image

images = []
for i in range(7):
    img = Image.open("result ("+str(i+1)+").png")
    images.append(img.load())

new = Image.new("RGB", (800*7, 800), "white")
newpxs = new.load()
for i in range(800*7):
    for j in range(800):
        newpxs[i,j] = images[i/800][i%800, j]

new.show()
new.save("finalresult.png")
