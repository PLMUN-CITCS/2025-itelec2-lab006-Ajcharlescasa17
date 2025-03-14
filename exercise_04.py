# Import the math module
import math

# Calculate the square root of 16
number = 16
sqrt_result = math.sqrt(number)

# Get the value of pi
pi_value = math.pi

# Calculate the sine of 30 degrees
angle_degrees = 30
angle_radians = math.radians(angle_degrees)  # Convert degrees to radians
sin_result = round(math.sin(angle_radians), 15)  # Round to match expected precision

# Calculate the cosine of 60 degrees
cos_result = round(math.cos(math.radians(60)), 15)  # Fixed: Cosine of 60 degrees

# Calculate the tangent of 45 degrees
tan_result = round(math.tan(math.radians(45)), 15)  # Fixed: Tangent of 45 degrees

# Calculate the exponential of 2
exp_result = round(math.exp(2), 15)

# Calculate logarithms
log_result = round(math.log(10), 15)  # Natural log (base e)
log10_result = round(math.log(100, 10), 15)  # Log base 10

# Display the results (Ensure exact formatting)
print("Square root of", number, "is:", sqrt_result)
print("Value of pi is:", pi_value)
print("Sine of 30 degrees (in radians) is:", sin_result)
print("Cosine of 60 degrees (in radians) is:", cos_result)
print("Tangent of 45 degrees (in radians) is:", tan_result)
print("Exponential of 2 is:", exp_result)
print("Logarithm (base e) of 10 is:", log_result)
print("Logarithm (base 10) of 100 is:", log10_result)