#author : Ulysse DURAND
#title : Truth-table

inputs = 6

def main():
    tabl = "|"
    tabl2 = "|"
    for i in range(inputs):
        tabl+=" "+chr(i+97)+" |"
        tabl2+="---|"
    tabl+=" Y |"
    tabl2+= "---|"
    print (tabl+"\n"+tabl2)
    for i in range(2**inputs):
        params = []
        for j in range(inputs):
            params.append(i/(2**j)%2)
        s = int(boolAlgebra(params))
        tabl = "|"
        for j in range(inputs):
            tabl += " "+str(params[j])+" |"
        tabl+=" "+str(s)+" |"
        print(tabl)

def boolAlgebra(params):
    for i in range(len(params)):
        exec(chr(97+i)+"=params[i]")

    formula = "a+!(b).c.!(d+e+f)"

    exec(boolFormula(formula))
    return Y

def boolFormula(text):
    while True:
        test = False
        for i in range(len(text)-1):
            if (ord(text[i]) >=97 and ord(text[i])<123 and ord(text[i+1]) >=97 and ord(text[i+1])<123):
                text = text[:i+1]+"."+text[i+1:]
                test = True
        if test == False:
            break
    text = text.replace("+"," or ")
    text = text.replace("."," and ")
    text = text.replace("!","not")
    text = "Y = "+text
    return text

def nand(a,b):
    return not(a and b)

if __name__ == "__main__":
    main()
