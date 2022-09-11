from getpass import getpass
from classes.Food import Food
from classes.Dish import Dish
from classes.Dessert import Dessert
from classes.Drink import Drink


class ViewMenu:
		"""
		A class to allow users to view the menu and add food to cart

		Attributes
		----------
		None

		Methods
		-------
		view_menu() -> None
						The method that allows viewers to add food to cart
		"""

		def __init__(self) -> None:
				"""
				Parameters
				----------
				None
				"""

				pass

		def view_menu(self) -> None:
				"""
				The method that displays the menu

				Parameters
				----------
				None
				"""

				while True:
						print("----------------------------------------------------")
						print("Menu")
						print("----------------------------------------------------")

						for count, cls in enumerate(Food.__subclasses__()):
								print("{}. {}".format(count + 1, cls.__name__))

						print("0. Back")
						print("----------------------------------------------------")

						strInput = input("Enter your choice: ")

						try:
								intInput = int(strInput)
						except ValueError:
								getpass("Invalid input, please enter to continue.")
								continue

						if intInput == 0:
								break
						else:
								pass
