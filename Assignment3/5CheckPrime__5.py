"""
Write a program which accept N numbers from user and store it into List. Accept one another
number from user and return frequency of that number from List.
Input : Number of elements : 11
Input Elements : 13 5 45 7 4 56 5 34 2 5 65
Element to search : 5
Output : 3
"""
import MarvellousNum
def ListPrime(lst):
    addPrime = 0
    for i in range(len(lst)):
        reslt = MarvellousNum.ChkPrime(lst[i])
        if(reslt== True):
            addPrime+=lst[i] 
    return addPrime

def main():
    lst = []
    num = int(input("Enter how many elements you want: "))
    for i in range(num):
        no = int(input("Enter no {}: ".format(i+1)))
        lst.append(no)
    result= ListPrime(lst)    
    print("Addition of All Prime No is: ",result)
    
#Entry Function        
if __name__ == "__main__":
    main()