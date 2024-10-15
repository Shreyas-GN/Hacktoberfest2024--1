# For Loop Example
print("Counting to 5 using a for loop:")

# The for loop runs a set number of times, defined by the range function.
# range(1, 6) generates numbers from 1 to 5 (inclusive of 1, exclusive of 6).
for i in range(1, 6):  
    print(f"For loop iteration {i}: Number = {i}")

# Adding a separator for better readability
print("\n--------------------------\n")

# While Loop Example
print("Counting to 5 using a while loop:")

# The while loop will keep running as long as the condition (count <= 5) is True.
count = 1  # Start count at 1
while count <= 5:
    print(f"While loop iteration {count}: Number = {count}")
    count += 1  # Increment count to ensure the loop ends after 5 iterations.

# Once the condition count > 5 is met, the loop will stop.
print("\nWhile loop has ended.")
