# Реверсування однозв'язного списку

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def reverse_linked_list(head):
    prev = None
    current = head
    while current is not None:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    head = prev
    return head

def print_list(head):
    current = head
    while current:
        print(current.value, end=' -> ')
        current = current.next
    print('None')

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)

print("Оригінальний список:")
print_list(head)

head = reverse_linked_list(head)

print("Реверсований список:")
print_list(head)

# Сортування однозв'язного списку

def merge_sort(head):
    if head is None or head.next is None:
        return head
    
    middle = get_middle(head)
    next_to_middle = middle.next
    middle.next = None
    
    left = merge_sort(head)
    right = merge_sort(next_to_middle)
    
    sorted_list = merge(left, right)
    return sorted_list

def get_middle(head):
    if head is None:
        return head
    
    slow = head
    fast = head
    
    while fast.next is not None and fast.next.next is not None:
        slow = slow.next
        fast = fast.next.next
    
    return slow

def merge(left, right):
    if left is None:
        return right
    if right is None:
        return left
    
    if left.value < right.value:
        result = left
        result.next = merge(left.next, right)
    else:
        result = right
        result.next = merge(left, right.next)
    
    return result

# Тестування сортування
head = Node(4)
head.next = Node(2)
head.next.next = Node(1)
head.next.next.next = Node(3)

print("Оригінальний список:")
print_list(head)

head = merge_sort(head)

print("Відсортований список:")
print_list(head)

# Об'єднання двох відсортованих однозв'язних списків

def merge_two_sorted_lists(l1, l2):
    dummy = Node(0)
    tail = dummy
    
    while l1 is not None and l2 is not None:
        if l1.value < l2.value:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next
    
    if l1 is not None:
        tail.next = l1
    if l2 is not None:
        tail.next = l2
    
    return dummy.next

# Тестування об'єднання двох відсортованих списків
head1 = Node(1)
head1.next = Node(3)
head1.next.next = Node(5)

head2 = Node(2)
head2.next = Node(4)
head2.next.next = Node(6)

print("Список 1:")
print_list(head1)
print("Список 2:")
print_list(head2)

merged_head = merge_two_sorted_lists(head1, head2)

print("Об'єднаний список:")
print_list(merged_head)