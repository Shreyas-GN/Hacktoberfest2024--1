# If statements allow you to make decisions in your program.
# You can check conditions, like whether a number is greater than, less than, or equal to another number.

age = int(input("Enter your age: "))  # We use int() to convert the input from a string to an integer.

if age >= 18:
    print("You are an adult.")  # This block runs if the condition is True (age is 18 or more).
else:
    print("You are a minor.")   # This block runs if the condition is False (age is less than 18).
