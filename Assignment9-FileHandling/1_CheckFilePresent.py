"""
Write a program which accepts file name from user and check whether that file exists in
current directory or not.
Input : Demo.txt
Check whether Demo.txt exists or not.
"""
import os  
Currentpath=''
def getCurrentDirectoryFiles():
    global Currentpath    
    Currentpath = os.getcwd()  #Path having Current Working Directory/-root
    dir_list = os.listdir(Currentpath) #List of all files and folder for Given Path      
    return dir_list
display = lambda lst:print("List Contains :",lst)  
def CheckFileInLstFiles(filename,lstFiles):
    if filename in lstFiles:
        return True
    else:
        return False
def AcceptFileNameNDisplay():
    global Currentpath
    fileslist =getCurrentDirectoryFiles()
    displayall = input("Do You want to display all Files in Current Directory: Reply with yes/Yes/YES or y/Y : ") 
    if displayall.lower() == "yes" or displayall.lower() == "y":
            display(fileslist)
    print("Enter File Name to check in Current Directory :")
    filename= input()

    if(CheckFileInLstFiles(filename,fileslist)==True):
        print("Exist** File {} is Present In Current Directory {}".format(filename,os.path.basename(Currentpath)))
    else:
        print("Does Not EXist** File {} is Not Found In Current Directory {}".format(filename,os.path.basename(Currentpath)))
        ChangePathNCheck()

def ChangePathNCheck():
    changedir = input("Do You want to change Directory .? press y if yes : ") 
    if changedir.lower() == "y":
        userPath = input("Enter complete Path : ") 
        try:
            os.chdir(userPath) 
            print("Current New Path is :",os.getcwd())
            repeat = input("Do You want to repeat Procedure with New Directory .? press y if yes : ") 
            if repeat.lower() == "y":
                AcceptFileNameNDisplay()
        except FileNotFoundError as error:
            print("Path Not Found..! Please Select Correct Path & Try Again Later -Error Details:- {}".format(error))       
def CheckFileByOpen(): #Alternate Way
    print("Enter File Name to check in Current Directory :")
    filename= input()
    try:
        Fd1 = open(filename,'r')
        if Fd1.closed == False:
            print("File Found In Current Directory")
            Fd1.close()
          
    except FileNotFoundError as err:
        print("File is Not present in Current Directory Details are -{}".format(err))
    except PermissionError as err1:
        print("File is Not Having Permission for Read in Current Directory Details are -{}".format(err1))
    except OSError as err2:
        print("Os Error -Invalid Args Details are -{}".format(err2))
    except IOError as err3:
          print("Unable to open File -{}".format(err3))
    finally:        
        displayall = input("Do You want to display all Files in Current Directory: Reply with yes/Yes/YES or y/Y : ") 
        if displayall.lower() == "yes" or displayall.lower() == "y":
            fileslist =getCurrentDirectoryFiles()
            display(fileslist)

def main():
    AcceptFileNameNDisplay()
    #OR U Can Use -> # CheckFileByOpen()
if __name__ == "__main__":
    main()