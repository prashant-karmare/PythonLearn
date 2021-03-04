"""
Write a recursive program which accept number from user and return its
factorial.
Input : 5
Output : 120
"""
#fact=1
def Fact(no): 
    fact =no
    if(no>1):
        no-=1
        fact = fact * Fact(no)        
    return fact
  
def main():
    inputno=int(input("Enter Number : "))
    ans=Fact(inputno)
    print("Factorial of num is: ",ans) 
  
    
#Entry Function        
if __name__ == "__main__":
    main()