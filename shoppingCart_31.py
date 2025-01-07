class ShoppingCart:

    def __init__(self):
        self.items = []
    
    def addittem(self, itemName,price,qty):
        product = {
        "itemName": itemName.lower(),
        "details": {"price": price, "qty": qty},
        "total" : price * qty
        }
        self.items.append(product)

    def removeItem(self,itemName):
        for i in self.items:
            if itemName.lower() == i["itemName"]:
                self.items.remove(i)
                return
        print(f"Item {itemName} not found in cart.")

    def totalPrice(self):
        total = 0
        for i in self.items:
            total += i["total"]
        print(total)






    def updateQty(self,itemName,qty):
        for i in self.items:
            if itemName.lower() == i["itemName"]:
                i["details"]["qty"] = qty
                i["total"] = i["details"]["price"] * qty
                return
        print(f"Item {itemName} not found in cart.")
            
    def printDetails(self):
        print(self.items)


cart = ShoppingCart()

cart.addittem("mango",55,1) # adds item (instance)
cart.addittem("orange",45,1) # adds item (instance)
cart.addittem("grape",40,1) # adds item (instance)
cart.addittem("banana",60,1) # adds item (instance)
cart.printDetails() # print Cart Items
cart.removeItem("kiwi") # kiwi found then remove
cart.removeItem("Banana") # banana found then remove
cart.printDetails() # print updated cart items
cart.updateQty("grape",2) # updates grape qty
cart.printDetails() # prints updated Cart Items
cart.totalPrice() # print total amount of cart


