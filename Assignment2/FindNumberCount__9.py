"""
Write a program which accept number from user and return number of digits in that number.
Input : 5187934 Output : 7
"""
def FindDigitCount(no):    
    counter = 0
    while no>0:
        counter+=1
        no=int(no/10)        
    return counter

def FindLengthOfDigitStandardFunction(no):    
   return len(str(no))
    
   
def main():
    inno=int(input("Enter Number : You want to check Digit Count  ") )
    outputLength= FindDigitCount(inno) 
    print(outputLength)
    length=FindLengthOfDigitStandardFunction(inno)
    print("Count is: ",length)
    
#Entry Function        
if __name__ == "__main__":
    main()