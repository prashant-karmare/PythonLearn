"""
Design object oriented python application which accept n no from user and perform below operations:
Display all even no
Calculate the summation of all nos
Display all perfect no

Display all Prime NO

"""
class Numbers:
    #inlist =[]
    def __init__(self,no):
        self.size = no
        self.lst = [] 
    def AcceptNNo(self):
        for i in range(self.size):
            self.lst.append(int(input("Enter No {}: ".format(i+1))))
        #inlist = self.lst
    def DisplayList(self,mylst):
        for i in range(len(mylst)):
            print(" ",mylst[i])

    evenNo = lambda no: (no%2==0) 
    
    def AllEvenNo(self):
        return list(filter(Numbers.evenNo,self.lst))

    def sumAll(self,lst):
        add = 0
        for i in range(len(lst)):
            add += lst[i]
        return add

    def Divisible(self,no):
        divisibleNoLst = []
        for i in range(1,int(no/2)+1):
            if(no%i==0):
                divisibleNoLst.append(i)  
        return divisibleNoLst

    def PerfectNo(self,no):
       if(no==self.sumAll(self.Divisible(no))):
           return True

    def AllPerfectNo(self):
        return list(filter(self.PerfectNo,self.lst))

    def ChkPrime(self,no):
        for i in range(2,no):
            if no%i == 0:
                flag = False
                break         
        else:
            if(no==1):
                flag=False
            else:
                flag = True
        return flag

    def chkLstPrime(self):
        return list(filter(self.ChkPrime,self.lst))

    def __del__(self):
        print("Deallocating Resources")
        del self.lst

    
def main():
    num = int(input("Enter how many elements you want:"))
    obj1 = Numbers(num)
    obj1.AcceptNNo()
    obj1.DisplayList(obj1.lst)
    print("Even No List is:")
    obj1.DisplayList(obj1.AllEvenNo())
    print("Sum of all is:",obj1.sumAll(obj1.lst))
    print("Perfect No List Contains:")
    obj1.DisplayList(obj1.AllPerfectNo())
    print("Prime No List is:")
    obj1.DisplayList(obj1.chkLstPrime())


#Entry Function        
if __name__ == "__main__":
    main()