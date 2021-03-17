"""
Design python application which contains two threads named as thread1 and thread2.
Thread1 display 1 to 50 on screen and thread2 display 50 to 1 in reverse order on
screen. After execution of thread1 gets completed then schedule thread2.

"""
import threading

def Threads(fun,strname,locker):  
    fun(strname,locker)
def Thread1(no,lock):
    lock.acquire()
    for i in range(1,no+1):
        print(i)  
    lock.release()
def Thread2(no,lock):
    lock.acquire()
    for i in range(no,0,-1):
        print(i)    
    lock.release()

    
def main():
    #print("Enter the No : ")
    #no = int(input())
    no = 50
    lock = threading.Lock()
    thread1 = threading.Thread(target= Threads,args=(Thread1,no,lock,))
    thread2 = threading.Thread(target= Threads,args=(Thread2,no,lock,))
    print("Thread1 Displaying 1 to 50")
    thread1.start()   
    thread1.join()

    print("Thread2 Displaying 50 to 1")
    thread2.start()
    thread2.join()

#Entry Function        
if __name__ == "__main__":
    main()