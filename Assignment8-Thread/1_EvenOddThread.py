"""
Design python application which creates two thread named as even and odd. Even
thread will display first 10 even numbers and odd thread will display first 10 odd
numbers.

"""
import threading

def EvenOdd(fun,uptoRange):
    fun(uptoRange)


def DisplayEvenListUptoNo(no):
    rangenos = range(no)
    evencounter = 0
    lstEvenNos = []
    for _i in rangenos:
        lstEvenNos.append(evencounter)
        evencounter += 2        
    print("Even  Nos are : ",lstEvenNos)
    #return lstEvenNos
def DisplayOddListUptoNo(no):
    rangenos = range(no)
    oddcounter = 1
    lstOddNos = []
    for _i in rangenos:
        lstOddNos.append(oddcounter)
        oddcounter += 2
        
    print("Odd  Nos are : ",lstOddNos)

def main():
    #print("Enter Number")
    #rangeNO=int(input())
    rangeNO = 10
    even = threading.Thread(target=EvenOdd, args=(DisplayEvenListUptoNo,rangeNO))
    odd = threading.Thread(target=EvenOdd, args=(DisplayOddListUptoNo,rangeNO))

    even.start()
    odd.start()

    even.join()
    odd.join()
    

#Entry Function        
if __name__ == "__main__":
    main()