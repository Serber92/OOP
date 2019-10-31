

class Animals:
  def __init__(self, kind, name):
    self.kind = kind
    self.name = name
    self.happy = True
  def display_info(self):
    print(self.kind, self.name, "Happy?", self.happy)
    return self

class Lion(Animals):
  def __init__(self, kind, name):
    super().__init__(kind, name)
    self.roar = "ti pidr"

class Tiger(Animals):
  def __init__(self, kind, name):
    super().__init__(kind, name)
    self.roar = "ti gnida"
    self.happy = False


class Zoo:
  def __init__(self, zoo_name):
    self.animals = []
    self.name = zoo_name

  def add_lion(self, name):
    self.animals.append(Lion("lion", name))
    return self

  def add_tiger(self, name):
    self.animals.append(Tiger("tiger", name))
    return self

  def print_all_info(self):
    print("-"*80, "\n", self.name)
    for animal in self.animals:
      animal.display_info()


priton = Zoo("priton")
priton.add_lion("Valanok").add_tiger("dibil").print_all_info()