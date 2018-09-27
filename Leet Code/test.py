
import sys

###Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures? 

def main():
    str = input("Enter the String ")
    print(str)
    print(isUnique(str))

def isUnique(str):
    hs = dict()
    for i in str:
        if i in hs:
            print(i)
            return False
        else:
            hs[i] = 1
    return True

def isUnique2(str):
    sort = sorted(str)
    for i in range(1, len(sort)):
        if(sort[i] == sort[i-1]):
            print(sort[i])
            return False
    return True

if __name__ == '__main__':
    main()

