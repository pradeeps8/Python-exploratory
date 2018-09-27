"""
This is a naive solution which is insertion sort
O(n*k) time complexity and O(1) space complexity solution.
Worst case is O(n*n) when k >= n
"""
import heapq

def kmessedArraysort(arr, k):
    length = len(arr)
    for i in range(length):
        j = i + 1
        kj = i + k
        while (j < length) and (j <= kj):
            if (arr[i] > arr[j]):
                tmp = arr[i]
                arr[i] = arr[j]
                arr[j] = tmp
            j = j + 1

    return arr
"""
Priority Queue solution/ min-heap.

Time complexity = O(n*log(k))
log(k) to heapify everytime we push an element 
Worst case = O(n*log(n)) when k >= n
Space complexity = O(log(k))

"""
def kmessedArraysort2(arr, k):
    length = len(arr)
    k = min(k, length-1) 
    h = arr[0:k+1]
    heapq.heapify(h)
    
    for i in range(length-k-1):
        ## heapreplace first pops the first element and then pushes the given element 
        arr[i] = heapq.heapreplace(h, arr[i+k+1])
    #print(h)
    ### Last K+1 elements to be placed in the array correctly.
    i = length-k-1
    while i < length:
        arr[i] = heapq.heappop(h)
        i = i+1
    
    return arr


def main():
    k = (int)(input("Please enter the value of k within 1 to 20:"))
    
    arr = [1,3,5,2,6,4,9,10,7,8]
    print(k)
    print(arr)
    print(kmessedArraysort2(arr, k))

if __name__ == '__main__':
    main()

