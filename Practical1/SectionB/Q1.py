# Module Score Calculator
# Computes the module score - a weighted average

def main():
		print('----------------------------------------------------')
		print('Module Score Calculator')
		print('----------------------------------------------------')

		# COMPONENTS						WEIGHTAGES
		# Mid-Semester Test		: 20%
		# Assignment 1				: 25%
		# Assignment 2				: 30%
		# General Performance	: 20%

		# input for Mid-Semester Test in Integer
		MSTScore = int(input('Enter your MST Score\t\t\t: '))

		# input for Assignment 1 in Integer
		Assignment1Score = int(input('Enter your Assignment 1 Score\t\t: '))
		
		# input for Assignment 2 in Integer
		Assignment2Score = int(input('Enter your Assignment 2 Score\t\t: '))

		# input for General Performance in Integer
		GPScore = int(input('Enter your General Performance Score\t: '))

		# calculate moduleScore based on weightages
		moduleScore = (MSTScore / 100 * 20) + (Assignment1Score / 100 * 25) + (Assignment2Score / 100 * 35) + (GPScore / 100 * 20)

		print('----------------------------------------------------')
		# print the moduleScore out
		print('Your module score is ' + str(moduleScore))
		print('----------------------------------------------------')


if __name__ == "__main__":
		main()
