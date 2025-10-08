def convert_to_days():
    nb_hours=int(input("Enter number of hours: "))
    nb_minutes=int(input("Enter number of minutes: "))
    nb_seconds=int(input("Enter number of seconds: "))
    days = get_days(nb_hours, nb_minutes, nb_seconds)
    print(f"The number of days is: {days:.4f}")

def get_days(hours, minutes, seconds):
    total_days = (hours / 24) + (minutes / 1440) + (seconds / 86400)
    return total_days

#convert_to_days()

def calc_weight_on_planet(weight,gravity=23.1):
    return weight * gravity / 9.81


# print(calc_weight_on_planet(70, 3.7))  # Mars
# print(calc_weight_on_planet(70, 8.87)) # Venus
# print(calc_weight_on_planet(70)) 
# print(calc_weight_on_planet(70, 23.1)) # 

def num_atoms(mass, molar_mass=196.97, avogadro=6.022e23):
    return (mass / molar_mass) * avogadro

# print(num_atoms(10)) # Gold
# print(num_atoms(10, 12.001)) # Carbon
# print(num_atoms(10, 1.008)) # Hydrogen

def calc_new_height():
    current_width = float(input("Enter current width in cm: "))
    curent_height = float(input("Enter current height in cm: "))
    desired_width = float(input("Enter desired width in cm: "))
    new_height = (desired_width * curent_height) / current_width
    print(f"The new height should be: {new_height:.2f} cm")
    return new_height

# calc_new_height()

def convert_temp():
    temp_farenheit = float(input("Enter temperature in Fahrenheit: "))
    print(f"The temperature in Fahrenheit is: {temp_farenheit}")
    print(f"The temperature in Celsius is: {convert_to_celsius(temp_farenheit)}")
    print(f"The temperature in Kelvin is: {convert_to_kelvin(temp_farenheit)}")

def convert_to_celsius(temp_farenheit):
    return (temp_farenheit - 32) * 5/9

def convert_to_kelvin(temp_farenheit):
    return convert_to_celsius(temp_farenheit) + 273.15

convert_temp()