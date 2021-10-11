"""
Author: Nicholas Nguyen
File: analysis.py

Program to crack encrypted.txt
Worked with Nobel Manaye
"""


# Method used to help when manual swapping letters in the frequency table
def manualMap(dictionary, letter1, letter2, letter3, letter4):
    dictionary[letter1] = letter2
    dictionary[letter3] = letter4


def main():
    # Open and read the lines in the text file
    encrypted = open("encrypted.txt", "r")
    lines = encrypted.readlines()
    # A dictionary for when we go through the text that
    # stores the frequency that each letter appears
    freqTable = {"a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0,
                 "g": 0, "h": 0, "i": 0, "j": 0, "k": 0, "l": 0,
                 "m": 0, "n": 0, "o": 0, "p": 0, "q": 0, "r": 0,
                 "s": 0, "t": 0, "u": 0, "v": 0, "w": 0, "x": 0,
                 "y": 0, "z": 0}
    # An array representation of the above dictionary with the index
    # representing the frequency order
    encryptedFreqTable = []

    # http://pi.math.cornell.edu/~mec/2003-2004/cryptography/subs/frequencies.html
    # A list of all letters put in order of frequency
    # (e is most common then t, then a, etc)
    realFreqTable = ["e", "t", "a", "o", "i", "n", "s", "r", "h",
                     "d", "l", "u", "c", "m", "f", "y", "w", "g",
                     "p", "b", "v", "k", "x", "q", "j", "z", " ",
                     ",", "."]

    # https://stackoverflow.com/questions/1155617/count-the-number-of-occurrences-of-a-character-in-a-string
    # Count number of times each letter appears
    for word in lines:
        for key in freqTable:
            freqTable[key] += word.count(key)

    # Make a list in order of appearance frequency
    while freqTable != {}:
        highestKey = "a"
        for key in freqTable:
            if freqTable[key] > freqTable[highestKey]:
                highestKey = key

        encryptedFreqTable.append(highestKey)
        freqTable.pop(highestKey)

    # Append " ", ",", and "." to avoid errors when substituting
    encryptedFreqTable.append(" ")
    encryptedFreqTable.append(".")
    encryptedFreqTable.append(",")

    # Make a dictionary mapping the generated frequency table to the
    # real frequency table
    # https://www.geeksforgeeks.org/python-convert-two-lists-into-a-dictionary/
    mappingDict = {}
    for key in encryptedFreqTable:
        for value in realFreqTable:
            mappingDict[key] = value
            realFreqTable.remove(value)
            break

    # Manual swapping
    # d <-> i
    manualMap(mappingDict, "d", "i", "z", "o")
    # f <-> s
    manualMap(mappingDict, "f", "s", "v", "d")
    # i <-> g
    manualMap(mappingDict, "i", "g", "h", "v")
    # u <-> d
    manualMap(mappingDict, "u", "d", "v", "h")
    # g <-> b
    manualMap(mappingDict, "g", "b", "e", "f")
    # c <-> t
    manualMap(mappingDict, "c", "t", "n", "e")
    # j <-> l
    manualMap(mappingDict, "j", "l", "y", "r")
    # m <-> x
    manualMap(mappingDict, "m", "x", "b", "q")
    # e <-> k
    manualMap(mappingDict, "e", "k", "w", "f")
    # w <-> v
    manualMap(mappingDict, "w", "v", "h", "f")
    # t <-> f
    manualMap(mappingDict, "t", "f", "h", "p")
    # p <-> q
    manualMap(mappingDict, "p", "q", "b", "j")
    # b <-> z
    manualMap(mappingDict, "b", "z", "a", "j")

    # Print a newline to make thing prettier
    print("\n")
    # Substitute the encrypted letters for their corresponding real letters
    # and print out the text
    for word in lines:
        for letters in word:
            print(mappingDict[letters], end="")
    # Print a newline so my terminal isn't ugly
    print("\n")


if __name__ == "__main__":
    main()
