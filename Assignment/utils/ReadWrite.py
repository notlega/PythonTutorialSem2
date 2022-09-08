import csv


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

		def read(self) -> list[list]:
				"""
				Reads the csv file and returns a 2D List

				Raises
				------
				FileNotFoundError
					If file is not found within the directory being searched.
				"""

				with open(self.csv_name, "r", newline="") as file:
						reader = csv.reader(file, delimiter=",")
						dataList = []
						for count, row in enumerate(list(reader)):
								if count == 0:
										dataList.append(row)
										continue

								dataList.append([row[0], row[1], float(row[2]), int(row[3])])
						return dataList

		def write(self, food: list[list]) -> None:
				"""
				Takes in a 2D List and writes to a csv file

				Raises
				------
				FileNotFoundError
					If file is not found within the directory being searched.
				"""

				with open(self.csv_name, "w+", newline="") as file:
						writer = csv.writer(file)
						writer.writerows(food)
