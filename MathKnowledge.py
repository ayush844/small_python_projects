import math

#########################################################################################################################

# Built-in Basic Math Functions (No import math Required):


#Here are good examples for each of the specified built-in math functions:



### **1. `abs(x): Returns the absolute value of x`**

# Example 1: Absolute value of a positive number
print(abs(10))  # Output: 10
# Example 2: Absolute value of a negative number
print(abs(-15.5))  # Output: 15.5



### **2. `round(x, n): Rounds x to n decimal places`**

# Example 1: Rounding a number to no decimal places
print(round(5.678))  # Output: 6
# Example 2: Rounding a number to 2 decimal places
print(round(3.14159, 2))  # Output: 3.14



### **3. `pow(x, y): Returns x raised to the power of y`**

# Example 1: Integer exponent
print(pow(2, 3))  # Output: 8 (2^3)
# Example 2: Floating-point exponent
print(pow(5, 0.5))  # Output: 2.23606797749979 (Square root of 5)



### **4. `divmod(x, y): Returns a tuple (quotient, remainder) of x divided by y`**

# Example: Using divmod to calculate quotient and remainder
quotient, remainder = divmod(17, 5)
print(f"Quotient: {quotient}, Remainder: {remainder}")  
# Output: Quotient: 3, Remainder: 2



### **5. `sum(iterable, start=0): Returns the sum of all items in an iterable, optionally starting with start`**

# Example 1: Summing numbers in a list
print(sum([1, 2, 3, 4]))  # Output: 10
# Example 2: Using a starting value
print(sum([1, 2, 3, 4], start=10))  # Output: 20



### **6. `min(iterable, *args, key=None): Returns the smallest item in an iterable or among two or more arguments`**

# Example 1: Finding the minimum in a list
print(min([4, 7, 1, 9]))  # Output: 1
# Example 2: Finding the minimum among multiple arguments
print(min(4, 7, 1, 9))  # Output: 1
# Example 3: Using the `key` parameter (e.g., based on string length)
words = ["apple", "banana", "kiwi"]
print(min(words, key=len))  # Output: kiwi (shortest word)



### **7. `max(iterable, *args, key=None): Returns the largest item in an iterable or among two or more arguments`**

# Example 1: Finding the maximum in a list
print(max([4, 7, 1, 9]))  # Output: 9
# Example 2: Finding the maximum among multiple arguments
print(max(4, 7, 1, 9))  # Output: 9
# Example 3: Using the `key` parameter (e.g., based on string length)
words = ["apple", "banana", "kiwi"]
print(max(words, key=len))  # Output: banana (longest word)



#These examples illustrate how to use these functions effectively in various scenarios. Let me know if you want to dive deeper into any of these!



#########################################################################################################################


# Math Module Functions (Require import math):


# Here are examples of some of the most famous and frequently used functions from Python's `math` module:


### **1. `math.sqrt(x): Returns the square root of x`**

# Example: Calculate the square root of a number
result = math.sqrt(25)
print(result)  # Output: 5.0



### **2. `math.factorial(x): Returns the factorial of x`**

# Example: Calculate the factorial of a number
result = math.factorial(5)
print(result)  # Output: 120 (5! = 5 * 4 * 3 * 2 * 1)



### **3. `math.pow(x, y): Returns x raised to the power of y`**

# Example: Calculate powers using math.pow
result = math.pow(3, 4)
print(result)  # Output: 81.0



### **4. `math.log(x, base): Returns the logarithm of x with the specified base`**

# Example: Calculate logarithm with base 10
log_base10 = math.log(1000, 10)
print(log_base10)  # Output: 3.0

# Example: Natural logarithm (base e)
log_base_e = math.log(20)
print(log_base_e)  # Output: 2.995732273553991



### **5. `math.ceil(x): Returns the smallest integer greater than or equal to x`**

# Example: Round up a floating-point number
result = math.ceil(4.2)
print(result)  # Output: 5



### **6. `math.floor(x): Returns the largest integer less than or equal to x`**

# Example: Round down a floating-point number
result = math.floor(4.8)
print(result)  # Output: 4



### **7. `math.pi`: The constant π (pi)**

# Example: Calculate the circumference of a circle
radius = 5
circumference = 2 * math.pi * radius
print(circumference)  # Output: 31.41592653589793



### **8. `math.e`: The constant e**

# Example: Exponential growth calculation
result = math.e ** 2
print(result)  # Output: 7.38905609893065



### **9. `math.sin(x), math.cos(x), math.tan(x): Trigonometric functions`**

# Example: Calculate sine, cosine, and tangent of an angle (in radians)
angle = math.pi / 4  # 45 degrees in radians
sin_value = math.sin(angle)
cos_value = math.cos(angle)
tan_value = math.tan(angle)

print(sin_value)  # Output: 0.7071067811865475
print(cos_value)  # Output: 0.7071067811865476
print(tan_value)  # Output: 1.0



### **10. `math.hypot(x, y): Returns the Euclidean norm (\(\sqrt{x^2 + y^2}\))`**

# Example: Calculate the length of the hypotenuse
result = math.hypot(3, 4)
print(result)  # Output: 5.0 (3-4-5 triangle)



### **11. `math.isclose(a, b): Checks if two numbers are approximately equal`**

# Example: Comparing floating-point numbers
a = 0.1 + 0.2
b = 0.3
result = math.isclose(a, b)
print(result)  # Output: True



### **12. `math.degrees(x)` and `math.radians(x)`: Convert between radians and degrees**

# Example: Convert radians to degrees
degrees = math.degrees(math.pi / 4)
print(degrees)  # Output: 45.0

# Example: Convert degrees to radians
radians = math.radians(90)
print(radians)  # Output: 1.5707963267948966



### **13. `math.gcd(a, b): Returns the greatest common divisor of a and b`**

# Example: Find the greatest common divisor
result = math.gcd(56, 98)
print(result)  # Output: 14



# These examples demonstrate practical use cases of the most popular functions from the `math` module. Let me know if you'd like to explore specific ones further!