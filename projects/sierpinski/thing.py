from PIL import Image
black = (0,0,0)
iterations = 120
rule = [[[0,0,0],[0,0,1],[0,1,0],[0,1,1],[1,0,0],[1,0,1],[1,1,0],[1,1,1]],[0,1,1,1,1,0,0,0]]


img = Image.new("RGB",(2*iterations+1,iterations),"white")
imgpxs = img.load()
for i in range(iterations):
    if (i==0):
        imgpxs[iterations,i] = black
    else :
        for j in range(2*iterations-1):
            j+=1
            above = [imgpxs[j-1,i-1],imgpxs[j,i-1],imgpxs[j+1,i-1]]
            above = [int(x==(0,0,0))for x in above]
            if ((rule[1][rule[0].index(above)])==1):
                imgpxs[j,i] = black
        if (i%10 == 0):
            print (i*100.0)/iterations
img.show()
img.save("truc.png")
