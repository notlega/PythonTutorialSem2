# Write a script that takes in a series of numbers from a text file
# Each line of the text file should contain exactly one integer
# Eg. p2_t1_data.txt
# The script should print out some statistics regarding the file and its content
#
# Sample output
# Enter the input file name please: p2_t1_data.txt
# p2_t1_data.txt contains 9 numbers
# The total sum of all the 9 numbers is 1093
# The average sum of all the numbers is 121.44
#
# TO RUN THE SCRIPT, DRAG THE TXT OUT INTO THE MAIN FOLDER


def main():
		# input of file name in string
		file_name = input("Enter the input file name please: ")

		# open and read file
		file = open(file_name, "r")

		# get list of numbers within file
		numbers = file.readlines()

		# print out number of numbers within file
		print(file_name, "contains", len(numbers), "numbers")

		# calculate total sum of numbers using a for loop
		total_sum = 0
		for num in numbers:
				total_sum += int(num)

		# print out total sum of all numbers within file
		print("The total sum of all the", len(numbers), "numbers is", round(total_sum, 2))

		# calculate the average of all numbers
		average = total_sum / len(numbers)

		# print out the average of all numbers within file
		print("The average of the numbers is", round(average, 2))

		# close file
		file.close()


if __name__ == "__main__":
		main()
