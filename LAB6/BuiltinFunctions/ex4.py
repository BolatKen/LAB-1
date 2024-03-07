import time
import math

def calculate_square_root(number, milliseconds):
    time.sleep(milliseconds / 1000)  
    result = math.sqrt(number)
    return result

# Sample input
number = int(input())
milliseconds = int(input())

# Invoke square root function after specific milliseconds
result = calculate_square_root(number, milliseconds)
print(f"Square root of {number} after {milliseconds} milliseconds is {result}")
