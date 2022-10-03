# a) Write a fucntion getInput 
# This function takes in a string parameter
# The parameter will be used in the input dialog prompt
# eg. getInput("1st")
# This function returns the int input value
# b) Write a function findMax
# This function takes in two int parameters named num1 and num2
# This function compares which number is bigger
# This function returns one of the following string values
# "1st number is bigger"
# "2nd number is bigger"
# "The 2 numbers are equal"
# c) Modify main code to use the functions getInput("1st"), getInput("2nd"), and findMax()


def getInput(prompt):
		# input as integer
		return int(input("Enter the " + prompt + " number: "))


def findMax(num1, num2):
		if num1 > num2:
				# 1st number is bigger
				return "1st number is bigger"
		elif num2 > num1:
				# 2nd number is bigger
				return "2nd number is bigger"
		else:
				# The 2 numbers are equal
				return "The 2 numbers are equal"


def main():
		print("----------------------------------------------------")
		# read 1st number
		num1 = getInput("1st")
		# read 2nd number
		num2 = getInput("2nd")
		print("----------------------------------------------------")
		# find max
		print(findMax(num1, num2))
		print("----------------------------------------------------")


if __name__ == "__main__":
	main()
