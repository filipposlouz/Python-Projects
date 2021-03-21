import shutil
import os

def fileCopy (src, dest):
    shutil.copy2(src, dest)
    return print("file copied")


def folderCopy (src, dest):
    shutil.copytree(src, dest)
    return print("folder copied")


def checkAndCopy (src, dest, check):
    if (check == True):
        if (not os.path.exists(src)):
            print("source file doesn't exist")
            exit()
        else:
            if (os.path.exists(dest)):
                print("Folder already exists.\nReplace? (y/n)")
                temp = input()
                if (temp == "y"):
                    shutil.rmtree(dest)
                    folderCopy(src, dest)
                else:
                    print("Exiting..")
                    exit()
            else:
                folderCopy(src, dest)
    else:
        fileCopy(src, dest)
    return 0
