"""
Write a recursive program which accept number from user and return
summation of its digits.
Input : 879
Output : 24
"""
sum = 0
def DigitAdd(no): 
    global sum
    if(no>0): 
        sum += no%10         
        no =int(no/10)
        DigitAdd(no)
    return sum

def main():
    inputno=int(input("Enter Number : "))
    addtn=DigitAdd(inputno)
    print("Addition of digit  are: ",addtn) 
  
    
#Entry Function        
if __name__ == "__main__":
    main()