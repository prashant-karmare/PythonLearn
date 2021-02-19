"""
Write a program which accept number from user and return addition of digits in that number.
Input : 5187934 Output : 37
"""
def FindDigitAddition(no):    
    digitAddition = 0
    while no>0:
        digitAddition += no%10
        no=int(no/10)        
    return digitAddition

   
def main():
    inno=int(input("Enter Number : You want to check Digit Count  ") )
    result= FindDigitAddition(inno)    
    print("Addition of Digit  is: ",result)
    
#Entry Function        
if __name__ == "__main__":
    main()