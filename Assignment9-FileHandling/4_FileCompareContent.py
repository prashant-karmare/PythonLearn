"""
Write a program which accept two file names from user and compare contents of both the
files. If both the files contains same contents then display success otherwise display failure.
Accept names of both the files from command line.
Input : Demo.txt Hello.txt
Compare contents of Demo.txt and Hello.txt

"""

def CompareFileContent(filename1,filename2):    
    try:
        Fd1 = open(filename1,'r')
        Fd2 = open(filename2,'r')
        if Fd1.closed == False and Fd2.closed == False:
            if Fd1.read() == Fd2.read():
                    print("Success:  Both Files are Identical")
            else:
                print("Failure: OhNo.! Files are Not Same")
        Fd1.close()
        Fd2.close()

    except FileNotFoundError as err:
        print("File is Not present in Current Directory Details are -{}".format(err))
    except PermissionError as err1:
        print("File is Not Having Permission for Read in Current Directory Details are -{}".format(err1))
    except OSError as err2:
        print("Os Error -Invalid Args Details are -{}".format(err2))
    except IOError as err3:
          print("Unable to open/write File -{}".format(err3))

  
        

def main():
    print("Enter File Details for Comparison of Content:")
    fl1= input("Enter 1st File Name : ")
    fl2= input("Enter 2nd File Name : ")
    CompareFileContent(fl1,fl2)
   
if __name__ == "__main__":
    main()