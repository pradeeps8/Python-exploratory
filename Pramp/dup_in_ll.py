import random

class node:
    def __init__(self, data):
        self.val = data
        self.next = None

class linkedlist:
    def __init__(self):
        self.head = None

    def insert(self, data):
        newnode = node(data)
        if self.head == None:
            self.head = newnode
            return

        cur = self.head
        while cur.next != None:
            cur = cur.next

        cur.next = newnode
        return

    def findDuplicates(self):
        dups = set()
        ht = dict()

        if self.head == None:
            return dups

        cur = self.head
        ht[cur.val] = 1
        while cur.next != None:
            nextVal = cur.next.val
            if nextVal in ht:
                dups.add(nextVal)
            else:
                ht[nextVal] = 1
            cur = cur.next

        return dups

    def printlinkedlist(self):
        if self.head == None:
            print("Empty Linked List")
            return
        
        printstr = ""
        cur = self.head
        
        while cur.next != None:
            printstr = printstr + str(cur.val) + "->"
            cur = cur.next
        
        printstr = printstr + str(cur.val) + "->None"
        
        print(printstr)


def main():
    
    n = (int)(input("Enter the number of nodes: "))
    
    ll = linkedlist()
    for i in range(n):
        ll.insert(random.randint(0, 10))
    """
    ll.insert(10)
    ll.insert(3)
    ll.insert(2)
    ll.insert(29)
    ll.insert(300)
    ll.insert(3)
    ll.insert(3)
    ll.insert(-10)
    ll.insert(10)
    """
    ll.printlinkedlist()
    print('Duplicates are ' + str(ll.findDuplicates()))

if __name__ == '__main__':
    main()
