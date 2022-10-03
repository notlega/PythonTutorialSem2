# Leap Year Checker
# (  (divisible by 4) and (not divisible by 100)  )    or   (divisible by 400)
# a) Write a fucntion isLeapYear 
# This function takes in an int parameter named year
# This function returns True if year is a leap year, False otherwise
# b) Write a function readYear
# This function takes no parameters
# This function prompts the user for a year
# This function returns the year as an int
# c) Modify main code to use the functions readYear and isLeapYear


def isLeapYear(year):
		if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
				# Leap year
				return True
		else:
				# Not a leap year
				return False


def readYear():
		# year input as integer
		year = int(input("Enter a year: "))
		# return year
		return year


def main():
		print("----------------------------------------------------")
		print("Leap Year Checker")
		print("----------------------------------------------------")
		# read year
		year = readYear()
		print("----------------------------------------------------")
		if isLeapYear(year):
				# Leap year
				print(year, "is a leap year")
		else:
				# Not a leap year
				print(year, "is not a leap year")
		print("----------------------------------------------------")


if __name__ == "__main__":
		main()
