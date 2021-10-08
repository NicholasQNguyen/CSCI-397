"""
Program to crack hashed passwords from shadow.txt using dictionary.txt
"""
import hashlib
from hashlib import blake2b

def main():
    dictionary = open("dictionary.txt", "r")
    passwords = open("password,txt", "w")
    shadow = open("shadow", "r")

    shadowHashes = []

    # https://docs.python.org/3/library/hashlib.html
    m = hashlib.md5()

    # Create a list of just the hashes w/o the user#: and \n
    for line in shadow:
        shadowHashes.append(line[6:].strip())

    # for hash in shadowHashes:
    #     print(hash)

    #Go through the lines of the dictionary
    for line in dictionary:
        encodedLine = line.encode()
        hashedLine = hashlib.sha256(encodedLine).hexdigest()
        #hash the line
        # print(hashedLine)
        #go through the lines of shadowHashes
        for hashes in shadowHashes:
            # print(hashes)
            #Compare the hash we calculated to each of the shadowHashes
            if hashedLine == hashes:
                #If we get a match, print out line
                print(line)

    for i in range(100000):
        #try to hash it with every salt 1-99999
        #append i onto the string we'll hash
        None

if __name__ == "__main__":
    main()