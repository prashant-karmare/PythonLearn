"""
Write a program which contains filter(), map() and reduce() in it. Python application which
contains one list of numbers. List contains the numbers which are accepted from user. Filter
should filter out all such numbers which greater than or equal to 70 and less than or equal to
90. Map function will increase each number by 10. Reduce will return product of all that
numbers.
Input List = [4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70]
List after filter = [76, 89, 86, 90, 70]
List after map = [86, 99, 96, 100, 80]
Output of reduce = 6538752000
"""
import functools as fc
#Function for Filter no between 70 & 90
def CheckNoBeetween(no):
    if(no>=70 and no<=90):
        return True
    else:
        return False

#Map Function Increase each no by 10
def IncreaseByNo(no1,no2=10):
    return no1+no2

#Reduce  product of all No
product = lambda no1,no2: int(no1)*int(no2)

def main():
    lst = []
    num = int(input("Enter how many elements you want:"))
    for i in range(num):
        no = int(input("Enter num {}:".format(i+1)))
        lst.append(no)

    filteredlist =list(filter(CheckNoBeetween,lst))
    print("List after filter = : ",filteredlist) 
    mappedInclist = list(map(IncreaseByNo,filteredlist)) 
    print("List after map = : ",mappedInclist) 
    result= fc.reduce(product,mappedInclist)    
    print("Output of reduce: ",result)

#Entry Function        
if __name__ == "__main__":
    main()