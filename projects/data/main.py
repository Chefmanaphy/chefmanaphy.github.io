import os
from os import listdir
from os.path import exists, join

def main():
    while True:
        command = raw_input()
        if (command[0] == "1"):
            command = command[1:]
            params = command.split(" ")
            if (len(params)==2):
                if (exists("data\\utils\\"+params[0])):
                    if (not(exists(params[1]))):
                        os.system("xcopy data\\utils\\"+params[0]+" "+params[1]+"\\ /E")
                        os.system("atom -a "+params[1])
                        os.system("explorer "+params[1])
                        break
                    else:
                        print "le projet qui se nomme "+params[1]+" existe deja"
                else:
                    print "le type de projet "+params[0]+" n'existe pas"
            else:
                print "2 parametres attendus : "+command
        else:
            if (command=="liste"):
                files = [f for f in listdir("..\\root") if exists(f)]
                print "liste des projets :"
                for afile in files:
                    print "- "+afile
            elif (exists(""+command)):
                os.system("atom -a "+command)
                os.system("explorer "+command)
                break
            else:
                print "le projet "+command+" n'existe pas"


if __name__=="__main__":
    main()
