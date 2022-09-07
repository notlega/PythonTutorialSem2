# Prompts user for 5 integers
# Displays the sum of the integers entered


def main():
		print("----------------------------------------------------")
		# for loop version

		# instantiate sum
		forSum = 0

		# loops 5 times
		for i in range(5):
				forSum += int(input("number" + str(i + 1) + ": "))

		print("Sum of numbers:", forSum)
		print("----------------------------------------------------")
		# while loop version

		# instantiate sum
		whileSum = 0

		# create i
		i = 1

		# loops 5 times
		while i < 6:
				whileSum += int(input("number" + str(i) + ": "))
				i += 1

		print("Sum of numbers:", whileSum)
		print("----------------------------------------------------")


if __name__ == "__main__":
		main()
