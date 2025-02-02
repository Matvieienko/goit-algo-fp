class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def insert_after(self, prev_node: Node, data):
        if prev_node is None:
            print("Попереднього вузла не існує.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key: int):
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            cur = None
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if cur is None:
            return
        prev.next = cur.next
        cur = None

    def search_element(self, data: int) -> Node | None:
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    # Реверсує однозв'язний список, змінюючи посилання між вузлами
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    # Сортує однозв'язний список методом вставки
    def sort(self):
        if not self.head or not self.head.next:
            return
        sorted_list = None
        current = self.head
        while current:
            next_node = current.next
            sorted_list = self.sorted_insert(sorted_list, current)
            current = next_node
        self.head = sorted_list

    # Вставляє вузол у відповідне місце в уже відсортованому списку
    def sorted_insert(self, head: Node, new_node: Node):
        if not head or new_node.data < head.data:
            new_node.next = head
            return new_node
        current = head
        while current.next and current.next.data < new_node.data:
            current = current.next
        new_node.next = current.next
        current.next = new_node
        return head

    # Об'єднує два відсортовані однозв'язні списки в один відсортований список
    @staticmethod
    def merge_sorted_lists(list1, list2):
        dummy = Node()
        tail = dummy
        while list1 and list2:
            if list1.data < list2.data:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        tail.next = list1 if list1 else list2
        return dummy.next


# Приклад використання
llist1 = LinkedList()
llist1.insert_at_end(1)
llist1.insert_at_end(3)
llist1.insert_at_end(5)

llist2 = LinkedList()
llist2.insert_at_end(2)
llist2.insert_at_end(4)
llist2.insert_at_end(6)

print("Перший список:")
llist1.print_list()
print("Другий список:")
llist2.print_list()

# Об'єднання двох списків
merged_list_head = LinkedList.merge_sorted_lists(llist1.head, llist2.head)
merged_list = LinkedList()
merged_list.head = merged_list_head
print("Об'єднаний список:")
merged_list.print_list()

# Реверсування списку
print("\nРеверсування об'єднаного списку:")
merged_list.reverse()
merged_list.print_list()

# Сортування списку
print("\nСортування реверсованого списку:")
merged_list.sort()
merged_list.print_list()