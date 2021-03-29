"""
Write a program which accept file name from user and create new file named as Demo.txt and
copy all contents from existing file into new file. Accept file name through command line
arguments.
Input : ABC.txt
Create new file as Demo.txt and copy contents of ABC.txt in Demo.txt

"""

def CopyContenttoSecondFile(filename,toWriteFileName):    
    try:
        Fd1 = open(filename,'r')
        writefd = open(toWriteFileName,'w')
        if Fd1.closed == False:
            writefd.write(Fd1.read())
            Fd1.close()
            writefd.close()
            print("**File Copied Successfully**")
    except FileNotFoundError as err:
        print("File is Not present in Current Directory Details are -{}".format(err))
    except PermissionError as err1:
        print("File is Not Having Permission for Read in Current Directory Details are -{}".format(err1))
    except OSError as err2:
        print("Os Error -Invalid Args Details are -{}".format(err2))
    except IOError as err3:
          print("Unable to open/write File -{}".format(err3))
    
def readfileDisplayContent(filename):
    try:
        ReadFile = open(filename,'r')
        if ReadFile.closed == False:           
            print("Contennt of File {} are --".format(filename))
            print(ReadFile.read())
            ReadFile.close()
    except FileNotFoundError as err:
        print("File is Not present in Current Directory Details are -{}".format(err))
def main():
    print("Enter File Name For Copy Data to Demo File in Current Directory :")
    filename= input()
    CopyContenttoSecondFile(filename,"Demo.txt")
    readfileDisplayContent("Demo.txt")
if __name__ == "__main__":
    main()