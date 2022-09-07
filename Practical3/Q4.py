# Write a program that takes in 2 integer values
# Displays all the odd numbers between the 2 integer values excluding themselves
# Assume that 1st number is smaller than or equal to 2nd number


def main():
		print("----------------------------------------------------")
		# 1st integer input
		intInput1 = int(input("Enter 1st integer: "))

		# 2nd integer input
		intInput2 = int(input("Enter 2nd integer: "))

		print("Odd numbers between {} & {}:".format(intInput1, intInput2))
		for i in range(intInput2 - intInput1 + 1):
				# skip i == 0
				if i == 0:
						continue
				
				# check odd numbers using modulus function
				if (intInput1 + i) % 2:
						print(intInput1 + i)
		print("----------------------------------------------------")


if __name__ == "__main__":
		main()
