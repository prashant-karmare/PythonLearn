"""
Design python application which creates two threads as evenfactor and oddfactor.
Both the thread accept one parameter as integer. Evenfactor thread will display
addition of even factors of given number and oddfactor will display addition of odd
factors of given number. After execution of both the thread gets completed main
thread should display message as “exit from main”.
"""
import threading

def EvenOdd(fun,uptoRange):
    fun(uptoRange)

def AddFactors(no,EvenOrOdd):
    #print("Operation ",EvenOrOdd)
    sumfact=0
    for i in range(1,int(no/2)+1):
        if ((no%i == 0)and(((EvenOrOdd =='even') and (i%2 == 0)) or (EvenOrOdd =='odd' and i%2 != 0)or(EvenOrOdd =='all'))):
            sumfact+=i
    return sumfact

def DisplayEvenFactorsAddition(no):
    addition = AddFactors(no,'even')
    print("Even No Factors Addition is : ",addition)
  
def DisplayOddFactorsAddition(no):
    addition = AddFactors(no,'odd')
    print("Odd No Factors Addition is : ",addition)

def main():
    print("Enter Number")
    rangeNO=int(input())
    Evenfactor = threading.Thread(target=EvenOdd, args=(DisplayEvenFactorsAddition,rangeNO))
    oddfactor = threading.Thread(target=EvenOdd, args=(DisplayOddFactorsAddition,rangeNO))

    Evenfactor.start()
    oddfactor.start()

    Evenfactor.join()
    oddfactor.join()

    print("exit from main")
    

#Entry Function        
if __name__ == "__main__":
    main()