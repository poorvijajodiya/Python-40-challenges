print("Welcome to the Temperature Conversion App")
print()
F = float(input("What is the given temperature in degrees Fahrenheit: "))
celcius = (5/9)*(F-32)
kelvin = 273.15 + celcius
celcius = round(celcius,4)
kelvin = round(kelvin,4)
F = round(F,4)
print("Degree Fahrenheit:\t{}\nDegrre Celcius:\t\t{}\nDegree Kelvin:\t\t{}".format(F,celcius,kelvin))