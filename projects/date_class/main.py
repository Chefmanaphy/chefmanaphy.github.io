#author : DURAND Ulysse
#title : maindate

from date import Date

week = ["lundi","mardi","mercredi","jeudi","vendredi","samedi","dimanche"]

def main():
    for i in range(101):
        print str(i)+" ans : "+week[Date(19,5,2000+i).wd]


if __name__=="__main__":
    main()
