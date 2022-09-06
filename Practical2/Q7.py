# Leap Year Checker
# (  (divisible by 4) and (not divisible by 100)  )    or   (divisible by 400)


def main():
    print("----------------------------------------------------")
    print("Leap Year Checker")
    print("----------------------------------------------------")

    # year input as integer
    year = int(input("Enter a year: "))

    print("----------------------------------------------------")
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        # Leap year
        print(year, "is a leap year")
    else:
        # Not a leap year
        print(year, "is not a leap year")
    print("----------------------------------------------------")


if __name__ == "__main__":
    main()
