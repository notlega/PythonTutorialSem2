# initalise a list with the following values
# my_list = [1, 5, 6, 7, 9, 100, 23, 6, 5, 1]
# filter out the duplicate values and produce the following list
# [1, 5, 6, 7, 9, 23, 100]
# print out the list


def main():
		print("----------------------------------------------------")
		# initialise my_list
		my_list = [1, 5, 6, 7, 9, 100, 23, 6, 5, 1]
		
		# use list comprehension to remove duplicates
		# initialise new list
		new_list = []
		
		# for loop through my_list to check each number
		for num in my_list:
				if num not in new_list:
						# if current number is not in the new list
						new_list.append(num)

		# TODO: if you have big brain u can use quicksort
		# sort list using built in bubble sort algo
		new_list.sort()

		# print sorted list
		print(new_list)
		print("----------------------------------------------------")
		

if __name__ == "__main__":
		main()
