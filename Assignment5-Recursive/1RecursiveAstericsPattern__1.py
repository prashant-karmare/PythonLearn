"""
Write a recursive program which display below pattern.
Input : 5
Output : * * * * *
"""
def printMatrics(no, char="*"):
    if(no>0):
        print(" ",char, end=" " )
        no -=1
        printMatrics(no,char)

def main():
    inputno=int(input("Enter Number : "))
    #inputchar= input("Enter character you want to print: ")
    #printMatrics(inputno,inputchar)
    printMatrics(inputno) 
  
    
#Entry Function        
if __name__ == "__main__":
    main()