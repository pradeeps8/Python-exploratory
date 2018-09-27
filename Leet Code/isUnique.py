import timeit

###Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures? 

def main():
	str = r'SAFGHJKL:POIUYTREWQZXCVBNM<>?_)(*&^%$#@!~asdfghjklqwertyiuopmnbvcxz,./;][1234567890-=+'
	#str = None
	if str is None:
		str = input("Enter the String ")
	print(str)
	print("Using Dict ", isUnique(str))
	print("Using Sort ", isUnique2(str))
	
	def wrapper(func, *args, **kwargs):
		def wrapped():
			return func(*args, **kwargs)
		return wrapped
	uniq1 = wrapper(isUnique, str)
	uniq2 = wrapper(isUnique2, str)
	print("Time using Dict: ", timeit.timeit(uniq1, number=100000))
	print("Time using sort: ", timeit.timeit(uniq2, number=100000))
	
def isUnique(str):
    hs = dict()
    for i in str:
        if i in hs:
            #print(i)
            return False
        else:
            hs[i] = 1
    return True

def isUnique2(str):
    sort = sorted(str)
    for i in range(1, len(sort)):
        if(sort[i] == sort[i-1]):
            #print(sort[i])
            return False
    return True

if __name__ == '__main__':
    main()

