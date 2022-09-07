# Using a While loop to prompt a user for an input
# If the user enters "hello", display "This will be printed only when user input "hello""
# If user enters "e" or "E", exit
# If user enters anything else, display "Other Input: <input>"


def main():
		print("----------------------------------------------------")
		# while loop for user prompt
		while True:
				# user input in string
				userInput = input("Your Input (\"E\" to exit) : ")

				if userInput.lower() == "hello".lower():
						# if userInput is hello
						print("This will be printed only when user input \"hello\"")
				elif userInput.lower() == "e":
						# exit program
						print("Exit the while loop.")
						break
				else:
						# if userInput is anything else
						print("Other Input: " + userInput)
		print("----------------------------------------------------")


if __name__ == "__main__":
		main()
