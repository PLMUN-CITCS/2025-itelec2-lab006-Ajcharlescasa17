import math

# Step 3: Calculate the square root of 16
number = 16
sqrt_result = math.sqrt(number)

# Step 4: Get the value of pi
pi_value = math.pi

# Step 5: Calculate the sine of 30 degrees (convert to radians)
sin_angle_degrees = 30
sin_angle_radians = math.radians(sin_angle_degrees)
sin_result = math.sin(sin_angle_radians)

# Step 6: Calculate the cosine of 60 degrees (convert to radians)
cos_angle_degrees = 60
cos_angle_radians = math.radians(cos_angle_degrees)
cos_result = math.cos(cos_angle_radians)

# Step 6: Calculate the tangent of 45 degrees (convert to radians)
tan_angle_degrees = 45
tan_angle_radians = math.radians(tan_angle_degrees)
tan_result = math.tan(tan_angle_radians)

# Step 7: Calculate the exponential and logarithms
exp_result = math.exp(2)  # e^2
log_result = math.log(10)  # Natural log (base e)
log10_result = math.log(100, 10)  # Log base 10 of 100

# Step 8: Display the results
print("Square root of", number, "is:", sqrt_result)
print("Value of pi is:", pi_value)
print("Sine of 30 degrees (in radians) is:", sin_result)
print("Cosine of 60 degrees (in radians) is:", cos_result)
print("Tangent of 45 degrees (in radians) is:", tan_result)
print("Exponential of 2 is:", exp_result)
print("Logarithm (base e) of 10 is:", log_result)
print("Logarithm (base 10) of 100 is:", log10_result)