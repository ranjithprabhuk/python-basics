class Mobile:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price
        print("Id of self in constructor", id(self))

mob1=Mobile("Apple", 20000)
mob2=Mobile("Samsung", 10000)

print(mob1.brand)
print(mob1.price)
print(mob2.brand)
print(mob2.price)