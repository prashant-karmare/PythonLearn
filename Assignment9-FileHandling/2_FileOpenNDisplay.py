"""
Write a program which accept file name from user and open that file and display the contents
of that file on screen.
Input : Demo.txt
Display contents of Demo.txt on console.

"""
#import os  
  
def OpenFileNDisplayContent(): #Alternate Way
    print("Enter File Name to Open in Current Directory :")
    filename= input()
    try:
        Fd1 = open(filename,'r')
        print("Content of File : ")
        if Fd1.closed == False:
            print(Fd1.read())
            Fd1.close()
          
    except FileNotFoundError as err:
        print("File is Not present in Current Directory Details are -{}".format(err))
    except PermissionError as err1:
        print("File is Not Having Permission for Read in Current Directory Details are -{}".format(err1))
    except OSError as err2:
        print("Os Error -Invalid Args Details are -{}".format(err2))
    except IOError as err3:
          print("Unable to open File -{}".format(err3))
    

def main():
    OpenFileNDisplayContent()
if __name__ == "__main__":
    main()