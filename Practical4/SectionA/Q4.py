# 			|	Math | English | Science
# Benny | 89   | 45      | 55
# Robin | 56   | 86      | 23
# Sally | 88   | 81      | 73
# Aaron | 35   | 75      | 39
# Simon | 65   | 62      | 77
# a) Create a 2d list called marks using the table above
# b) Print Sally's name and her math marks
# c) Display each student's name and math marks using a for loop
# d) Display each student's name and average marks of all subjects using a nested for loop


def main():
		print("----------------------------------------------------")
		# part a
		# initialise 2d list marks
		marks = [[]] * 5
		marks[0] = ["Benny", 89, 45, 55]
		marks[1] = ["Robin", 56, 86, 23]
		marks[2] = ["Sally", 88, 81, 73]
		marks[3] = ["Aaron", 35, 75, 39]
		marks[4] = ["Simon", 65, 62, 77]

		# part b
		# print Sally's name and her math marks
		print(marks[2][0], marks[2][1])
		print("----------------------------------------------------")

		# part c
		# display each student's name and math marks using a for loop
		for student in marks:
				print(student[0], student[1])
		print("----------------------------------------------------")

		# part d
		# display each student's name and average marks of all subjects using a nested for loop
		for student in marks:
				# initialise average to 0
				average = 0
				# for loop through all marks of the student
				for mark in student[1:]:
						# add mark to average
						average += mark
				# divide average by 3
				average /= 3
				# print student name and average
				print(student[0], average)
		print("----------------------------------------------------")


if __name__ == "__main__":
		main()
