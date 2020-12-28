class ListNode:
    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
        head = None
        result = None
        remainder = 0

        while l1 is not None and l2 is not None:
            res_val = l1.val + l2.val + remainder
            remainder = res_val // 10
            val = res_val % 10
            res = ListNode(val)
            if head is None:
                head = res
                result = res
            else:
                result.next = res
                result = res
            l1 = l1.next
            l2 = l2.next

        rem_nodes = l1 if l1 else l2

        while rem_nodes is not None:
            res_val = rem_nodes.val + remainder
            remainder = res_val // 10
            val = res_val % 10
            res = ListNode(val)
            if head is None:
                head = res
                result = res
            else:
                result.next = res
                result = res
            rem_nodes = rem_nodes.next

        if remainder:
            res = ListNode(remainder)
            result.next = res

        return head

def main():
    num1 = [1, 9, 1, 3]
    num2 = [9, 9, 9]

    num_node1 = None
    node1 = None
    for digit in num1[::-1]:
        node = ListNode(digit)
        if num_node1 is None:
            num_node1 = node
            node1 = node
        else:
            node1.next = node
            node1 = node

    num_node2 = None
    node2 = None
    for digit in num2[::-1]:
        node = ListNode(digit)
        if num_node2 is None:
            num_node2 = node
            node2 = node
        else:
            node2.next = node
            node2 = node

    result = addTwoNumbers(num_node1, num_node2)

    res = []
    while result is not None:
        res.append(result.val)
        result = result.next

    print("num 1 " + str(num1))
    print("num 2 " + str(num2))
    print("result " + str(res[::-1]))


if __name__ == '__main__':
    main()
