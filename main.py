import functions

if __name__ == '__main__':
    #source = "C://Users//skato//Desktop//algorithms//o_n.py"
    source = "C://Users//skato//Desktop//algorithms//kappa keepo.txt"
    dest = "C://Users//skato//Desktop//end"
    if ("." in source):
        check = False
    else:
        check = True
    functions.checkAndCopy(source, dest, check)