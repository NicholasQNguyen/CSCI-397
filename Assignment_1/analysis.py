"""
Program to crack encrypted.txt
"""


def main():
    encrypted = open("encrypted.txt", "r")
    decrypted = open("decrypted.txt", "w")
    # Go through the encrypted text and get the number of each letter
    # and put it in this dictionary
    freqTable = {"a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0,
                 "g": 0, "h": 0, "i": 0, "j": 0, "k": 0, "l": 0,
                 "m": 0, "n": 0, "o": 0, "p": 0, "q": 0, "r": 0,
                 "s": 0, "t": 0, "u": 0, "v": 0, "w": 0, "x": 0,
                 "y": 0, "z": 0}

    # http://pi.math.cornell.edu/~mec/2003-2004/cryptography/subs/frequencies.html
    # A list of all letters put in order of frequency
    # (e is most common then t)
    realFreqTable = ["e", "t", "a", "o", "i", "n", "s", "r", "h",
                     "d", "l", "u", "c", "m", "f", "y", "w", "g",
                     "p", "b", "v", "k", "x", "q", "j", "z", " ",
                     ".", ","]
    encryptedFreqTable = []
    lines = encrypted.readlines()
    # print(lines)
    # https://stackoverflow.com/questions/1155617/count-the-number-of-occurrences-of-a-character-in-a-string
    # Count number of times each letter appears
    for word in lines:
        for key in freqTable:
            freqTable[key] += word.count(key)

    for key in freqTable:
        print(key + ":", end="")
        print(freqTable[key])

    # Make a list in order of appearance frequency
    while freqTable != {}:
        highestKey = "a"
        for key in freqTable:
            if freqTable[key] > freqTable[highestKey]:
                highestKey = key
        
        encryptedFreqTable.append(highestKey)
        freqTable.pop(highestKey)   

    encryptedFreqTable.append(" ")
    encryptedFreqTable.append(".")
    encryptedFreqTable.append(",")
    print(encryptedFreqTable)


        

if __name__ == "__main__":
    main()
