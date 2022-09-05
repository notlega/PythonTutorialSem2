# Sum and Divisibility Check Calculator
# Prompts user for 2 integers
# Adds the 2 integers together and displays the result
# Checks if the first integer is divisible by the second integer
# Displays a boolean result

def main():
		print('----------------------------------------------------')
		print('Sum and Divisibility Check Calculator')
		print('----------------------------------------------------')

		# input for firstInteger in Integer
		firstInteger = int(input('Enter the 1st integer: '))

		# input for secondInteger in Integer
		secondInteger = int(input('Enter the 2nd integer: '))

		# checks if firstInteger is divisible by secondInteger and defines a boolean variable
		divisibleBoolean = True
		if firstInteger % secondInteger != 0:
				divisibleBoolean = False

		print('----------------------------------------------------')
		# prints sumOfIntegers
		print('The SUM of ' + str(firstInteger) + ' + ' + str(secondInteger) + ' = ' + str(firstInteger + secondInteger))
		# prints divisible result
		print(str(firstInteger) + ' is divisible by ' + str(secondInteger) + '? (True or False) : ' + str(divisibleBoolean))
		print('----------------------------------------------------')


if __name__ == "__main__":
		main()
