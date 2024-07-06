FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5


def convert_to_celsius(fahrenheit):
    result = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return result

def convert_to_fahrenheit(celsius):
    result = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32 
    return result

temperature = float(input("Enter the temperature to convert: "))
c_f = upper(input("Is this temperature in Celsius or Fahrenheit? (C/F): "))

match c_f:
    case "F":
        convert_to_celsius()
    case "C":
        convert_to_fahrenheit()
    case _:
        "Invalid input"