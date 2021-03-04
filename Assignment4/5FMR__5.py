"""
Write a program which contains filter(), map() and reduce() in it. Python application which
contains one list of numbers. List contains the numbers which are accepted from user. Filter
should filter out all prime numbers. Map function will multiply each number by 2. Reduce will
return Maximum number from that numbers. (You can also use normal functions instead of
lambda functions).
Input List = [2, 70 , 11, 10, 17, 23, 31, 77]
List after filter = [2, 11, 17, 23, 31]
List after map = [4, 22, 34, 46, 62]
Output of reduce = 62
"""
import functools as fc
# Filter filter out all prime numbers
def checkPrimeNo(no):
    for i in range(2,no):
        if no%i == 0:
            return False        
    else:
        if no == 1:
            return False
        else:
            return True
#Map function multiply each number by 2
def multby2(no):
    return no*2

#Reduce return Maximum number
def max(no1,no2):
    if(no1>no2):
        return no1
    else:
        return no2

def main():
    lst = []
    num = int(input("Enter how many elements you want:"))
    for i in range(num):
        no = int(input("Enter num {}:".format(i+1)))
        lst.append(no)

    filteredlist =list(filter(checkPrimeNo,lst))
    print("List after filter = : ",filteredlist) 
    mappedInclist = list(map(multby2,filteredlist)) 
    print("List after map = : ",mappedInclist) 
    result= fc.reduce(max,mappedInclist)    
    print("Output of reduce: ",result)

#Entry Function        
if __name__ == "__main__":
    main()