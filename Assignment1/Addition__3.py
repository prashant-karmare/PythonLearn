"""
Write a program which contains one function named as Add() which accepts two numbers
from user and return addition of that two numbers.
Input : 11 5 Output : 16
"""
def Add(no1,no2):
   return no1+no2   

def main():
    print("Enter Two Numbers for Addition:")
    inputNo1=int(input())
    inputNo2=int(input())
    resltAdd = Add(inputNo1,inputNo2)
    print("Addition of {} & {} is: {}".format(inputNo1,inputNo2,resltAdd))
#Entry Function        
if __name__ == "__main__":
    main()