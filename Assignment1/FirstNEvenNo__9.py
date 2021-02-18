"""
Write a program which display first 10 even numbers on screen.
Output : 2 4 6 8 10 12 14 16 18 20
"""
def FirstNEvenNo(no=10):
    strOutput=""
    evenNO = 2   
    while(no>0):
        strOutput +=str(evenNO) + " " 
        evenNO+=2
        no-=1      
    return strOutput
    
   
def main():
    #inputno=int(input("Enter Number Upto You want to get Even no:"))    
    output= FirstNEvenNo() 
    print(output)
    
#Entry Function        
if __name__ == "__main__":
    main()