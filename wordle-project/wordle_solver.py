import pandas as pd

df = pd.read_fwf("possible_words.txt", header=None)

def getGuesses():
    green_info = {}
    yellow_info = {}
    green = input("Are there any greens? (y/n)\n")
    if (green == "y"):
        print("What was the letter and position? (letter position)/(end)")
        while (True):
            val = input()
            if (val == 'end'):
                break
            val = val.split(" ")
            green_info[val[0]] = int(val[1])-1

    yellow = input("Are there any yellows? (y/n)\n")
    if (yellow == "y"):
        print("What was the letter and position? (letter position)")
        while (True):
            val = input()
            if (val == 'end'):
                break
            val = val.split(" ")
            yellow_info[val[0]] = int(val[1])-1
    black_info = input("What are the not included letters?\n")

    return green_info, yellow_info, black_info


def computeAnswers(green_info, yellow_info, black_info):
    counter = 0
    first_list = []
    updated_list = []
    for key, val in green_info.items():
        if (counter == 0):
            for index, row in df.iterrows():
                word = row[0]
                if (word[val] == key):
                    first_list.append(word)
            counter = 1
            updated_list = first_list
        else:
            updated_list = []
            for word in first_list:
                if (word[val] == key):
                    updated_list.append(word)
            first_list = updated_list

    for key, val in yellow_info.items():
        if (len(updated_list) == 0):
            for index, row in df.iterrows():
                word = row[0]
                for char in word:
                    if (char == key):
                        if (len(str(val)) > 1):
                            if (len(str(val)) == 2):
                                if (word[int(str(val)[0])-1] != key and word[int(str(val)[1])] != key):
                                    updated_list.append(word)
                            if (len(str(val)) == 3):
                                if (word[int(str(val)[0])-1] != key and word[int(str(val)[1])-1] != key and word[int(str(val)[2])] != key):
                                    updated_list.append(word)
                        else:
                            if (word[val] != key):
                                updated_list.append(word)
            first_list = updated_list
        else:
            updated_list = []
            for word in first_list:
                for char in word:
                    if (char == key):
                        if (len(str(val)) > 1):
                            if (len(str(val)) == 2):
                                if (word[int(str(val)[0])-1] != key and word[int(str(val)[1])] != key):
                                    updated_list.append(word)
                            if (len(str(val)) == 3):
                                if (word[int(str(val)[0])-1] != key and word[int(str(val)[1])-1] != key and word[int(str(val)[2])] != key):
                                    updated_list.append(word)
                        else:
                            if (word[val] != key):
                                updated_list.append(word)
            first_list = updated_list

    included = False
    if (len(updated_list) == 0):
        for index, row in df.iterrows():
            word = row[0]
            for char in word:
                for letter in black_info:
                    if (char == letter):
                        included = True
                        break
                if (included == True):
                    break
            if (included == False):
                updated_list.append(word)
            included = False
    else:
        updated_list = []
        for word in first_list:
            for char in word:
                for letter in black_info:
                    if (char == letter):
                        included = True
                        break
                if (included == True):
                    break
            if (included == False):
                updated_list.append(word)
            included = False
    return updated_list


if __name__ == "__main__":
    # first_guess = "other"
    # second_guess = "nails"
    green_info, yellow_info, black_info = getGuesses()
    guess = computeAnswers(green_info, yellow_info, black_info)
    print(guess)