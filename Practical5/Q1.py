# Rank   | Prize Money ($)
# 1      | 1000
# 2      | 800
# 3      | 700
# 4      | 300
# 5      | 300
# Others | 20
# a) Write a function getInput
# It should prompt for the rank of the contestant
# Returns the value entered
# The function does not take in any parameter
# It should return an int
# b) Write a function printPrize
# Takes in an int parameter called rank
# Checks and displays prize money based on rank
# It does not return any value
# c) Call both functions in main code


def getInput():
		# prompt for rank
		rank = int(input("Enter rank: "))
		# return rank
		return rank


def printPrize(rank):
		# check rank and print prize money
		if rank == 1:
				print("Prize money: $1000")
		elif rank == 2:
				print("Prize money: $800")
		elif rank == 3:
				print("Prize money: $700")
		elif rank == 4 or rank == 5:
				print("Prize money: $300")
		else:
				print("Prize money: $20")


def main():
		print("----------------------------------------------------")
		# call getInput
		rank = getInput()
		# call printPrize
		printPrize(rank)
		print("----------------------------------------------------")


if __name__ == "__main__":
		main()
		