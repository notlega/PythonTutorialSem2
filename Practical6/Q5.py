# Using the csv file mentioned below
# marks.csv
# Write a script that uses 2 methods of open files
# To read the data from the file and create a 2d list
#
# Sample output
# [['John', 60], ['Mary', 75], ['Sharon', 82], ['Alex', 83]]


import csv


def main():
		print("----------------------------------------------------")
		# method 1: using file open
		list1 = []

		# open file marks.csv and read data
		marks_file = open("marks.csv", "r")

		# use a for loop to filter through data and clean it
		for count, line in enumerate(marks_file):
				# ignore headers
				if count == 0:
						continue

				line = line.strip()
				line = line.split(",")
				list1.append([line[0], int(line[1])])

		# print 2d list list1
		print(list1)

		# close file
		marks_file.close()
		print("----------------------------------------------------")
		# method 2: using csv reader
		list2 = []

		# open file marks.csv
		new_marks_file = open("marks.csv", "r")

		# open file marks.csv and read data
		marks_csv = csv.reader(new_marks_file, delimiter=",")

		# use a for loop to filter through data and clean it
		for count, line in enumerate(marks_csv):
				# ignore headers
				if count == 0:
						continue

				list2.append([line[0], int(line[1])])

		# print 2d list list2
		print(list2)

		# close file
		new_marks_file.close()
		print("----------------------------------------------------")


if __name__ == "__main__":
		main()
