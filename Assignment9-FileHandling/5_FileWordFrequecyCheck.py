"""
Accept file name and one string from user and return the frequency of that string from file.
Input : Demo.txt Marvellous
Search “Marvellous” in Demo.txt

"""

def FindStringCountInFile(filename,substring):    
    try:
        Fd1 = open(filename,'r')       
        if Fd1.closed == False:
            count = Fd1.read().count(substring)
            print("Frequency of the String in File is: ",count)

    except FileNotFoundError as err:
        print("File is Not present in Current Directory Details are -{}".format(err))
    except PermissionError as err1:
        print("File is Not Having Permission for Read in Current Directory Details are -{}".format(err1))
    except OSError as err2:
        print("Os Error -Invalid Args Details are -{}".format(err2))
    except IOError as err3:
          print("Unable to open/write File -{}".format(err3))

    
def main():
    print("Enter Details:")
    filename= input("Enter File Name : ")
    strng= input("Enter String You want to Find Frequency: ")
    FindStringCountInFile(filename,strng)
   
if __name__ == "__main__":
    main()