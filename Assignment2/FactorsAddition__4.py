"""
Write a program which accept one number form user and return addition of its factors.
Input : 12 Output : 16 (1+2+3+4+6)
"""
import math
def AddFactors(no):
    sumfact=0
    for i in range(1,int(no/2)+1):
        if no%i == 0:
            sumfact+=i
    return sumfact
        
def main():
    inputno=int(input("Enter Number for Factorial:"))
    reslt = AddFactors(inputno)
    print("Output : ",reslt)

#Entry Function        
if __name__ == "__main__":
    main()