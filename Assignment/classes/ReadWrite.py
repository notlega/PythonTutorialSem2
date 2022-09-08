class ReadWrite:
		"""
		A class used to read and write from csv files

		...

		Attributes
		----------
		csv_name: str
			The name of the csv file

		Methods
		-------
		read() -> list[list]
			Reads the csv file and returns a 2D List
		write(food: list[list]) -> None
			Takes in a 2D List and writes it to a csv file
		"""

		def __init__(self, csv_name: str) -> None:
				"""
				Parameters
				----------
				csv_name: str
					The name of the csv file
				"""

				self.csv_name = csv_name

		def read() -> list[list]:
				"""
				Reads the csv file and returns a 2D List

				Raises
				------
				FileNotFoundError
					If file is not found within the directory being searched.
				"""
