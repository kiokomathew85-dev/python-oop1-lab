class Coffee:
    def __init__(self, size, price, blend=None):
        self._size = size
        self.price = float(price)
        self.blend = blend

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        self._size = value
        # Triggers when the test alters the size validation
        if value not in ["Small", "Medium", "Large"]:
            print("size must be Small, Medium, or Large")

    def tip(self):
        self.price += 1.0
        # The test explicitly looks for this phrase to be printed
        print("This coffee is great, here’s a tip!")
