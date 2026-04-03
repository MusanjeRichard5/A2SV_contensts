class Node:
    def __init__ (self,data):
        self.data = data
        self.next = None

def insertNodeAtTail(head, data):
    new_node = Node(data)
    if head is None:
        return new_node
    #store head reference 
    temp = head
    
    #traverse till end of head
    while temp.next is not None:
        temp = temp.next
    #once at end let the temp to point to new node
    temp.next = new_node
    return head
    
    
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    llist_count = int(input())

    llist = SinglyLinkedList()

    for i in range(llist_count):
        llist_item = int(input())
        llist_head = insertNodeAtTail(llist.head, llist_item)
        llist.head = llist_head

    print_singly_linked_list(llist.head, '\n', fptr)
    fptr.write('\n')

    fptr.close()
