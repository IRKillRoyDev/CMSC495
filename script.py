class House:
    """_summary_string() returns a string that summarizes the information about the house.
    """
    def __init__(self, price, square_feet, num_bedrooms, num_baths):
        self.price = price
        self.square_feet = square_feet
        self.num_bedrooms = num_bedrooms
        self.num_baths = num_baths

    def get_price(self):
        """_summary_string() returns a string that summarizes the information about the house."""
        return self.price

    def get_square_feet(self):
        """_summary_string() returns a string that summarizes the information about the house."""
        return self.square_feet

    def get_num_bedrooms(self):
        """_summary_string() returns a string that summarizes the information about the house."""
        return self.num_bedrooms

    def get_num_baths(self):
        """_summary_string() returns a string that summarizes the information about the house."""
        return self.num_baths

    def set_price(self, new_price):
        """_summary_

        Args:
            new_price (_type_): _description_
        """
        self.price = new_price

    def set_square_feet(self, new_square_feet):
        """_summary_

        Args:
            new_price (_type_): _description_
        """
        self.square_feet = new_square_feet

    def set_num_bedrooms(self, new_num_bedrooms):
        """_summary_

        Args:
            new_price (_type_): _description_
        """
        self.num_bedrooms = new_num_bedrooms

    def set_num_baths(self, new_num_baths):
        """_summary_

        Args:
            new_price (_type_): _description_
        """
        self.num_baths = new_num_baths

    def is_big_house(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.square_feet > 15000

    def is_expensive(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.price > 100000

    def is_small_house(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.square_feet < 1000

    def is_cheap(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.price < 5000

    def is_average_sized(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.square_feet > 1000 and self.square_feet < 15000

    def is_roomy(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.num_bedrooms > 3

    def is_bathroom_huge(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.num_baths > 2

    def is_not_roomy(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.num_bedrooms < 3

    def is_not_bathroom_huge(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.num_baths < 2

    def is_under_average_price(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.price < 50000

    def is_over_average_price(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.price > 50000

    def is_under_average_size(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.square_feet < 15000

    def is_over_average_size(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.square_feet > 15000

    def is_under_average_bedrooms(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.num_bedrooms < 3

    def is_over_average_bedrooms(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.num_bedrooms > 3

    def is_under_average_baths(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.num_baths < 2

    def is_over_average_baths(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.num_baths > 2

    def is_under_average_size_and_price(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.square_feet < 15000 and self.price < 50000

    def is_over_average_size_and_price(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.square_feet > 15000 and self.price > 50000

    def is_under_average_bedrooms_and_price(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.num_bedrooms < 3 and self.price < 50000

    def is_over_average_bedrooms_and_price(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.num_bedrooms > 3 and self.price > 50000

    def is_under_average_baths_and_price(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.num_baths < 2 and self.price < 50000

    def is_over_average_baths_and_price(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.num_baths > 2 and self.price > 50000

    def is_under_average_size_and_bedrooms(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.square_feet < 15000 and self.num_bedrooms < 3

    def is_over_average_size_and_bedrooms(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.square_feet > 15000 and self.num_bedrooms > 3

    def is_under_average_size_and_baths(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.square_feet < 15000 and self.num_baths < 2

    def is_over_average_size_and_baths(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.square_feet > 15000 and self.num_baths > 2

    def is_under_average_price_and_bedrooms(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.price < 50000 and self.num_bedrooms < 3

    def is_over_average_price_and_bedrooms(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.price > 50000 and self.num_bedrooms > 3

    def is_under_average_price_and_baths(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.price < 50000 and self.num_baths < 2

    def is_over_average_price_and_baths(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.price > 50000 and self.num_baths > 2

    def is_under_average_size_and_bedrooms_and_price(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.square_feet < 15000 and self.num_bedrooms < 3 and self.price < 50000

    def is_over_average_size_and_bedrooms_and_price(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.square_feet > 15000 and self.num_bedrooms > 3 and self.price > 50000

    def is_under_average_size_and_baths_and_price(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.square_feet < 15000 and self.num_baths < 2 and self.price < 50000

    def is_over_average_size_and_baths_and_price(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.square_feet > 15000 and self.num_baths > 2 and self.price > 50000

    def is_under_average_bedrooms_and_baths_and_price(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.num_bedrooms < 3 and self.num_baths < 2 and self.price < 50000

    def is_over_average_bedrooms_and_baths_and_price(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.num_bedrooms > 3 and self.num_baths > 2 and self.price > 50000

    def is_under_average_size_and_bedrooms_and_baths_and_price(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.square_feet < 15000 and self.num_bedrooms < 3 and self.num_baths < 2 and self.price < 50000

    def is_over_average_size_and_bedrooms_and_baths_and_price(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.square_feet > 15000 and self.num_bedrooms > 3 and self.num_baths > 2 and self.price > 50000

    def is_under_average_price_and_bedrooms_and_baths(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.price < 50000 and self.num_bedrooms < 3 and self.num_baths < 2

    def is_over_average_price_and_bedrooms_and_baths(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.price > 50000 and self.num_bedrooms > 3 and self.num_baths > 2
