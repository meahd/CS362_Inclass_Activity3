# Calculator App
# David Meah - CS362 - 2/4/2021

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if (b == 0):
        print("Can't divide by 0")
    else:
        return a / b

#Input validation function
def floatInputValidation(user_input):
    while True: #Loops till right input is entered
        try:
            tempVal = float(input(user_input))
        except ValueError:
            print("Error: Invalid Input")
            print("Try again")
            continue
        else:
            return tempVal #If not ValueErrors then break out of loop
            break

# Main
print("= Simple Calculator Application =")

a = floatInputValidation("1st input: ")
b = floatInputValidation("2nd input: ")

print(a, "+", b, "=", add(a, b))
print(a, "-", b, "=", subtract(a, b))
print(a, "*", b, "=", multiply(a, b))
print(a, "/", b, "=", divide(a, b))
