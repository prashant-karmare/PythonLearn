"""
Write a program which accept one number for user and check whether number is prime or not.
Input : 5 Output : It is Prime Number
"""
def checkPrimeNo(no):
    for i in range(2,no):
        if no%i == 0:
            return False
    else:
        return True
        
def main():
    inputno=int(input("Enter Number:"))
    reslt = checkPrimeNo(inputno)
    if reslt ==True:
        print("It Is Prime Number")
    else:
        print("It Is Not a Prime Number")

#Entry Function        
if __name__ == "__main__":
    main()