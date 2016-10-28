class MemberProfile:
    def __init__(self, name, address, phone_numbers, brand_photo, shop_id):
        self.name = name
        self.address = address
        self.phone_numbers = phone_numbers
        self.brand_photo = brand_photo
        self.shop_id = shop_id


class FoodHelper:
    def __init__(self, title, price, description, food_photo):
        self.title = title
        self.price = price
        self.description = description
        self.food_photo = food_photo


class SimplifiedFood:
    def __init__(self, title, price, amount):
        self.title = title
        self.price = price
        self.amount = amount

    def __str__(self):
        return self.title
