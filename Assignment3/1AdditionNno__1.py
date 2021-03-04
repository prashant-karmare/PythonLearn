"""
Write a program which accept N numbers from user and store it into List. Return addition of all
elements from that List.
Input : Number of elements : 6
Input Elements : 13 5 45 7 4 56
Output : 130
"""
def ListNnoAddition(lst):    
    sum = 0
    for i in range(len(lst)):
        sum +=lst[i]    
    return sum
   
def main():
    lst = []
    num = int(input("Enter how many elements you want:"))
    for _i in range(num):
        no = int(input("Enter num :"))
        lst.append(no)
    result= ListNnoAddition(lst)    
    print("Addition of List  is: ",result)
    
#Entry Function        
if __name__ == "__main__":
    main()