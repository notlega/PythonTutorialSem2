# Write a script to combine two dictionaries
# Add the values for common keys
#
# d1 = {
# 		'a': 100,
# 		'b': 200,
# 		'c': 300
# }
# d2 = {
# 		'a': 300,
# 		'b': 200,
# 		'd': 400
# }
#
# Sample output
# d3 = {
# 		'a': 400,
# 		'b': 400,
# 		'c': 300,
# 		'd': 400
# }


def main():
		print("----------------------------------------------------")
		# create two dictionaries
		d1 = {
				'a': 100,
				'b': 200,
				'c': 300
		}
		d2 = {
				'a': 300,
				'b': 200,
				'd': 400
		}

		# create a new dictionary
		d3 = {}

		# use a for loop to combine the two dictionaries
		for key in d1:
				if key in d2:
						d3[key] = d1[key] + d2[key]
				else:
						d3[key] = d1[key]

		for key in d2:
				if key not in d1:
						d3[key] = d2[key]

		# print the new dictionary
		print(d3)

		print("----------------------------------------------------")


if __name__ == "__main__":
		main()
