"""
Write a program which display 10 to 1 on screen.
Output : 10 9 8 7 6 5 4 3 2 1
"""
def LoopReverse(no):   
    strout = ""
    while no>0:
        strout +=str(no) + " "
        #print(no)
        no-=1
    return strout
    
   
def main():
    output= LoopReverse(10)
    print("Output : "+output)
    
#Entry Function        
if __name__ == "__main__":
    main()