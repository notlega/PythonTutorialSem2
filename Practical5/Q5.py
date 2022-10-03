# Complete the below program
# def readInput():
# 		Prompt the user for the number of rows and columns
# 		Convert and return the input as an int
#
#
# def choosePattern():
# 		Prompt the user for the pattern to be printed
# 		Convert and return the input as an int
#
#
# def printPattern1(n):
# 		Print the pattern as shown below
# 		Assuming n = 4
# 		1	1	1	1
# 		2	2	2	2
# 		3	3	3	3
# 		4	4	4	4
#
#
# def printPattern2(n):
# 		Print the pattern as shown below
# 		Assuming n = 4
# 		1	2	3	4
# 		1	2	3	4
# 		1	2	3	4
# 		1	2	3	4
#
#
# def main():
# 		pat = choosePattern()
# 		num = readInput()
# 		Code the if statement to invoke the correct printPattern function
# 		depending on the value of pat
#
#
# if __name__ == "__main__":
# 		main()
#
# Sample Output 1
# 1. Choose pattern 1
# 2. Choose pattern 2
# Your pattern: 1
# Enter number of rows: 3
# 1	1	1
# 2	2	2
# 3	3	3
#
# Sample Output 2
# 1. Choose pattern 1
# 2. Choose pattern 2
# Your pattern: 2
# Enter number of rows: 3
# 1	2	3
# 1	2	3
# 1	2	3


def readInput():
		# Prompt the user for the number of rows and columns
		# Convert and return the input as an int
		return int(input("Enter number of rows: "))


def choosePattern():
		# Prompt the user for the pattern to be printed
		# Convert and return the input as an int
		return int(input("1. Choose pattern 1\n2. Choose pattern 2\nYour pattern: "))


def printPattern1(n):
		# Print the pattern as shown below
		# Assuming n = 4
		# 1	1	1	1
		# 2	2	2	2
		# 3	3	3	3
		# 4	4	4	4
		for i in range(1, n + 1):
				for j in range(1, n + 1):
						print(i, end="\t")
				print()


def printPattern2(n):
		# Print the pattern as shown below
		# Assuming n = 4
		# 1	2	3	4
		# 1	2	3	4
		# 1	2	3	4
		# 1	2	3	4
		for i in range(1, n + 1):
				for j in range(1, n + 1):
						print(j, end="\t")
				print()


def main():
		pat = choosePattern()
		num = readInput()
		# Code the if statement to invoke the correct printPattern function
		# depending on the value of pat
		if pat == 1:
				printPattern1(num)
		elif pat == 2:
				printPattern2(num)


if __name__ == "__main__":
		main()
