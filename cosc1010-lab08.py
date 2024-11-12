# Talon Bluemel
# UWYO COSC 1010
# 11-11-24
# Lab 8
# Lab Section:12
# Sources, people worked with, help given to: I had to look up a way to do the square root operation because I had no idea what I was doing. https://www.geeksforgeeks.org/find-root-of-a-number-using-newtons-method/.
#I also had to run the code through ChatGPT several times to help me troubleshoot errors.

# Write a function that will properly check strings to see if they are an int or float, and convert them if so
# If they can't be converted return false
# Other wise return the converted int or float 
# Floats should only have one decimal point in them 
def convert(s):
    try:
        return int(s)
    except ValueError:
        try:
            if '.' in s and s.count('.') == 1 and len(s.split('.')[1]) <= 1:
                return float(s)
            else:
                return False
        except ValueError:
            return False


print("*" * 75)


# Point-slope y = mx + b
# This is used in mathematics to determine what the value y would be for any given x
# Where b is the y-intercept, where the line crosses the y-axis (x = 0)
# m is the slope of the line, the rate of change, how steep the line is
# x is the variable, and is determined by which point on the graph you wish to evaluate
# Create a function slope_intercept that takes in four parameters
    # m, the slope
    # b, the intercept
    # a lower x bound
    # an upper x bound
# Return a list for all values of y for the given x range, inclusive (whole number X's only)
# Check to make sure that the lower bound is less than or equal to the upper bound
# m, b can be floats or integers
# the bounds must be integers, if not return false
def slope_intercept(m, b, lower_x, upper_x):
    if not isinstance(lower_x, int) or not isinstance(upper_x, int):
        return False
    
    if lower_x > upper_x:
        return False

    y_values = []
    for x in range(lower_x, upper_x + 1):
        y = m * x + b
        y_values.append(y)
    return y_values
# Create a while loop to prompt users for their input for the four variables
# Exit on the word exit
# Remember all inputs are strings, but the function needs ints or floats
# Call your function and print the resulting list
def slope_intercept(m, b, lower_x, upper_x):
    # Check if lower_x and upper_x are integers
    if not isinstance(lower_x, int) or not isinstance(upper_x, int):
        return False
    
    # Check if the lower bound is less than or equal to the upper bound
    if lower_x > upper_x:
        return False
    
    # Calculate the y-values for each integer x in the range [lower_x, upper_x]
    y_values = []
    for x in range(lower_x, upper_x + 1):
        y = m * x + b
        y_values.append(y)
    
    return y_values

def get_input():
    while True:
        m_input = input("Enter the slope (m), or type 'exit' to quit: ")
        if m_input.lower() == 'exit':
            break
        
        b_input = input("Enter the intercept (b): ")
        if b_input.lower() == 'exit':
            break
        
        lower_x_input = input("Enter the lower x bound: ")
        if lower_x_input.lower() == 'exit':
            break
        
        upper_x_input = input("Enter the upper x bound: ")
        if upper_x_input.lower() == 'exit':
            break

        try:
            m = float(m_input)
            b = float(b_input)
            lower_x = int(lower_x_input)
            upper_x = int(upper_x_input)

            result = slope_intercept(m, b, lower_x, upper_x)
            if result is False:
                print("Invalid input or bounds. Please try again.")
            else:
                print("Resulting y-values: ", result)
        except ValueError:
            print("Invalid input. Please enter numeric values for the slope, intercept, and bounds.")        
get_input()

print("*" * 75)
# Write a function to solve the quadratic formula
# https://en.wikipedia.org/wiki/Quadratic_formula
# Accept inputs for a, b, c
# Remember that this returns two values
# Create a loop like above to prompt the user for input for the three values
# Create a second function that just does the square root operation 
    # If the number you are trying to take the square root of is negative, return null
# Function to safely perform the square root operation using Newton's method
def safe_sqrt(value, tolerance=1e-10):
    if value < 0:
        return None

    guess = value

    while True:
   
        better_guess = 0.5 * (guess + value / guess)

        if abs(better_guess - guess) < tolerance:
            return better_guess
        guess = better_guess

def quadratic_formula(a, b, c):

    discriminant = b**2 - 4 * a * c
    sqrt_discriminant = safe_sqrt(discriminant)

    if sqrt_discriminant is None:
        return None
    
    root1 = (-b + sqrt_discriminant) / (2 * a)
    root2 = (-b - sqrt_discriminant) / (2 * a)
    
    return root1, root2

def get_quadratic_input():
    while True:
        a_input = input("Enter the coefficient a, or type 'exit' to quit: ")
        if a_input.lower() == 'exit':
            break
        
        b_input = input("Enter the coefficient b: ")
        if b_input.lower() == 'exit':
            break
        
        c_input = input("Enter the coefficient c: ")
        if c_input.lower() == 'exit':
            break

        try:
            a = float(a_input)
            b = float(b_input)
            c = float(c_input)
            if a == 0:
                print("Coefficient 'a' cannot be zero in a quadratic equation.")
                continue
            result = quadratic_formula(a, b, c)
            if result is None:
                print("No real solutions (discriminant is negative).")
            else:
                root1, root2 = result
                print(f"The solutions are: {root1} and {root2}")
        except ValueError:
            print("Invalid input. Please enter numeric values for a, b, and c.")
get_quadratic_input()