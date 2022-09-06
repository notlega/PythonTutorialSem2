# Student Score Calculator
# Student enters his score
# Displays the student's grade
#
# Score						Grade
# ---------------------
# 80 and above		"A"
# 70 to 79				"B"
# 60 to 69				"C"
# 50 to 59				"D"
# 49 and below		"F"


def main():
    print("----------------------------------------------------")
    print("Student Score Calculator")
    print("----------------------------------------------------")

    # student score input in integer
    studentScore = int(input("Enter your score: "))

    print("----------------------------------------------------")
    if studentScore >= 80:
        # if studentScore is more or equal to 80
        print("Your grade is A!")
    elif studentScore >= 70 and studentScore <= 79:
        # if studentScore is more or equal to 70 and lesser or equal to 79
        print("Your grade is B!")
    elif studentScore >= 60 and studentScore <= 69:
        # if studentScore is more or equal to 60 and lesser or equal to 69
        print("Your grade is C!")
    elif studentScore >= 50 and studentScore <= 59:
        # if studentScore is more or equal to 50 and lesser or equal to 59
        print("Your grade is D!")
    else:
        # if studentScore is lesser than 50
        print("Your grade is F!")


if __name__ == "__main__":
    main()
