class Item:
    

    def __init__(self, price, weight):
        self.price = price
        self.weight = weight

i = Item(10, 20)

print(f"Price: {i.price}, Weight: {i.weight}")
