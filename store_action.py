import store
import products

shinok = store.Store(name="Shinok")
kolbasa = products.Product(name="kolbasa", price=50, category="meat")
hleb = products.Product(name="hleb", price=10, category="hleb")
morkva = products.Product(name="morkva", price=5, category="vegies")

shinok.add_product(kolbasa).add_product(hleb).add_product(morkva)

shinok.sell_product(1).set_clearance(50).sell_product(0)
