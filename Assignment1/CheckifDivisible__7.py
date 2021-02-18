"""
Write a program which contains one function that accept one number from user and returns
true if number is divisible by 5 otherwise return false.
Input : 8 Output : False
Input : 25 Output : True
"""
def CheckDivisible(no, divisibleno=5):    
    if(no%divisibleno==0):
        return True        
    else:
        return False
    
   
def main():
    inputno=int(input("Enter Number  for check:"))
    reslt= CheckDivisible(inputno) 
    print("Output : ",reslt)
    
#Entry Function        
if __name__ == "__main__":
    main()