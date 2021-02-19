"""
Write a program which accept one number and display below pattern.
Input : 5
Output : 
* * * * *
* * * *
* * *
*
"""
def printMatrics(no, char="*"):
    decrementer = no
    for _row in range(decrementer):
        for _col in range(decrementer):
            print(char, end=" ")
        print()
        decrementer-=1
        
      

def main():
    inputno=int(input("Enter Number :"))
    #inputchar= input("Enter character you want to print:")
    #printMatrics(inputno,inputchar)
    printMatrics(inputno) 
    
    
#Entry Function        
if __name__ == "__main__":
    main()