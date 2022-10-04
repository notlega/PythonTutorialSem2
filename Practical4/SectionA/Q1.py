# Create a List named numberList with 50 cells
# Prompt for 2 numbers, num1 and num2
# Initalise all cells of odd index with num1 and even index with num2
# Create without using for loop


def main():
		print("----------------------------------------------------")

		# get num1 input in integer
		num1 = int(input("Enter num1: "))

		# get num2 input in integer
		num2 = int(input("Enter num2: "))
		print("----------------------------------------------------")

		numberList = []

		i = 0

		# set while loop to loop 50 times
		while i < 50:
				if i % 2 == 0:

						# if list index is an even number
						numberList.append(num2)
				else:

						# if list index is not an even number
						numberList.append(num1)
				
				i += 1

		# print numberList out
		print(numberList)
		print("----------------------------------------------------")


if __name__ == "__main__":
		main()
