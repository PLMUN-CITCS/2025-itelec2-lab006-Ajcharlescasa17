# Import the math module
import math

# Step 3: Calculate the square root
number = 16
sqrt_result = math.sqrt(number)

# Step 4: Get the value of pi
pi_value = math.pi

# Step 5: Calculate the sine of an angle
angle_30_degrees = 30
angle_30_radians = math.radians(angle_30_degrees)
sin_result = math.sin(angle_30_radians)

# Step 6: Calculate the cosine and tangent of angles
cos_result = math.cos(math.radians(60))  # Cosine of 60 degrees
tan_result = math.tan(math.radians(30))  # Tangent of 30 degrees (not 45)

# Step 7: Calculate the exponential and logarithms
exp_result = math.exp(2)  # e^2
log_result = math.log(10)  # Natural log (base e) of 10
log10_result = math.log(100, 10)  # Log base 10 of 100

# Step 8: Display the results with proper formatting
print(f"Square root of {number} is: {sqrt_result}")
print(f"Value of pi is: {pi_value}")
print(f"Sine of 30 degrees (in radians) is: {sin_result}")
print(f"Cosine of 60 degrees (in radians) is: {cos_result}")
print(f"Tangent of 30 degrees (in radians) is: {tan_result}")
print(f"Exponential of 2 is: {exp_result}")
print(f"Logarithm (base e) of 10 is: {log_result}")
print(f"Logarithm (base 10) of 100 is: {log10_result}")