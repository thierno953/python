class Phone:

    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def call(self, phone_number):
        print(f"{self.brand} is calling {phone_number}")

    def __str__(self) -> str:
        return f"Brand = {self.brand}\nPrice ={self.price}"


iphone = Phone("Iphone 7+", 300)
samsung = Phone("Samsung S20", 1300)

print(iphone)
print(samsung)

iphone.call("999")
samsung.call("1000")

