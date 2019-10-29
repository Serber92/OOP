class User:
  def __init__(self, name, email):
    self.name = name
    self.email = email
    self.account_balance = 0

  def make_deposit(self, amount):
    self.account_balance += amount
    return self

  def make_withdrawal(self, amount):
    self.account_balance -= amount
    return self

  def display_user_balance(self):
    print(self.name, ": Balance $" + str(self.account_balance))
    return self
    
  def transfer_money(self, other_user, amount):
    self.make_withdrawal(amount)
    other_user.make_deposit(amount)
    return self

pidr = User('Pidr', 'pidr@com')
gnida = User('Gnida', 'gnida@com')

pidr.make_deposit(100).display_user_balance().transfer_money(gnida, 50)
gnida.display_user_balance()
pidr.display_user_balance()
