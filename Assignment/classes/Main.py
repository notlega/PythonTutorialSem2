import getpass
from utils.ReadWrite import ReadWrite


class Main:
		"""
		The main class of the program

		...

		Attributes
		----------
		NULL

		Methods
		-------
		NULL
		"""

		def __init__(self) -> None:
				"""
				Parameters
				----------
				NULL
				"""

		def main(self) -> None:
				"""
				The main part of the program

				Parameters
				----------
				NULL
				"""

				while True:
						readWrite = ReadWrite("food.csv")
						food = readWrite.read()
						print(food)
						print("----------------------------------------------------")
						print("Happy Restaurant")
						print("----------------------------------------------------")
						print("1. View Menu")
						print("2. View Order")
						print("3. Admin Menu")
						print("0. Exit")
						print("----------------------------------------------------")

						strInput = input("Enter your choice: ")

						try:
								intInput = int(strInput)
						except ValueError:
								getpass.getpass("Invalid input, please enter to continue.")
								continue

						if intInput == 1:
								# viewMenu()
								pass
						elif intInput == 2:
								# viewOrder()
								pass
						elif intInput == 3:
								# adminMenu()
								pass
						elif intInput == 0:
								break
						else:
								getpass.getpass("Invalid input, please enter to continue.")

						readWrite.write(food)
						print("Thank you for using Happy Restaurant!")
