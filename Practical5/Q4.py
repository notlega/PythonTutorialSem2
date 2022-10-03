# Write a program that converts Fahrenheit to Celsius
# The formula for conversion is
# Celcius = 5 / 9 * (Fahrenheit - 32)
# a) Write a function to prompt the user for a temperature in Fahrenheit
# The function returns the input value as a float
# b) Write a function to convert Fahrenheit to Celsius
# The function returns the converted value as a float
# c) Call (a) and (b) from main code
# Display the temperature in Celcius


def readFahrenheit():
		# input as float
		return float(input("Enter a temperature in Fahrenheit: "))


def convertFahrenheitToCelsius(fahrenheit):
		# convert fahrenheit to celsius
		return 5 / 9 * (fahrenheit - 32)


def main():
		print("----------------------------------------------------")
		# read fahrenheit
		fahrenheit = readFahrenheit()
		print("----------------------------------------------------")
		# convert fahrenheit to celsius
		print(fahrenheit, "Fahrenheit is", convertFahrenheitToCelsius(fahrenheit), "Celsius")
		print("----------------------------------------------------")


if __name__ == "__main__":
		main()
		