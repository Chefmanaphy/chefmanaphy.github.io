#author : DURAND Ulysse
#title : Mario's plates

def main():
    count = 3
    jeu = True
    matrix0 = tomatrix("puzzle0.txt")
    matrix1 = tomatrix("puzzle1.txt")
    solve(matrix0,matrix1,count,jeu)

def tomatrix(thefile):
    lines = []
    f = open(thefile)
    for line in f:
        boolline = []
        line = line.replace("\n","")
        for char in line:
            boolline.append(bool(int(char)))
        lines.append(boolline)

    return lines

def solve(m0, m1,count,jeu):
    solved = False
    h = len(m0)
    w = len(m0[0])
    loops = (w,count*2)
    nbiter = loops[0]**loops[1]
    soluces = []
    percentage = 0.0
    old = 0.0
    for i in xrange(nbiter):
        old = (i*100.0)/nbiter
        if (int(percentage) != int(old)):
            percentage = old
            print("{:.2%}".format(percentage/100))

        res = []
        for j in range(loops[1]):
            res.append(i/(loops[0]**j)%loops[0])
        mtest = [[i[j] for j in range(w)] for i in m0]
        for j in range(count):
            mtest = testTry(mtest,res[j*2],res[j*2+1])
        if (compareMatrices(mtest,m1)):
            solved = True

            soluce = []
            for k in range(count):
                soluce.append((res[k*2],res[k*2+1]))
            if (jeu):
                solucematrix = [[0 for i in range(w)] for i in range(h)]
                for play in range(len(soluce)):
                    solucematrix[soluce[play][1]][soluce[play][0]] = play+1
                pmatrix(solucematrix)
                break
            else:
                soluces.append(soluce)
            print soluce
    if not(jeu):
        if (solved):
            print str(len(soluces))+" solutions : "
            for soluce in soluces:
                print soluce
        else :
            print "aucune solution"
    else:
        print "aucune solution"




def testTry(m0,x,y):
    h = len(m0)
    w = len(m0[0])
    res = [[i[j] for j in range(w)] for i in m0]
    for i in range(-1,2):
        for j in range(-1,2):
            sx = x+i
            sy = y+j
            if (sx>=0 and sx<w and sy>=0 and sy<h):
                res[sy][sx] = not(m0[sy][sx])
    return res

def pmatrix(m0):
    for i in range(len(m0)):
        line = []
        for j in range(len(m0[i])):
            line.append(int(m0[i][j]))
        print line
def compareMatrices(m0,m1):
    res = True
    for i in range(len(m0)):
        for j in range(len(m0[i])):
            if m0 != m1:
                res = False
    return res



if __name__=="__main__":
    main()
