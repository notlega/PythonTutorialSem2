# Staff Salary Increment Calculator
# Takes 2 integer values representing years of service and salary of staff
# Displays how much increment the staff will obtain
#
# Years						Salary						Increment
# -------------------------------------------
# Less than 10		Less than $1000		$100
# 								Less than $2000		$200
# 								$2000 or more			$300
# -------------------------------------------
# 10 or more			Less than $1000		$200
# 								Less than $2000		$300
# 								$2000 or more			$400


def main():
    print("----------------------------------------------------")
    print("Staff Salary Increment Calculator")
    print("----------------------------------------------------")

    # staff years of service input in integer
    staffYearsOfService = int(input("Enter your years of service: "))

    # staff salary input in integer
    staffSalary = int(input("Enter your salary: "))

    print("----------------------------------------------------")
    if staffYearsOfService < 10:
        # if staffYearsOfService is lesser than 10

        if staffSalary < 1000:
            # if staffSalary is lesser than 1000
            print("Your increment is $100!")
        elif staffSalary >= 1000 and staffSalary < 2000:
            # if staffSalary is more or equal to 1000 and lesser than 2000
            print("Your increment is $200!")
        else:
            # if staffSalary is more or equal to 2000
            print("Your increment is $300!")
    else:
        # if staffYearsOfService is more or equal to 10

        if staffSalary < 1000:
            # if staffSalary is lesser than 1000
            print("Your increment is $200!")
        elif staffSalary >= 1000 and staffSalary < 2000:
            # if staffSalary is more or equal to 1000 and lesser than 2000
            print("Your increment is $300!")
        else:
            # if staffSalary is more or equal to 2000
            print("Your increment is $400!")
    print("----------------------------------------------------")


if __name__ == "__main__":
    main()
