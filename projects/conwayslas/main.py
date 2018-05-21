#author :
#title : conway's look and say

def thefunction(last):
    res = ""
    laststr = str(last)
    length = len(laststr)
    i = 0
    while i < length:
        nb = laststr[i]
        c = 1
        while True:
            if (i+c <= length-1):
                if laststr[i+c] == nb:
                    c+=1
                else:
                    break
            else:
                break
        i+=c
        res+=str(c)+nb
    res = int(res)
    return res


u = [1]
for i in range(40):
    u.append(thefunction(u[-1]))
thefile = open("suite.txt","w")
for term in u:
    print len(str(term))
    thefile.write(str(term)+"\n")
