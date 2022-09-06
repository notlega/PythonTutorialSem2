# Fahrenheit to Celcius
# Inputs a fahrenheit temp and outputs a celcius temp


def main():
    print("----------------------------------------------------")
    print("Fahrenheit to Celcius Conversion")
    print("----------------------------------------------------")

    # get fahrenheit temp in float
    fahrenheitTemp = float(input("Enter the temperature in fahrenheit : "))

    # convert from fahrenheit to celcius
    celciusTemp = 5 / 9 * (fahrenheitTemp - 32)

    print("----------------------------------------------------")
    # str.format to format the string celciusTemp into 2dp
    print(
        str.format(
            "Temperature in celcius is : {celciusTemp:.2f}", celciusTemp=celciusTemp
        )
    )
    print("----------------------------------------------------")


if __name__ == "__main__":
    main()
