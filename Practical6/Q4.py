# Write a script to read data from the csv file below
# marks.csv
# Determine the name and number of students who scored an A
#
# Score						Grade
# ---------------------
# 80 and above		"A"
# 70 to 79				"B"
# 60 to 69				"C"
# 50 to 59				"D"
# 49 and below		"F"


import csv


def main():
		print("----------------------------------------------------")
		# number of students scoring A in int
		a_students = 0

		# open marks.csv file
		marks = open("marks.csv", "r")

		# read marks.csv file with csv import
		marks_reader = csv.reader(marks, delimiter=",")

		# for loop to clean and append data into marks list
		for count, marks in enumerate(list(marks_reader)):
				if count == 0:
						# to ignore header
						continue

				if int(marks[1]) >= 80:
						# if student scores an A
						print(marks[0], "has scored an A!")

						# +1 to a_student count
						a_students += 1

		print("----------------------------------------------------")
		# print number of students who scored A
		print("Total number of students who scored A:", str(a_students))

		print("----------------------------------------------------")


if __name__ == "__main__":
		main()
