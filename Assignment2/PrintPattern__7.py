"""
Write a program which accept one number and display below pattern.
Input : 5
Output : 
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
"""
def printMatrics(no, char="*"):

    for _row in range(no):
        for col in range(no):
            print(col+1, end=" ")
        print()
        

def main():
    inputno=int(input("Enter Number :"))    
    printMatrics(inputno) 
    
    
#Entry Function        
if __name__ == "__main__":
    main()