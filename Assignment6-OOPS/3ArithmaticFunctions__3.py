"""
Write a program which contains one class named as Arithmetic.
Arithmetic class contains three instance variables as Value1 ,Value2.
Inside init method initialise all instance variables to 0.
There are three instance methods inside class as Accept(), Addition(), Subtraction(),
Multiplication(), Division().
Accept method will accept value of Value1 and Value2 from user.
Addition() method will perform addition of Value1 ,Value2 and return result.
Subtraction() method will perform subtraction of Value1 ,Value2 and return result.
Multiplication() method will perform multiplication of Value1 ,Value2 and return result.
Division() method will perform division of Value1 ,Value2 and return result.
After designing the above class call all instance methods by creating multiple objects.

"""
class Arithmetic:
    def __init__(self):
        self.Value1 = 0    #Instance Variable
        self.Value2 = 0

    def Accept(self,objName):
        print("----------")
        print("Enter Details for Arithmatic Operation for ",objName," :")
        self.Value1=int(input(" Enter Value 1 "))
        self.Value2=int(input(" Enter Value 2 "))

    def Addition(self):        
         reslt =  self.Value1 + self.Value2
         return reslt
    def Subtraction(self):        
         reslt =  self.Value1 - self.Value2
         return reslt         
    def Multiplication(self):        
         reslt =  self.Value1 * self.Value2
         return reslt
    def Division(self):
        if(self.Value2==0):
            reslt = " Sorry, Division is not posible due to 0 at Denominator "      
        else:
            reslt =  self.Value1 / self.Value2
        return reslt

    def Display(self,methdname,result):
        print("----------")
        print(" Result for {} is : {}".format(methdname,result))
      

  
def main():   
    Obj1 = Arithmetic()
    Obj2 = Arithmetic()
    Obj3 = Arithmetic()
    Obj1.Accept("Object 1")
    Obj2.Accept("Object 2")

    print("Below are Object 1 Details : ")
    ans = Obj1.Addition()
    Obj1.Display("Addition",ans)
    ans = Obj1.Subtraction()
    Obj1.Display("Subtraction",ans)
    ans = Obj1.Multiplication()
    Obj1.Display("Multiplication",ans)
    ans = Obj1.Division()
    Obj1.Display("Division",ans)

    print("Below are Object 2 Details : ")
    add = Obj2.Addition()
    sub = Obj2.Subtraction()
    mult = Obj2.Multiplication()
    div = Obj2.Division()

    Obj2.Display("Addition",add)
    Obj2.Display("Subtraction",sub)
    Obj2.Display("Multiplication",mult)
    Obj2.Display("Division",div)

    Obj3.Accept("Object 3")
    print("Below are Object 3 Details : ")
    Obj3.Display("Addition",Obj3.Addition())
    Obj3.Display("Subtraction",Obj3.Subtraction())
    Obj3.Display("Multiplication",Obj3.Multiplication())
    Obj3.Display("Division",Obj3.Division())

#Entry Function        
if __name__ == "__main__":
    main()