# a) Write a script to write the following text to a new file "greeting.txt"
# "Hello Sir!"
# b) Write a script to append the following new lines to "greeting.txt"
# "How are you?"
# "Hope you are fine"
# c) Open "greeting.txt" to confirm if lines are added successfully


import os


def main():
		# (a)
		# open file for writing
		if not os.path.exists("greeting.txt"):
				# create file
				file = open("greeting.txt", "w")
				# write text
				file.write("Hello Sir!")
				# close file
				file.close()

		# (b)
		# open file for appending
		file = open("greeting.txt", "a")
		# write text
		file.write("How are you?")
		file.write("Hope you are fine")
		# close file
		file.close()


if __name__ == "__main__":
		main()
