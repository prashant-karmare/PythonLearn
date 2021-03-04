"""
Write a recursive program which display below pattern.
Input : 5
Output : 1 2 3 4 5
"""
def printMatrics(no,counter=1):
    if(counter<=no):
        print(" ",counter, end=" " )
        counter +=1
        printMatrics(no,counter)

def main():
    inputno=int(input("Enter Number  : "))    
    printMatrics(inputno) 
  
    
#Entry Function        
if __name__ == "__main__":
    main()