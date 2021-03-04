"""
Write a program which contains one lambda function which accepts one parameter and return
power of two.
Input : 4 Output : 16
Input : 6 Output : 64
"""
power= lambda powerno,baseno=2: (baseno**powerno)

def main():
    print("Enter Number")
    inputNO=int(input())
    #base=int(input("Enter BaseNo:"))
    #reslt = power(inputNO,base)
    reslt = power(inputNO)
    print("Power of 2 raise to {} is: {}".format(inputNO,reslt))

#Entry Function        
if __name__ == "__main__":
    main()