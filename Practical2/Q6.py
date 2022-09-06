# Step 1:  Prompt user for 2 numbers with value between 1 to 10.
# Step 2:  Find the average of the 2 numbers.
# Step 3:  Display the following message:
# 									A < B < C
# 			Where A is the smaller number, B is the average and C is the larger number.
# 			OR
# 			A=B=C
# 			if the A,B,C values are all the same.


def main():
    print("----------------------------------------------------")

    # first integer number input
    num1 = int(input("Enter 1st number between 1 - 10: "))

    # second integer number input
    num2 = int(input("Enter 2nd number between 1 - 10: "))

    # calculate average between num1 and num2
    numAvg = (num1 + num2) / 2

    print("----------------------------------------------------")
    # print average of num1 and num2
    print("Average of 1st and 2nd number is: {:.1f}".format(round(numAvg, 2)))

    if num1 == num2:
        # if all numbers are equal
        print("{} = {} = {}".format(num1, numAvg, num2))
    else:
        # if numbers are not equal

        if num1 > num2:
            # if num1 is more than num2
            print("{} < {} < {}".format(num2, numAvg, num1))
        else:
            # if num2 is more than num1
            print("{} < {} < {}".format(num1, numAvg, num2))
    print("----------------------------------------------------")


if __name__ == "__main__":
    main()
