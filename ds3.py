

''' 
URLify: Write a method to replace all spaces in a string with '%20'.
You may assume that the string has sufficient space at the end to hold the additional characters, and that you are given the "true" length of the string. 
(Note: if implementing in Java, please use a character array so that you can perform this operation in place.) 
EXAMPLE 
Input:  "Mr John Smith    ", 13 
Output: "Mr%20John%20Smith" 
'''

def main():
    str1 = input("Enter the string with additional space at the end:")
    leng = int(input("Enter the actual lenght of the string: "))
    print(urlify(str1, leng))

def urlify(str1, leng):
    str2 = bytearray(str1, 'utf-8')
    #str2 = list(str1)
    actlen = len(str1)
    i = leng - 1
    j = actlen - 1
    while (i >= 0) :
        if(str1[i] == ' '):
            str2[j] = '0'
            str2[j-1] = '2'
            str2[j-2] = '%'
            j = j - 2
        else:
            str2[j] = str1[i]
        j = j - 1
        i = i - 1
    return str(str2)
##    return ''.join(str2)

if __name__ == '__main__':
    main()

