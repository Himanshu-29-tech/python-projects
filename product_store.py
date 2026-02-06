# ==========================================
# Product Store (Python OOP)
# ==========================================
# Features:
# 1. Create products with name and price
# 2. Track total number of products created
# 3. Calculate discount on product price
# ==========================================


class Product:
    """Represents a product in an online store"""

    # class variable to track total products
    count = 0

    def __init__(self, name, price):
        """Constructor to initialize product details"""
        self.name = name
        self.price = price
        Product.count += 1

    def get_info(self):
        """Instance method to display product information"""
        print(f"Price of {self.name} is Rs.{self.price}")

    @classmethod
    def get_count(cls):
        """Class method to show total products"""
        print(f"Total products in store = {cls.count}")

    @staticmethod
    def calc_discount(price, discount):
        """Static method to calculate discounted price"""
        discounted_price = price - (price * discount / 100)
        print(f"Discounted price = Rs.{discounted_price}")


# ==========================
# Creating product objects
# ==========================
p1 = Product("Phone", 10_000)
p2 = Product("Laptop", 50_000)
p3 = Product("Pen", 10)

# ==========================
# Using methods
# ==========================
p1.get_info()
p2.get_info()
p3.get_info()

Product.get_count()

p1.calc_discount(10_000, 12)
