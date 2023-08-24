def convert_length(value, from_unit, to_unit):
    conversion_factors = {
        "meters": 1,
        "centimeters": 0.01,
        "millimeters": 0.001,
        "feet": 0.3048,
        "inches": 0.0254,
        "yards": 0.9144,
        "kilometers": 1000,
        "miles": 1609.34,
    }
    return value * conversion_factors[from_unit] / conversion_factors[to_unit]

def convert_weight(value, from_unit, to_unit):
    conversion_factors = {
        "kilograms": 1,
        "grams": 0.001,
        "milligrams": 0.000001,
        "pounds": 0.453592,
        "ounces": 0.0283495,
    }
    return value * conversion_factors[from_unit] / conversion_factors[to_unit]

def convert_temperature(value, from_unit, to_unit):
    if from_unit == "celsius" and to_unit == "fahrenheit":
        return (value * 9/5) + 32
    elif from_unit == "fahrenheit" and to_unit == "celsius":
        return (value - 32) * 5/9
    elif from_unit == "celsius" and to_unit == "kelvin":
        return value + 273.15
    elif from_unit == "kelvin" and to_unit == "celsius":
        return value - 273.15
    else:
        return value

def main():
    print("Unit Conversion Calculator")

    while True:
        print("\nSelect conversion:")
        print("1. Length")
        print("2. Weight")
        print("3. Temperature")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            value = float(input("Enter value: "))
            from_unit = input("Enter from unit: ").lower()
            to_unit = input("Enter to unit: ").lower()
            result = convert_length(value, from_unit, to_unit)
            print(f"{value} {from_unit} = {result} {to_unit}")

        elif choice == "2":
            value = float(input("Enter value: "))
            from_unit = input("Enter from unit: ").lower()
            to_unit = input("Enter to unit: ").lower()
            result = convert_weight(value, from_unit, to_unit)
            print(f"{value} {from_unit} = {result} {to_unit}")

        elif choice == "3":
            value = float(input("Enter value: "))
            from_unit = input("Enter from unit (celsius/fahrenheit/kelvin): ").lower()
            to_unit = input("Enter to unit (celsius/fahrenheit/kelvin): ").lower()
            result = convert_temperature(value, from_unit, to_unit)
            print(f"{value} {from_unit} = {result} {to_unit}")

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()