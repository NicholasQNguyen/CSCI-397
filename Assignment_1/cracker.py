"""
Program to crack hashed passwords from shadow.txt using dictionary.txt
"""
import hashlib

def main():
    dictionary = open("dictionary.txt", "r")
    shadow = open("shadow", "r")

    shadowHashes = []

    # Create a list of just the hashes w/o the user#: and \n
    for line in shadow:
        shadowHashes.append(line[6:].strip())

    for hash in shadowHashes:
        print(hash)

    #Go through the lines of the dictionary
        #hash the line
            #go through the lines of shadowHashes
                #Compare the hash we calculated to each of the shadowHashes
                    #If we get a match, print out line

    #https://www.geeksforgeeks.org/md5-hash-python/
    ## print(hashlib.md5(b"Nicholas").digest())
    for i in range(100000):
        #try to hash it with every salt 1-99999
        #append i onto the string we'll hash
        None

if __name__ == "__main__":
    main()