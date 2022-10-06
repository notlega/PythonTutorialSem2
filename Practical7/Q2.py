# Create a script to create a dictionary from a string
# The string is an input by the user
# The dictionary should track the count of letters within
# The program will then output the letters in the string in ascending order
#
# Sample output
# String: resource
# Dictionary: {'r': 2, 'e': 2, 's': 1, 'o': 1, 'u': 1, 'c': 1}
# The word 'resource' is made up of:
# 1 'c'
# 1 'e'
# 2 'o'
# 1 'r'
# 2 's'
# 1 'u'


def main():
		print("----------------------------------------------------")
		# create a dictionary
		d = {}

		# get user input
		string = input("String: ")

		# use a for loop to count the letters
		for letter in string:
				if letter in d:
						d[letter] += 1
				else:
						d[letter] = 1

		# print the dictionary
		print("Dictionary:", d)

		# print the word
		print("The word '" + string + "' is made up of:")

		# use a for loop to print the letters in ascending order
		for letter in sorted(d):
				print(str(d[letter]) + " '" + letter + "'")

		print("----------------------------------------------------")


if __name__ == "__main__":
		main()
