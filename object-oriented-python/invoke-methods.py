class Mobile:
    def __init__(self,price,brand):
        print (id(self))
        self.price = price
        self.brand = brand

    def display(self):
        print("Displaying details: \n price:" + str(self.price) + ", brand:" + str(self.brand))

    def purchase(self):
        self.display()
        print("Mobile purchased for Rs." + str(self.price) + ", brand:" + self.brand)


mobile = Mobile(20000, "Apple")
mobile.purchase()
