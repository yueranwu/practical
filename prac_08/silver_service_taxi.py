"""
Create a class
"""

from taxi import Taxi


class SilverServiceTaxi(Taxi):
    """specialised version of a taxi"""
    flagfall = 4.5

    def __init__(self, name, fuel, fanciness):
        """initiate a silver service taxi"""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km = self.price_per_km * self.fanciness

    def __str__(self):
        """Return a string representation of a SilverServiceTaxi."""
        return "{} plus flagfall of ${:.2f}".format(super().__str__(), self.flagfall)

    def get_fare(self):
        """update method in Taxi class to round and return value"""
        return self.flagfall + super().get_fare()
