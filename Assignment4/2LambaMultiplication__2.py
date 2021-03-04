"""
Write a program which contains one lambda function which accepts two parameters and return
its multiplication.
Input : 4 3 Output : 12
Input : 6 3 Output : 18
"""
mult= lambda no1,no2: no1*no2

def main():
    print("Enter 2 Numbers for Multiplication")
    Num1=int(input())
    Num2=int(input())
    reslt = mult(Num1,Num2)
    print("Multiplication of {} & {} is: {}".format(Num1,Num2,reslt))

#Entry Function        
if __name__ == "__main__":
    main()