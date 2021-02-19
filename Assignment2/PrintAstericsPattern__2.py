"""
Write a program which accept one number and display below pattern.
Input : 5
Output : 
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
"""
def printMatrics(no, char="*"):
    for _row in range(no):
        for _col in range(no):
            print(char, end=" ")
        print()
        
      

def main():
    inputno=int(input("Enter Number :"))
    #inputchar= input("Enter character you want to print:")
    #result=printMatrics(inputno,inputchar)
    printMatrics(inputno) 
    #print(output)
    
#Entry Function        
if __name__ == "__main__":
    main()