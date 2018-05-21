#author : DURAND Ulysse
#title : maindate

class Date:
    def __init__(self,j,m,a):
        self.bissex = self.bissextile(a)
        self.month = self.months(a)
        if (j>0 and m>0 and m<13 and j <= self.month[m-1]):
            self.ds = self.daystamp(j,m,a)
            self.wd = (5+self.ds)%7

    def bissextile(self,a):
        return (a%4 == 0 and not(a%100 == 0)) or (a%400==0)
    def daystamp(self,j,m,a):
        res = 0
        nbcycl = a/400
        res+=nbcycl*146097
        a-=nbcycl*400
        for i in range(0,a,1):
            res+=int(self.bissextile(i))+365
        for i in range(m-1):
            res+=self.months(a)[i]
        res+=j-1
        if a<0:
            res*=-1
        return int(res)

    def months(self,a):
        return [31,28+int(self.bissextile(a)),31,30,31,30,31,31,30,31,30,31]

    def add(self,nb):
        res = self.todate(self.ds+nb)
        return res

    def todate(self,ds):
        nbcycl = ds/146097
        ca = 400*nbcycl
        res = ds%146097
        while res>365+int(self.bissextile(ca)):
            res-=365+int(self.bissextile(ca))
            ca+=1
        i=0
        while(res>self.months(ca)[i]):
            res-=self.months(ca)[i]
            i+=1
        cm = i+1
        cj = res+1
        return int(cj),int(cm),int(ca)
