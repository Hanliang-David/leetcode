# temperature_converter.py
def celsius_to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

c = 100
f = 212
print(f"{c}°C is {celsius_to_fahrenheit(c)}°F")
print(f"{f}°F is {fahrenheit_to_celsius(f)}°C")
