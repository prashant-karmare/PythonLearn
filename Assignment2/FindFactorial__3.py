"""
Write a program which accept one number from user and return its factorial.
Input : 5 Output : 120
"""

def Factorial(no):
    fact = no
    while no>1:
        fact = fact * (no-1)        
        no-=1
    return fact
def main():
    inputno=int(input("Enter Number for Factorial:"))
    reslt = Factorial(inputno)
    print("Output : ",reslt)

#Entry Function        
if __name__ == "__main__":
    main()