# Print multiples of 5 from 0 to 100
# Using both for loop and while loop


def main():
		print("----------------------------------------------------")
		# while loop version

		# define i
		i = 0
		while i < 101:
				print(i * 5)
				i += 1

		print("----------------------------------------------------")
		# for loop version

		for i in range(101):
				print(i * 5)

		print("----------------------------------------------------")


if __name__ == "__main__":
		main()
