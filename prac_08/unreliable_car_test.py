"""
CP1404 Practical 08
This is a program for testing the UnreliableCar class
"""

from unreliable_car import UnrealiableCar


def main():
    car = UnrealiableCar("car", 100, 50)

    # try more times
    print(car)
    car.drive(50)
    print(car)


main()


"""
def main():


    # create cars with different reliabilities
    good_car = UnreliableCar("Mostly Good", 100, 90)
    bad_car = UnreliableCar("Dodgy", 100, 9)

    # attempt to drive the cars many times
    # output what distance they drove
    for i in range(1, 12):
        print("Attempting to drive {}km:".format(i))
        print("{:12} drove {:2}km".format(good_car.name, good_car.drive(i)))
        print("{:12} drove {:2}km".format(bad_car.name, bad_car.drive(i)))

    # print the final states of the cars
    print(good_car)
    print(bad_car)
main()
"""