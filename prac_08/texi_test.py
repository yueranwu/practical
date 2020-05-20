"""
CP1404 Practical
This is a test program for testing Taxi class
"""

from taxi import Taxi


def main():
    """
    print taxi information
    """
    prius_taxi = Taxi("Prius 1", 100)

    prius_taxi.drive(40)    # Drive the taxi 40m
    print(prius_taxi)   # print the taxi's current details and the current fare
    print(" +-- Current fare {:.2f}".format(prius_taxi.get_fare()))

    prius_taxi.start_fare()  # restart the meter (start a new fare)
    prius_taxi.drive(100)
    print(prius_taxi)
    print(" +-- Current fare {:.2f}".format(prius_taxi.get_fare()))


main()
