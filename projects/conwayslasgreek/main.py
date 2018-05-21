#author :
#title : conway's look and say greek


def num2roman(num):
    num_map = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'),
               (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]



    roman = ''

    while num > 0:
        for i, r in num_map:
            while num >= i:
                roman += r
                num -= i

    return roman


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
        res+=num2roman(c)+nb
    return res


u = ["I"]
for i in range(100):
    u.append(thefunction(u[-1]))
thefile = open("suite.txt","w")
for term in u:
    print len(term)
    thefile.write(term+"\n")
