class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" ")
            current_node = current_node.next
        print("\n")
    
    def reverse(self):
        prev = None
        current = self.head
        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def merge_sort(self):
        if self.head is None or self.head.next is None:
            return self.head
        
        middle = self.get_middle(self.head)
        next_to_middle = middle.next
        middle.next = None
        
        left = self.merge_sort_recursive(self.head)
        right = self.merge_sort_recursive(next_to_middle)
        
        sorted_list = self.sorted_merge(left, right)
        self.head = sorted_list
    
    def merge_sort_recursive(self, h):
        if h is None or h.next is None:
            return h
        
        middle = self.get_middle(h)
        next_to_middle = middle.next
        middle.next = None
        
        left = self.merge_sort_recursive(h)
        right = self.merge_sort_recursive(next_to_middle)
        
        sorted_list = self.sorted_merge(left, right)
        return sorted_list
    
    def get_middle(self, head):
        if head is None:
            return head
        
        slow = head
        fast = head
        
        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next
        
        return slow
    
    def sorted_merge(self, a, b):
        if a is None:
            return b
        if b is None:
            return a
        
        if a.data <= b.data:
            result = a
            result.next = self.sorted_merge(a.next, b)
        else:
            result = b
            result.next = self.sorted_merge(a, b.next)
        
        return result
    
def merge_sorted_lists(list1, list2):
    dummy = Node()
    tail = dummy

    current1 = list1.head
    current2 = list2.head

    while current1 is not None and current2 is not None:
        if current1.data <= current2.data:
            tail.next = current1
            current1 = current1.next
        else:
            tail.next = current2
            current2 = current2.next
        tail = tail.next

    if current1 is not None:
        tail.next = current1
    else:
        tail.next = current2

    merged_list = LinkedList()
    merged_list.head = dummy.next
    return merged_list
    

# Приклад використання:
linked_list = LinkedList()
linked_list.append(3)
linked_list.append(9)
linked_list.append(4)
linked_list.prepend(8)
linked_list.prepend(1)

linked_list_2 = LinkedList()
linked_list_2.append(6)
linked_list_2.append(2)
linked_list_2.append(7)
linked_list_2.prepend(5)
linked_list_2.prepend(10)

print("Зв'язний список 1:")
linked_list.print_list()

print("Зв'язний список 2:")
linked_list_2.print_list()

print("Списки після реверсування:")
print("Список 1:")
linked_list.reverse()
linked_list.print_list()
print("Список 2:")
linked_list_2.reverse()
linked_list_2.print_list()

print("Сортування злиттям:")
print("Список 1:")
linked_list.merge_sort()
linked_list.print_list()
print("Список 2:")
linked_list_2.merge_sort()
linked_list_2.print_list()

print("Об'єднаний відсортований список:")
merged_list = merge_sorted_lists(linked_list,linked_list_2)
merged_list.print_list()


