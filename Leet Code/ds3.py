

''' 
URLify: Write a method to replace all spaces in a string with '%20'.
You may assume that the string has sufficient space at the end to hold the additional characters, and that you are given the "true" length of the string. 
(Note: if implementing in Java, please use a character array so that you can perform this operation in place.) 
EXAMPLE 
Input:  "Mr John Smith    ", 13 
Output: "Mr%20John%20Smith" 
'''

import timeit

def main():
    str1 = "I AM OK WITH ANY THING AT ALL WITH THIS FROM NOW ON                        "
    leng = 51
    #str1 = None
    #leng = None
    if str1 is None:
        str1 = input("Enter the string with additional space at the end:")
        leng = int(input("Enter the actual lenght of the string: "))
    
    print("List res: ", urlify(str1, leng))
    print("ByteArray res: ", urlify2(str1, leng))
    print("Time for list")

    def wrapper(func, *args, **kwargs):
        def wrapped():
            return func(*args, **kwargs)
        return wrapped
    
    url1 = wrapper(urlify, str1, leng)
    url2 = wrapper(urlify2, str1, leng)

    print(timeit.timeit(url1, number=1000000))
    print("Time for bytearray")
    print(timeit.timeit(url2, number=1000000))
    

## bytearray vs list
## Using list
def urlify(str1, leng):
    str2 = list(str1)
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
    return ''.join(str2)

## Using bytearray
def urlify2(str1, leng):
    str2 = bytearray(str1, 'utf-8')
    #str2 = list(str1)
    actlen = len(str1)
    i = leng - 1
    j = actlen - 1
    while (i >= 0) :
        if(str1[i] == ' '):
            str2[j] = ord('0')
            str2[j-1] = ord('2')
            str2[j-2] = ord('%')
            j = j - 2
        else:
            str2[j] = ord(str1[i])
        j = j - 1
        i = i - 1
    return str2.decode()

if __name__ == '__main__':
    main()

