"""
Write a program which accept N numbers from user and store it into List. Return Minimum
number from that List.
Input : Number of elements : 4
Input Elements : 13 5 45 7
Output : 5
"""
def Min(lst):
    if(len(lst)>0):   
        minno = lst[0]    
        for i in range(len(lst)):
            if(minno>lst[i]):
                minno=lst[i]  
    return minno
   
def main():
    lst = []
    num = int(input("Enter how many elements you want: "))
    for i in range(num):
        no = int(input("Enter num {}: ".format(i+1)))
        lst.append(no)
    result= Min(lst)    
    print("Minimum no of List  is: ",result)
    
#Entry Function        
if __name__ == "__main__":
    main()