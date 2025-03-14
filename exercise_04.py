import math

# Calculate the square root
number = 16
sqrt_result = math.sqrt(number)

# Get the value of pi
pi_value = math.pi

# Convert degrees to radians and calculate trigonometric functions
angle_30_degrees = 30
angle_60_degrees = 60
angle_45_degrees = 45

angle_30_radians = math.radians(angle_30_degrees)
angle_60_radians = math.radians(angle_60_degrees)
angle_45_radians = math.radians(angle_45_degrees)

sin_result = math.sin(angle_30_radians)
cos_result = math.cos(angle_60_radians)
tan_result = math.tan(angle_45_radians)

# Calculate exponential and logarithms
exp_result = math.exp(2)
log_result = math.log(10)  # Natural log (base e)
log10_result = math.log(100, 10)  # Log base 10

# Display results
print("Square root of", number, "is:", sqrt_result)
print("Value of pi is:", pi_value)
print("Sine of 30 degrees (in radians) is:", sin_result)
print("Cosine of 60 degrees (in radians) is:", cos_result)
print("Tangent of 45 degrees (in radians) is:", tan_result)
print("Exponential of 2 is:", exp_result)
print("Logarithm (base e) of 10 is:", log_result)
print("Logarithm (base 10) of 100 is:", log10_result)