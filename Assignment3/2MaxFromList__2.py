"""
Write a program which accept N numbers from user and store it into List. Return Maximum
number from that List.
Input : Number of elements : 7
Input Elements : 13 5 45 7 4 56 34
Output : 56
"""
def Max(lst):
    if(len(lst)>0):   
        maxno = lst[0]    
        for i in range(len(lst)):
            if(maxno<lst[i]):
                maxno=lst[i]  
    return maxno
   
def main():
    lst = []
    num = int(input("Enter how many elements you want:"))
    for i in range(num):
        no = int(input("Enter num {}:".format(i+1)))
        lst.append(no)
    result= Max(lst)    
    print("Maximum no of List  is: ",result)
    
#Entry Function        
if __name__ == "__main__":
    main()