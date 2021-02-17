"""
Write a program which accept number from user and check whether that number is positive or
negative or zero.
Input : 11 Output : Positive Number
Input : -8 Output : Negative Number
Input : 0 Output : Zero
"""
def CheckPostiveNegativeNo(no):   
    strout = ""
    if(no>0):
        strout = "Positive Number"
    elif(no<0):
        strout= "Negative Number"
    else:
        strout= "Zero"    
    return strout
    
   
def main():
    inputno=int(input("Enter Number :"))
    output= CheckPostiveNegativeNo(inputno)
    print("Output : "+output)
    
#Entry Function        
if __name__ == "__main__":
    main()