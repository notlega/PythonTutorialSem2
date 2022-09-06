# Display an aquarium's water health information
# Allow user to input the pH level number (0 - 14)
# Display a message indicating health (acidic, neutral, alkaline)


def main():
    print("----------------------------------------------------")
    print("Aquarium's Water Health Information")
    print("----------------------------------------------------")

    # pHLevel input in integer
    pHLevel = int(input("Enter pH level: "))

    print("----------------------------------------------------")
    if pHLevel > 0 and pHLevel < 7:
				# if pHLevel is more than 0 and lesser than 7
        print("The water in your tank is acidic!")
    elif pHLevel > 7:
				# if pHLevel is more than 7
        print("The water in your tank is alkaline!")
    else:
				# if pHLevel is 7
        print("The water in your tank is neutral!")
    print("----------------------------------------------------")


if __name__ == "__main__":
    main()
