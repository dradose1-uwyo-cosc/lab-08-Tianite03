# Talon Bluemel
# UWYO COSC 1010
# 11-05-24
# Homework: 3
# Lab Section:12
# Sources, people worked with, help given to: I had to look up Zeller's congruence which made this way easier. https://www.geeksforgeeks.org/zellers-congruence-find-day-date/

def get_day(mm, dd, yyyy):
    # Adjust months and year for Zeller's Congruence
    if mm < 3:
        mm += 12
        yyyy -= 1

    # Zeller's Congruence calculation
    k = yyyy % 100  
    j = yyyy // 100 
    day_of_week = (dd + ((13 * (mm + 1)) // 5) + k + (k // 4) + (j // 4) - (2 * j)) % 7

    days = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    
    return days[day_of_week]

date_input = input("Enter a date (MM/DD/YYYY): ")

try:
    month, day, year = map(int, date_input.split('/'))
    if not (1 <= month <= 12):
        raise ValueError("Invalid month")
    if not (1 <= day <= 31): 
        raise ValueError("Invalid day")

    day_of_week = get_day(month, day, year)
    print(f"The day of the week is: {day_of_week}")
except ValueError as e:
    print(f"Invalid input: {e}")
