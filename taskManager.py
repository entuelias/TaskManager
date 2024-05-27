class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def iterate(self):
        iterator = self.head
        while iterator:
            print(str(iterator.value) + " ")
            iterator = iterator.next

class TaskManager:
    def __init__(self):
        self.task_list = LinkedList()

    def add_task(self, task_name):
        self.task_list.append(task_name)

    def mark_completed(self, task_name):
        iterator = self.task_list.head
        while iterator:
            if iterator.value == task_name:
                iterator.value += " (completed)"
                break
            iterator = iterator.next

    def view_tasks(self):
        self.task_list.iterate()


task_manager = TaskManager()
task_manager.add_task("Task 1")
task_manager.add_task("Task 2")
task_manager.add_task("Task 3")
task_manager.view_tasks()
task_manager.mark_completed("Task 1")
task_manager.view_tasks()