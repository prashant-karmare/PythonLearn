"""
Create on module named as Arithmetic which contains 4 functions as Add() for addition, Sub()
for subtraction, Mult() for multiplication and Div() for division. All functions accepts two
parameters as number and perform the operation. Write on python program which call all the
functions from Arithmetic module by accepting the parameters from user.
"""
import Arithmatic
def main():
    print("Enter Two Numbers for Arithmatic Operations:")
    inputNo1=int(input())
    inputNo2=int(input())
    resltAdd = Arithmatic.Add(inputNo1,inputNo2)
    print("Addition of {} & {} is: {}".format(inputNo1,inputNo2,resltAdd))
    resltSub = Arithmatic.Sub(inputNo1,inputNo2)
    print("Substraction of {} & {} is: {}".format(inputNo1,inputNo2,resltSub))
    resltMult = Arithmatic.Mult(inputNo1,inputNo2)
    print("Multiple of {} & {} is: {}".format(inputNo1,inputNo2,resltMult))
    if inputNo2 != 0:
        resltDiv = Arithmatic.Div(inputNo1,inputNo2)
        print("Division of {} & {} is: {}".format(inputNo1,inputNo2,resltDiv))
    else:
        print("Division is not possible if Divided by 0")


#Entry Function        
if __name__ == "__main__":
    main()