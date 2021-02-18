"""
Write a program which accept number from user and print that number of “*” on screen.
Input : 5 Output : * * * * *
"""
def printNCharacters(no, char="*"):
    strOutput=""   
    while(no>0):
        strOutput +=char + " "
        no-=1
    return strOutput
    
   
def main():
    inputno=int(input("Enter Number :"))
    #inputchar= input("Enter character you want to print:")
    #result=printNCharacters(inputno,inputchar)
    output= printNCharacters(inputno) 
    print(output)
    
#Entry Function        
if __name__ == "__main__":
    main()