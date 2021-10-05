"""
Program to crack hashed passwords from shadow.txt using dictionary.txt
"""
import hashlib

def md5Hash(plainPassword, listOfHashes):
    # print(plainPassword)
    hashedPassword = hashlib.md5(plainPassword.encode()).digest()
    print(hashedPassword)
    for hash in listOfHashes:
        #slice so that we get rid of the user1:
        hash = hash[6:]



def sha1Hash(plainPassword, listOfHashes):
        hashedPassword = hashlib.sha1(plainPassword.encode()).digest()
        for hash in listOfHashes:
            hash = hash[6:]
            if hashedPassword == hash:
                return hash

def main():
    dictionary = open("dictionary.txt", "r")
    hashes = open("shadow", "r")

    # Try to hash it without salt
    for item in dictionary:
        md5H = md5Hash(item, hashes)

    # for item in dictionary:
    #     sha1H = sha1Hash(item, hashes)
    
    # print(md5H)
    # print(sha1H)
            
    #https://www.geeksforgeeks.org/md5-hash-python/
    ## print(hashlib.md5(b"Nicholas").digest())
    for i in range(100000):
        #try to hash it with every salt 1-99999
        #append i onto the string we'll hash
        None

if __name__ == "__main__":
    main()