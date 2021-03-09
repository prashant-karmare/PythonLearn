"""
Write a program which contains one class named as BankAccount.
BankAccount class contains two instance variables as Name & Amount.
That class contains one class variable as ROI which is initialise to 10.5.
Inside init method initialise all name and amount variables by accepting the values from user.
There are Four instance methods inside class as Display(), Deposit(), Withdraw(),
CalculateIntrest().
Deposit() method will accept the amount from user and add that value in class instance variable
Amount.
Withdraw() method will accept amount to be withdrawn from user and subtract that amount
from class instance variable Amount.
CalculateIntrest() method calculate the interest based on Amount by considering rate of interest
which is Class variable as ROI.
And Display() method will display value of all the instance variables as Name and Amount.
After designing the above class call all instance methods by creating multiple objects.
"""
class BankAccount:
    ROI = 10.5
    def __init__(self,name,amount=0.0):
        self.Name = name  
        self.Amount = amount

    def Display(self,msg):
        print(msg,"----------")
        print("Name : ", self.Name)
        print("Amount : ", self.Amount)
       
    def Deposit(self,amount):        
         self.Amount = self.Amount + amount

    def Withdraw(self,amount,boolWithdrawinNegative):
        if(boolWithdrawinNegative == False):
            if(self.Amount < amount):
                print("Notification :  Insufficient Balance to Withdraw Money") 
            else:
                 self.Amount = self.Amount - amount
        else:                                    
            self.Amount = self.Amount - amount
         
    def CalculateIntrest(self):        
         return self.Amount*BankAccount.ROI
  
def main():
    print("Enter Details of Bank Account for Obj1 :")
    Value1=input(" Name of Account Holder : ")
    Value2=float(input(" Ammount : "))
    Obj1 = BankAccount(Value1,Value2)
    print("Enter Details of Books for Obj2 :")
    Value1=input(" Name of Account Holder : ")
    Value2=float(input(" Ammount : "))
    Obj2 = BankAccount(Value1,Value2)

    Obj1.Deposit(100)
    Obj1.Display("Amount After Deposit 100")
    Obj1.Withdraw(50,True)
    Obj1.Display("Amount After Withdraw 100")
    print("Calculated Interest is : " ,Obj1.CalculateIntrest())
 
    Obj2.Deposit(100)
    Obj2.Display("Amount After Deposit 100")
    Obj2.Withdraw(50,False)
    Obj2.Display("Amount After Withdraw 100")
    print("Calculated Interest is : " ,Obj2.CalculateIntrest())
   
#Entry Function        
if __name__ == "__main__":
    main()