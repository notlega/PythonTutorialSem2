# Write a script to read the contents of two text files mentioned
# movies.txt
# fruits.txt
# Place the data of both files into two corresponding lists
# Print out both size and contents of both lists


def main():
		print("----------------------------------------------------")
		# open movies.txt file
		movies_txt = open("movies.txt", "r")

		# movies list read from movies.txt in list
		# use of for loop to remove \n from every element except last
		movies_list = []
		for str in movies_txt.readlines():
				movies_list.append(str.replace("\n", ""))

		# print out data of movies list
		print("Name of file:", movies_txt.name)
		print("Size of file:", len(movies_list))
		print("Contents of file:", movies_list)

		# close movies.txt file
		movies_txt.close()

		print("----------------------------------------------------")
		# open fruits.txt file
		fruits_txt = open("fruits.txt", "r")

		# fruits list read from fruits.txt in list
		# use of for loop to remove \n from every element except last
		fruits_list = []
		for str in fruits_txt.readlines():
				fruits_list.append(str.replace("\n", ""))

		# print out data of fruits list
		print("Name of file:", fruits_txt.name)
		print("Size of file:", len(fruits_list))
		print("Contents of file:", fruits_list)

		# close fruits.txt file
		fruits_txt.close()
		print("----------------------------------------------------")


if __name__ == "__main__":
		main()
