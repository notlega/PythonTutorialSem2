# Using the text file mentioned below
# student.txt
# Write a script to read the data from the file
# The script must use "with open("student.txt") as file"
# Create a 2d list with the data
#
# Sample output
# [['John', 'p12345', 75], ['Jack', 'p23456', 41], ['Mary', 'p31111', 46], ['Sharon', 'p34222', 81]]


def main():
		print("----------------------------------------------------")
		# open file using with open
		with open("student.txt") as file:
				# create a 2d list
				list1 = []

				# use a for loop to filter through data and clean it
				for line in file:
						line = line.strip()
						line = line.split(",")
						list1.append([line[0], line[1], int(line[2])])

				# print 2d list list1
				print(list1)
		
		print("----------------------------------------------------")


if __name__ == "__main__":
		main()
