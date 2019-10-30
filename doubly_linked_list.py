class DList:
  def __init__(self):
    self.head = None

  def add_to_front(self, node):
    if self.head == None:
      self.head = node
    else:
      current_head = self.head
      node.next = current_head
      node.next.previous = node
      self.head = node
    return self

  def add_to_end(self, node):
    runner = self.head
    while runner.next != None:
      runner = runner.next
    runner.next = node
    node.previous = runner
    return self

  def remove_at_end(self):
    runner = self.head
    while runner.next != None:
      runner = runner.next
    print("*****Node:", runner.value, "deleted*****")
    runner = runner.previous
    runner.next = None
    return self

  def remove_at_index(self, index):
    runner_index = 0
    runner = self.head
    while runner_index < index:
      runner = runner.next
      runner_index += 1
    runner.previous.next = runner.next
    runner.next.previous = runner.previous
    return self
  
  def add_at_index(self, index, new_node):
    runner_index = 0
    runner = self.head
    while runner_index < index:
      runner = runner.next
      runner_index += 1
    runner.previous.next = new_node
    new_node.next = runner
    runner.previous = new_node
    new_node.previous = runner.previous
    return self

  def print_list(self):
    runner = self.head
    index = 0
    while runner != None:
      print("Node at index", index, ":", runner.value)
      runner = runner.next
      index += 1
    return self
    

class Node:
  def __init__(self, value):
    self.value = value
    self.previous = None
    self.next = None


list = DList()
node0 = Node("first")
node1 = Node("second")
node2 = Node("third")
nodeEnd = Node("END")
nodeAdd = Node("Added in middle")

list.add_to_front(node2).add_to_front(node1).add_to_front(node0).print_list()
print("___________________")
print(">>>>Adding node to the end<<<<<")
list.add_to_end(nodeEnd).print_list()
print("___________________")
list.remove_at_end().print_list()
print("___________________")
print(">>>>>Removing at index 1<<<<<<")
list.remove_at_index(1).print_list()
print("___________________")
print(">>>>>Adding node at index 1<<<<<<")
list.add_at_index(1, nodeAdd).print_list()
list.remove_at_end().remove_at_end().remove_at_end().print_list()
