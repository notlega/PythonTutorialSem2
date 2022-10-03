# Create a List list1 that stores int
# Program will repeatedly prompt user for int input from keyboard
# Until user enters N
# Afterwards, use a for loop to retrieve the largest number from list
# Print it out


def main():
		print("----------------------------------------------------")
		# List list1
		list1 = []

		# while loop to reapeatedly get inputs
		while True:
				# input prompt
				num_str = input("Enter an integer or \"N\": ")
				
				if num_str.lower() == "n":
						# if input == N or input == n, exit loop
						break
				else:
						# if input is an integer, append to list
						list1.append(int(num_str))

		# initialise largest num variable
		largest_num = 0

		# for loop through list1
		for num in list1:
				if num > largest_num:
						# if current num in list is larger than current largest num
						# largest num will become current num
						largest_num = num

		# print out largest number using f string
		print(f"Largest number: {largest_num}")
		print("----------------------------------------------------")


if __name__ == "__main__":
		main()
