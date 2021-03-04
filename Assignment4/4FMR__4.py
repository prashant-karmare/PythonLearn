"""
Write a program which contains filter(), map() and reduce() in it. Python application which
contains one list of numbers. List contains the numbers which are accepted from user. Filter
should filter out all such numbers which are even. Map function will calculate its square.
Reduce will return addition of all that numbers.
Input List = [5, 2, 3, 4, 3, 4, 1, 2, 8, 10]
List after filter = [2, 4, 4, 2, 8, 10]
List after map = [4, 16, 16, 4, 64, 100]
Output of reduce = 204
"""
import functools as fc
#Function for filter out all such numbers which are even
checkEven = lambda no: (no%2==0)

#Map function calculate square
squareOfNo= lambda no:(no*no)

#Reduce return addition of all numbers
addition = lambda no1,no2: int(no1)+int(no2)

def main():
    lst = []
    num = int(input("Enter how many elements you want:"))
    for i in range(num):
        no = int(input("Enter num {}:".format(i+1)))
        lst.append(no)

    filteredlist =list(filter(checkEven,lst))
    print("List after filter = : ",filteredlist) 
    mappedInclist = list(map(squareOfNo,filteredlist)) 
    print("List after map = : ",mappedInclist) 
    result= fc.reduce(addition,mappedInclist)    
    print("Output of reduce: ",result)

#Entry Function        
if __name__ == "__main__":
    main()