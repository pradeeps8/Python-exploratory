### Check Permutation: Given two strings, write a method to decide if one is a permutation of the other. ###
def main():
    str1 = input("Enter the 1st string :")
    str2 = input("Enter the 2nd string :")

    print(checkForPermutability(str1, str2))

def checkForPermutability(str1, str2):
    sorted_str1 = sorted(str1)
    sorted_str2 = sorted(str2)
    if sorted_str1 == sorted_str2:
        return True
    else:
        return False

if __name__ == '__main__':
    main()

