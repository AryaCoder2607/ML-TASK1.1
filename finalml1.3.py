class Titandex:
    def __init__(self,Tname,Theight,Tstren):
        self.Tname=Tname
        self.Theight=Theight
        self.Tstren=Tstren
        self.twin=0
    def titanVsScout(self):
        print("enter how many battles between",self.Tname, "and scouts:")
        n=int(input())
        for i in range(n):
            namescout=input("enter name of scout")
            scoutstren=int(input("enter scout strength"))
            if(scoutstren>self.Tstren):
                print("wins: ",namescout)
                if self.twin!=0:
                    print("winning streak of",self.Tname,"is reset to 0")
                    self.twin=0
                else:
                    print("winning streak is",self.twin)    
            elif(scoutstren<self.Tstren):
                self.twin+=1
                print("wins",self.Tname)
            else:
                print('DRAW : hehe ')    

    def titanVstitan(self):
        print("enter how many battles between",self.Tname, "and titans:")
        n=int(input())

        for j in range(n):
            print("Enter name of titan and strength")
            tname=input()
            tstrength=int(input())

            if tname.lower()==(self.name).lower():
                print("cannot fight itself")          
            elif(tstrength>self.Tstren):
                print(" wins:  ",tname)
                if self.twin!=0:
                    print("win streak:",self.Tname,"is set to 0")
                else:
                    print("winn streak of ",self.twin)   
            elif tstrength==self.Tstren:
                print("Its a draw")
                if self.twin!=0:
                    print("win streak:",self.Tname,"is set to 0")
                    self.twin=0
                else:
                    print("winn streak of ",self.twin) 
            else:
                self.twin+=1
                print("winner is:",self.Tname)
                print("winn streak",self.twin)        



                 
a=input("ENTER NAME of titan")
b=input("enter height of titan")
c=input("enter strength of titan")
titan=Titandex(a,int(b),int(c))
titan.titanVsScout()
   









        
