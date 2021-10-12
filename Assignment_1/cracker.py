"""
Author: Nicholas Nguyen
File: cracker.py
Program to crack hashed passwords from shadow.txt using dictionary.txt
Worked with Will Xue
"""
import hashlib


def main():
    # Open up our files
    dictionary = open("dictionary.txt", "r")
    passwords = open("password,txt", "w")
    shadow = open("shadow", "r")

    shadowHashes = []

    # Create a list of just the hashes w/o the user#: and \n
    for line in shadow:
        shadowHashes.append(line[6:len(line)].strip())

    # for hash in shadowHashes:
    #     print(hash)
    #Go through the lines of the dictionary
    for line in dictionary:
        # Hash the line
        encodedLine = line[:len(line) - 1].encode()
        hashedLine = hashlib.md5(encodedLine).hexdigest()
        # print(hashedLine)
        #go through the hashes in shadowHashes
        for hashes in shadowHashes:
            # print(hashes)
            #Compare the hash we calculated to each of the shadowHashes
            if hashedLine == hashes:
                #If we get a match, print out line
                print(line)

    for i in range(100000):
        #try to hash it with every salt 0-99999
        #append i onto the string we'll hash
        for line in dictionary:
            encodedLine = line[:len(line) - 1].append(i).encode()
            hashedLine = hashlib.md5(encodedLine).hexdigest()
            for hashes in shadowHashes:
                if hashedLine == hashes:
                    print(line)

   # for hash in shadowHashes:
    #     print(hash)
    #Go through the lines of the dictionary
    for line in dictionary:
        # Hash the line
        encodedLine = line[:len(line) - 1].encode()
        hashedLine = hashlib.sha1(encodedLine).hexdigest()
        # print(hashedLine)
        #go through the hashes in shadowHashes
        for hashes in shadowHashes:
            # print(hashes)
            #Compare the hash we calculated to each of the shadowHashes
            if hashedLine == hashes:
                #If we get a match, print out line
                print(line)

    for i in range(100000):
        #try to hash it with every salt 0-99999
        #append i onto the string we'll hash
        for line in dictionary:
            encodedLine = line[:len(line) - 1].append(i).encode()
            hashedLine = hashlib.sha1(encodedLine).hexdigest()
            for hashes in shadowHashes:
                if hashedLine == hashes:
                    print(line)


if __name__ == "__main__":
    main()