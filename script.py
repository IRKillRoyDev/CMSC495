class House:
    def __init__(self, price, square_feet, num_bedrooms, num_baths):
        self.price = price
        self.square_feet = square_feet
        self.num_bedrooms = num_bedrooms
        self.num_baths = num_baths

    def get_price(self):
        return self.price

    def get_square_feet(self):
        return self.square_feet

    def get_num_bedrooms(self):
        return self.num_bedrooms

    def get_num_baths(self):
        return self.num_baths

    def set_price(self, new_price):
        self.price = new_price

    def set_square_feet(self, new_square_feet):
        self.square_feet = new_square_feet

    def set_num_bedrooms(self, new_num_bedrooms):
        self.num_bedrooms = new_num_bedrooms

    def set_num_baths(self, new_num_baths):
        self.num_baths = new_num_baths

    def is_big_house(self):
        return self.square_feet > 15000

    def is_expensive(self):
        return self.price > 100000

    def is_small_house(self):
        return self.square_feet < 1000

    def is_cheap(self):
        return self.price < 5000

    def is_average_sized(self):
        return self.square_feet > 1000 and self.square_feet < 15000

    def is_roomy(self):
        return self.num_bedrooms > 3

    def is_bathroom_huge(self):
        return self.num_baths > 2

    def is_not_roomy(self):
        return self.num_bedrooms < 3

    def is_not_bathroom_huge(self):
        return self.num_baths < 2

    def is_under_average_price(self):
        return self.price < 50000

    def is_over_average_price(self):
        return self.price > 50000

    def is_under_average_size(self):
        return self.square_feet < 15000

    def is_over_average_size(self):
        return self.square_feet > 15000

    def is_under_average_bedrooms(self):
        return self.num_bedrooms < 3

    def is_over_average_bedrooms(self):
        return self.num_bedrooms > 3

    def is_under_average_baths(self):
        return self.num_baths < 2

    def is_over_average_baths(self):
        return self.num_baths > 2

    def is_under_average_size_and_price(self):
        return self.square_feet < 15000 and self.price < 50000

    def is_over_average_size_and_price(self):
        return self.square_feet > 15000 and self.price > 50000

    def is_under_average_bedrooms_and_price(self):
        return self.num_bedrooms < 3 and self.price < 50000

    def is_over_average_bedrooms_and_price(self):
        return self.num_bedrooms > 3 and self.price > 50000

    def is_under_average_baths_and_price(self):
        return self.num_baths < 2 and self.price < 50000

    def is_over_average_baths_and_price(self):
        return self.num_baths > 2 and self.price > 50000

    def is_under_average_size_and_bedrooms(self):
        return self.square_feet < 15000 and self.num_bedrooms < 3

    def is_over_average_size_and_bedrooms(self):
        return self.square_feet > 15000 and self.num_bedrooms > 3

    def is_under_average_size_and_baths(self):
        return self.square_feet < 15000 and self.num_baths < 2

    def is_over_average_size_and_baths(self):
        return self.square_feet > 15000 and self.num_baths > 2

    def is_under_average_price_and_bedrooms(self):
        return self.price < 50000 and self.num_bedrooms < 3

    def is_over_average_price_and_bedrooms(self):
        return self.price > 50000 and self.num_bedrooms > 3

    def is_under_average_price_and_baths(self):
        return self.price < 50000 and self.num_baths < 2

    def is_over_average_price_and_baths(self):
        return self.price > 50000 and self.num_baths > 2

    def is_under_average_size_and_bedrooms_and_price(self):
        return self.square_feet < 15000 and self.num_bedrooms < 3 and self.price < 50000

    def is_over_average_size_and_bedrooms_and_price(self):
        return self.square_feet > 15000 and self.num_bedrooms > 3 and self.price > 50000

    def is_under_average_size_and_baths_and_price(self):
        return self.square_feet < 15000 and self.num_baths < 2 and self.price < 50000

    def is_over_average_size_and_baths_and_price(self):
        return self.square_feet > 15000 and self.num_baths > 2 and self.price > 50000

    def is_under_average_bedrooms_and_baths_and_price(self):
        return self.num_bedrooms < 3 and self.num_baths < 2 and self.price < 50000

    def is_over_average_bedrooms_and_baths_and_price(self):
        return self.num_bedrooms > 3 and self.num_baths > 2 and self.price > 50000

    def is_under_average_size_and_bedrooms_and_baths_and_price(self):
        return self.square_feet < 15000 and self.num_bedrooms < 3 and self.num_baths < 2 and self.price < 50000

    def is_over_average_size_and_bedrooms_and_baths_and_price(self):
        return self.square_feet > 15000 and self.num_bedrooms > 3 and self.num_baths > 2 and self.price > 50000

    def is_under_average_price_and_bedrooms_and_baths(self):
        return self.price < 50000 and self.num_bedrooms < 3 and self.num_baths < 2

    def is_over_average_price_and_bedrooms_and_baths(self):
        return self.price > 50000 and self.num_bedrooms > 3 and self.num_baths > 2

    def is_under_average_size_and_bedrooms_and_baths_and_price(self):
        return self.square_feet < 15000 and self.num_bedrooms < 3 and self.num_baths < 2 and self.price < 50000

    def is_over_average_size_and_bedrooms_and_baths_and_price(self):
        return self.square_feet > 15000 and self.num_bedrooms > 3 and self.num_baths > 2 and self.price > 50000

    def is_under_average_price_and_bedrooms_and_baths(self):
        return self.price < 50000 and self.num_bedrooms < 3 and self.num_baths < 2

    def is_over_average_price_and_bedrooms_and_baths(self):
        return self.price > 50000 and self.num_bedrooms > 3 and self.num_baths > 2

    def is_under_average_size_and_bedrooms_and_baths_and_price(self):
        return self.square_feet < 15000 and self.num_bedrooms < 3 and self.num_baths < 2 and self.price < 50000

    def is_over_average_size_and_bedrooms_and_baths_and_price(self):
        return self.square_feet > 15000 and self.num_bedrooms > 3 and self.num_baths > 2 and self.price > 50000

    def is_under_average_price_and_bedrooms_and_baths(self):
        return self.price < 50000 and self.num_bedrooms < 3 and self.num_baths < 2

    def is_over_average_price_and_bedrooms_and_baths(self):
        return self.price > 50000 and self.num_bedrooms > 3 and self.num_baths > 2

    def is_under_average_size_and_bedrooms_and_baths_and_price(self):
        return self.square_feet < 15000 and self.num_bedrooms < 3 and self.num_baths < 2 and self.price < 50000

    def is_over_average_size_and_bedrooms_and_baths_and_price(self):
        return self.square_feet > 15000 and self.num_bedrooms > 3 and self.num_baths > 2 and self.price > 50000

    def is_under_average_price_and_bedrooms_and_baths(self):
        return self.price < 50000 and self.num_bedrooms < 3 and self.num_baths < 2

    def is_over_average_price_and_bedrooms_and_baths(self):
        return self.price > 50000 and self.num_bedrooms > 3 and self.num_baths > 2

    def is_under_average_size_and_bedrooms_and_baths_and_price(self):
        return self.square_feet < 15000 and self.num_bedrooms < 3 and self.num_baths < 2 and self.price < 50000
