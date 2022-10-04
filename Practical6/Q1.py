# a) Write a script to write the following text to a new file "greeting.txt"
# "Hello Sir!"
# b) Write a script to append the following new lines to "greeting.txt"
# "How are you?"
# "Hope you are fine"
# c) Open "greeting.txt" to confirm if lines are added successfully


def main():
		# (a)
		# open file for writing
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
		file.write("\nHow are you?")
		file.write("\nHope you are fine")
		# close file
		file.close()


if __name__ == "__main__":
		main()
