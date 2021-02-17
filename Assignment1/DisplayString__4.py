"""
Write a program which display 5 times Marvellous on screen.
Output : Marvellous
Marvellous
Marvellous
Marvellous
Marvellous
"""
def LoopString(cnt,msg):
    while cnt>0:
        print(msg)
        cnt-=1 
   
def main():
    LoopString(5,"Marvellous")
    
#Entry Function        
if __name__ == "__main__":
    main()