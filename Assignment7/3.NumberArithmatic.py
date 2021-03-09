"""
Write a program which contains one class named as Numbers.
Arithmetic class contains one instance variables as Value.
Inside init method initialise that instance variables to the value which is accepted from user.
There are four instance methods inside class as ChkPrime(), ChkPerfect(), SumFactors(),
Factors().
ChkPrime() method will returns true if number is prime otherwise return false.
ChkPerfect() method will returns true if number is perfect otherwise return false.
Factors() method will display all factors of instance variable.
SumFactors() method will return addition of all factors. Use this method in any another method
as a helper method if required.
After designing the above class call all instance methods by creating multiple objects.

"""
class Numbers:
    #inlist =[]
    def __init__(self,value):
        self.Value = value
        #self.lst = [] 
    
  
    def SumFactors(self,lst):  #sumAll
        add = 0
        for i in range(len(lst)):
            add += lst[i]
        return add

    
    def Factors(self,no):
        divisibleNoLst = []
        for i in range(1,int(no/2)+1):
            if(no%i==0):
                divisibleNoLst.append(i)  
        return divisibleNoLst

    def ChkPerfect(self,no):
        if(no==self.SumFactors(self.Factors(no))):
           return True
        else:
            return False

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
   
    def DisplayList(self,mylst):
        for i in range(len(mylst)):
            print(" ",mylst[i])

    def __del__(self):
        print("Deallocating Resources")
        del self.Value

    
def main():
    num = int(input("Enter Value:"))
    obj1 = Numbers(num)
    print("----------")
    print("Output of ChkPrime : ",obj1.ChkPrime(obj1.Value))
    print("Output of ChkPerfect : ",obj1.ChkPerfect(obj1.Value))
    print("Output of Sum of Factors : ",obj1.SumFactors(obj1.Factors(obj1.Value)))
    print("Output of Factors : ",obj1.Factors(obj1.Value))
    print("----------")
    Obj2 = Numbers(28)
    print("----- Output By Programmer Given Values -----")
    print("Output of ChkPrime : ",Obj2.ChkPrime(Obj2.Value))
    print("Output of ChkPerfect : ",Obj2.ChkPerfect(Obj2.Value))
    print("Output of Sum of Factors : ",Obj2.SumFactors(Obj2.Factors(Obj2.Value)))
    print("Output of Factors : ",Obj2.Factors(Obj2.Value))

#Entry Function        
if __name__ == "__main__":
    main()