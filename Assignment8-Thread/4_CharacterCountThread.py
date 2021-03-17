"""
Design python application which creates three threads as small, capital, digits. All the
threads accepts string as parameter. Small thread display number of small characters,
capital thread display number of capital characters and digits thread display number of
digits. Display id and name of each thread.

"""
import threading

def findSmallChar(char):
    if char >='a' and char <='z':
        return True
def findCapitalChar(char):
    if char >='A' and char <='Z':
        return True
def findDigitChar(char):
    if char >='0' and char <='9':
        return True

def CharacterCount(fun,strname):  #,locker
    print("Name of Thread: ",threading.current_thread().name)
    print("Id of Thread: ",threading.get_ident())
    fun(strname)#,locker
def displayNoOfSmallCharsInString(strng):#,lockString
    #lockString.acquire()
    noOfChars = len(list(filter(findSmallChar,list(strng))))
    print("No of Small Character in String are : ",noOfChars)
    #lockString.release()
def displayNoOfCapitalCharsInString(strng):#,lockString
    #lockString.acquire()
    noOfChars = len(list(filter(findCapitalChar,list(strng))))
    print("No of Capital Character in String are : ",noOfChars)
    #lockString.release()
def displayNoOfDigitCharsInString(strng):#,lockString
    #lockString.acquire()
    noOfChars = len(list(filter(findDigitChar,list(strng))))
    print("No of Digits in String are : ",noOfChars)
    #lockString.release()

    
def main():
    print("Enter the String : ")
    strParam = input()
    #lock = threading.Lock()
    small = threading.Thread(target= CharacterCount,args=(displayNoOfSmallCharsInString,strParam,))#lock,
    capital = threading.Thread(target= CharacterCount,args=(displayNoOfCapitalCharsInString,strParam,))#lock,
    digits = threading.Thread(target= CharacterCount,args=(displayNoOfDigitCharsInString,strParam,))#lock,
    small.start()
    capital.start()
    digits.start()
    small.join()
    digits.join()
    capital.join()

#Entry Function        
if __name__ == "__main__":
    main()