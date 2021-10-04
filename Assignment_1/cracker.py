"""
Program to crack hashed passwords from shadow.txt using dictionary.txt
"""
import hashlib

def main():
    #Try to hash it without salt
    #https://www.geeksforgeeks.org/md5-hash-python/
    print(hashlib.md5(b"Nicholas").digest())
    for i in range(100000):
        #try to hash it with every salt 1-99999
        #append i onto the string we'll hash
        None

if __name__ == "__main__":
    main()