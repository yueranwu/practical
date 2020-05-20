"""
CP1404 practical 08
This is the test program for SilverServiceTaxi class
"""
from silver_service_taxi import SilverServiceTaxi


def main():
    silver = SilverServiceTaxi("silver", 100, 2)
    silver.drive(18)
    print(silver)
    fare = silver.get_fare()
    print(fare)


main()