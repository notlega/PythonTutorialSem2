from getpass import getpass
from options.ViewMenu import ViewMenu
from utils.ReadWrite import ReadWrite


class Main:
		"""
		The main class of the program

		...

		Attributes
		----------
		None

		Methods
		-------
		main() -> None
			The main method of the system.
		"""

		def __init__(self) -> None:
				"""
				Parameters
				----------
				NULL
				"""

				pass

		def main(self) -> None:
				"""
				The main method of the system

				Parameters
				----------
				None
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
								getpass("Invalid input, please enter to continue.")
								continue

						if intInput == 1:
								view_menu = ViewMenu()
								view_menu.view_menu()
						elif intInput == 2:
								# viewOrder()
								pass
						elif intInput == 3:
								# adminMenu()
								pass
						elif intInput == 0:
								break
						else:
								getpass("Invalid input, please enter to continue.")

				readWrite.write(food)
				print("Thank you for using Happy Restaurant!")


if __name__ == "__main__":
		main = Main()
		main.main()
