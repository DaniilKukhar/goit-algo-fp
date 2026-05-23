class Node:

    def __init__(self, data):

        self.data = data

        self.next = None

class LinkedList:

    def __init__(self):

        self.head = None

    # Додавання елемента в кінець списку

    def append(self, data):

        new_node = Node(data)

        if not self.head:

            self.head = new_node

            return

        current = self.head

        while current.next:

            current = current.next

        current.next = new_node

    # Виведення списку

    def print_list(self):

        current = self.head

        while current:

            print(current.data, end=" -> ")

            current = current.next

        print("None")

    # Реверсування списку

    def reverse(self):

        prev = None

        current = self.head

        while current:

            next_node = current.next

            current.next = prev

            prev = current

            current = next_node

        self.head = prev

    # Сортування злиттям

    def merge_sort(self, head):

        if head is None or head.next is None:

            return head

        middle = self.get_middle(head)

        next_to_middle = middle.next

        middle.next = None

        left = self.merge_sort(head)

        right = self.merge_sort(next_to_middle)

        sorted_list = self.sorted_merge(left, right)

        return sorted_list

    # Пошук середини списку

    def get_middle(self, head):

        if head is None:

            return head

        slow = head

        fast = head

        while fast.next and fast.next.next:

            slow = slow.next

            fast = fast.next.next

        return slow

    # Об'єднання двох відсортованих списків

    def sorted_merge(self, left, right):

        if left is None:

            return right

        if right is None:

            return left

        if left.data <= right.data:

            result = left

            result.next = self.sorted_merge(left.next, right)

        else:

            result = right

            result.next = self.sorted_merge(left, right.next)

        return result

    # Запуск сортування

    def sort(self):

        self.head = self.merge_sort(self.head)

    # Об'єднання двох відсортованих списків

    @staticmethod

    def merge_two_sorted_lists(list1, list2):

        merged_list = LinkedList()

        merged_list.head = merged_list.sorted_merge(

            list1.head,

            list2.head

        )

        return merged_list

def main():

    print("Початковий список:")

    linked_list = LinkedList()

    linked_list.append(5)

    linked_list.append(1)

    linked_list.append(3)

    linked_list.append(2)

    linked_list.append(4)

    linked_list.print_list()

    # Реверсування

    print("\nРеверсований список:")

    linked_list.reverse()

    linked_list.print_list()

    # Сортування

    print("\nВідсортований список:")

    linked_list.sort()

    linked_list.print_list()

    # Створення двох відсортованих списків

    list1 = LinkedList()

    list2 = LinkedList()

    list1.append(1)

    list1.append(3)

    list1.append(5)

    list2.append(2)

    list2.append(4)

    list2.append(6)

    # Об'єднання списків

    merged = LinkedList.merge_two_sorted_lists(list1, list2)

    print("\nОб'єднаний відсортований список:")

    merged.print_list()

if __name__ == "__main__":

    main()