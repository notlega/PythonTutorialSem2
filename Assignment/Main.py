def main():
		exitBoolean = True
		while exitBoolean:
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
						input("Invalid input, please enter to continue.")
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
						exitBoolean = False
				else:
						input("Invalid input, please enter to continue.")

		print("Thank you for using Happy Restaurant!")


if __name__ == "__main__":
		main()
