class SList:
  def __init__(self):
    self.head = None
    
  def add_to_front(self, val):
    new_node = SLNode(val)
    current_head = self.head
    new_node.next = current_head
    self.head = new_node
    return self

  def print_values(self):
    runner = self.head
    while (runner != None):
      print(runner.value)
      runner = runner.next
    return self
  
  
  def add_to_back(self, val):
    new_node = SLNode(val)
    runner = self.head
    while (runner.next != None):
      runner = runner.next
    runner.next = new_node
    return self

  def remove_from_front(self):
    runner = self.head
    self.head = runner.next
    return self

  def remove_from_back(self):
    runner = self.head
    while (runner.next.next != None):
      runner = runner.next
    runner.next = None
    return self

  def remove_val(self, val):
    runner = self.head
    #if first element
    if runner.value == val:
      self.head = runner.next
    #if middle or last element
    while runner.next.value != val:
      runner = runner.next
    temp = runner.next.next
    runner.next = None
    runner.next = temp
    return self

  def insert_at(self, val, n):
    runner = self.head
    if n == 0:
      self.add_to_front(val)
    else: 
      index = 1
      while n > index:
        runner = runner.next
        index += 1
      temp = runner.next
      new_node = SLNode(val)
      runner.next = new_node
      new_node.next = temp
    return self
    
    

class SLNode:
  def __init__(self, val):
    self.value = val
    self.next = None
    


my_list = SList()
my_list.add_to_front("are").add_to_front("Linked lists").add_to_back("fun!").insert_at("pidr", 3).print_values()
