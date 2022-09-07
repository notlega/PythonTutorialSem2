# Write a program that prompts the user to entera number between 0 - 100
# Displays a students grade based on the following table:
# 80 - 100: A
# 75 - 79: B+
# 70 - 74: B
# 65 - 69: C+
# 60 - 64: C
# 50 - 59: D
# 40 - 49: E
# 0 - 39: F


def main():
		print("----------------------------------------------------")
		booleanExit = False
		while booleanExit == False:

				# number input in integer
				userInput = int(input("Enter a number between 0 - 100: "))

				if userInput > 100 or userInput < 0:
						# if the number is not between 0 - 100
						print("Invalid input")
				else:
						# if the number is between 0 - 100

						if userInput >= 80:
								# if the number is 80 - 100
								print("Your grade is A!")
						elif userInput >= 75:
								# if the number is 75 - 79
								print("Your grade is B+!")
						elif userInput >= 70:
								# if the number is 70 - 74
								print("Your grade is B!")
						elif userInput >= 65:
								# if the number is 65 - 69
								print("Your grade is C+!")
						elif userInput >= 60:
								# if the number is 60 - 64
								print("Your grade is C!")
						elif userInput >= 50:
								# if the number is 50 - 59
								print("Your grade is D!")
						elif userInput >= 40:
								# if the number is 40 - 49
								print("Your grade is E!")
						else:
								# if the number is 0 - 39
								print("Your grade is F!")

						# exit the program
						booleanExit = True


if __name__ == "__main__":
		main()
