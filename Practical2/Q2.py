# BMI Weight Calculator
# Calculates a persons BMI using their height in meters and weight in kg
# Displays a message of their weight status based on their BMI
# BMI FORMULA = weight / height^2
#
# BMI							Weight Status
# -----------------------------
# Below 18.5			Underweight
# 18.5 - 24.9			Normal
# 25 - 29.9				Overweight
# 30 & above			Obese


def main():
		print("----------------------------------------------------")
		print("BMI Calculator")
		print("----------------------------------------------------")

		# kg weight input in float
		kgWeight = float(input("Enter weight in kilograms: "))

		# meter height input in float
		mHeight = float(input("Enter height in meters: "))

		# calculate BMI using weight and height
		BMI = kgWeight / (mHeight ** 2)

		print("----------------------------------------------------")
		# print BMI in 1dp
		print("Your BMI is: {:.2f}".format(round(BMI, 2)))
		if BMI > 0 and BMI < 18.5:
				# if BMI is positive and lesser than 18.5
				print("You are Underweight!")
		elif BMI >= 18.5 and BMI <= 24.9:
				# if BMI is more or equal to 18.5 and lesser than or equal to 24.9
				print("You are Normal!")
		elif BMI >= 25 and BMI <= 29.9:
				# if BMI is more or equal to 25 and lesser than or equal to 29.9
				print("You are Overweight!")
		else:
				# if BMI is more or equal to 30
				print("You are Obese!")
		print("----------------------------------------------------")


if __name__ == "__main__":
		main()
