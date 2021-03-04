"""
Write a recursive program which display below pattern.
Input : 5
Output : 5 4 3 2 1
"""
def printRevNo(no):
    if(no>0):
        print(" ",no, end=" " )
        no -=1
        printRevNo(no)

def main():
    inputno=int(input("Enter Number : "))
    printRevNo(inputno) 
  
    
#Entry Function        
if __name__ == "__main__":
    main()