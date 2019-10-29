class Store:
  def __init__(self, name, products=[]):
    self.name = name
    self.products = products
  
  def add_product(self, new_product):
    self.products.append(new_product)
    return self

  def sell_product(self, id):
    print("Product is sold. Info:")
    self.products[id].print_info()
    del self.products[id]
    return self

  def inflation(self, percent_increase):
    for product in self.products:
      product.update_price(percent_increase, True)
      return self
  
  def set_clearance(self, percent_discount):
    for product in self.products:
      product.update_price(percent_discount, False)
      return self





