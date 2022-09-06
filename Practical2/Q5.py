# Rental Calculator
# Takes in type of bicyle and number of hours rented
# Displays the rental fee


def main():
    print("----------------------------------------------------")
    print("Rental Calculator")
    print("----------------------------------------------------")
    print("Types of bicycles")
    print("1. Single Seater\n2. Double Seater")

    # type of bicycle in integer either 1 or 2
    bicycleType = int(input("Enter type of bicycle: "))

    # number of hours rented in integer
    numHoursRented = int(input("Enter number of hours rented: "))

    # initialise rental fee
    rentalFee = 0.0

    if bicycleType == 1:
        # if bicycle type is single seater
        rentalFee = 5.5 * numHoursRented
    elif bicycleType == 2:
        # if bicycle type is double seater
        rentalFee = 7.8 * numHoursRented

    if numHoursRented >= 3:
        rentalFee *= 0.7

    print("----------------------------------------------------")
    # print rental fee in 2dp
    print("Your rental fee is ${:.2f}".format(round(rentalFee, 2)))
    print("----------------------------------------------------")


if __name__ == "__main__":
    main()
