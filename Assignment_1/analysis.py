"""
Program to crack encrypted.txt
"""

def main():
    freqTable = {"a":0, "b":0, "c":0, "d":0, "e":0, "f":0,
     "g":0, "h":0, "i":0, "j":0, "k":0, "l":0, "m":0, "n":0,
     "o":0, "p":0, "q":0, "r":0, "s":0, "t":0, "u":0, "v":0,
     "w":0, "x":0, "y":0, "z":0}
    encrypted = open("encrypted.txt", "r")
    # https://stackoverflow.com/questions/1155617/count-the-number-of-occurrences-of-a-character-in-a-string
    for word in encrypted:
        for key in freqTable:
            freqTable[key] += word.count(key)
            print(word)

if __name__ == "__main__":
    main()