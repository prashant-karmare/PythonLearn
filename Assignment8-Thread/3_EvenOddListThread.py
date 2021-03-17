"""
Design python application which creates two threads as evenlist and oddlist. Both the
threads accept list of integers as parameter. Evenlist thread add all even elements
from input list and display the addition. Oddlist thread add all odd elements from input
list and display the addition.

"""
import threading
from itertools import filterfalse
from functools import reduce

def EvenOddList(fun,lstInteger):
    fun(lstInteger)

def CheckEven(no):  
    if no % 2 == 0:
        return True
    else:
        return False
add= lambda no1,no2: no1+no2 
def DisplayEvenNosAddition(lstIntegers):
    addition = reduce(add,filter(CheckEven,lstIntegers))
    print("Even Nos Addition is : ",addition)
  
def DisplayOddNosAddition(lstIntegers):
    addition = reduce(add,filterfalse(CheckEven,lstIntegers))
    print("Odd Nos Addition is : ",addition)

def main():
    lst =[]
    print("Enter How many Element You want to add in List.?")
    rangeNO=int(input())
    for i in range(rangeNO):
        lst.append(int(input("Enter Element :{} ".format(i+1))))

    evenlist = threading.Thread(target=EvenOddList, args=(DisplayEvenNosAddition,lst))
    oddlist = threading.Thread(target=EvenOddList, args=(DisplayOddNosAddition,lst))

    evenlist.start()
    oddlist.start()

    evenlist.join()
    oddlist.join()

    print("exit from main")
    

#Entry Function        
if __name__ == "__main__":
    main()