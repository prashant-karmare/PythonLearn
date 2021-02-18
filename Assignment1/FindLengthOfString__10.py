"""
Write a program which accept name from user and display length of its name.
Input : Marvellous Output : 10
"""
def FindLengthOfStringUsingLoop(strname):    
    counter = 0   
    for _chr in strname:
        counter+=1
    return counter

def FindLengthOfStringStandardFunction(strname):    
   return len(strname)
    
   
def main():
    inputName=input("Enter Name : You want to check Length  ")    
    outputLength= FindLengthOfStringUsingLoop(inputName) 
    print(outputLength)
    length=FindLengthOfStringStandardFunction(inputName)
    print("Length is: ",length)
    
#Entry Function        
if __name__ == "__main__":
    main()