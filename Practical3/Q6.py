# Bubble Tea Shop
# Use a while loop to allow users to select their drink of choice
# Exit when neccessary


def main():
		# while loop to start program
		while True:
				# print shop details
				print("----------------------------------------------------")
				print("Bubble Tea Shop")
				print("----------------------------------------------------")
				print("1. Coffee")
				print("2. Tea")
				print("3. Bubble Tea")
				print("0. No Thanks")
				print("----------------------------------------------------")

				# get int input
				intInput = int(input("Enter 1, 2, 3, or 0 to exit: "))

				print("----------------------------------------------------")
				if intInput == 1:
						# print coffee
						print("You choose Coffee.")
						break
				elif intInput == 2:
						# print tea
						print("You choose Tea.")
						break
				elif intInput == 3:
						# print bubble tea
						print("You choose Bubble Tea.")
						break
				elif intInput == 0:
						# print no thanks
						print("Thank You! Bye bye!")
						break
				else:
						# print invalid input
						print("Enter integer 1, 2, 3, or 0 only!")
		print("----------------------------------------------------")


if __name__ == "__main__":
		main()
