# Your Name
# ITELEC2
# Laboratory #06 – Utilizing Basic Math Libraries in Python

import math  # Import the math module

# 1️⃣ Calculate the square root of 16
number = 16
sqrt_result = math.sqrt(number)

# 2️⃣ Get the value of π (pi)
pi_value = math.pi

# 3️⃣ Calculate the sine of 30 degrees (converted to radians)
angle_degrees = 30
angle_radians = math.radians(angle_degrees)
sin_result = math.sin(angle_radians)

# 4️⃣ Calculate the cosine of 60 degrees (converted to radians)
angle_degrees_cos = 60
angle_radians_cos = math.radians(angle_degrees_cos)
cos_result = math.cos(angle_radians_cos)

# 5️⃣ Calculate the tangent of 45 degrees (converted to radians)
angle_degrees_tan = 45
angle_radians_tan = math.radians(angle_degrees_tan)
tan_result = math.tan(angle_radians_tan)

# 6️⃣ Calculate exponential of 2 (e^2)
exp_result = math.exp(2)

# 7️⃣ Calculate logarithms
log_result = math.log(10)  # Natural log (base e)
log10_result = math.log(100, 10)  # Log base 10

# 8️⃣ Print the results
print("Square root of", number, "is:", sqrt_result)
print("Value of pi is:", pi_value)
print("Sine of 30 degrees (in radians) is:", sin_result)
print("Cosine of 60 degrees (in radians) is:", cos_result)
print("Tangent of 45 degrees (in radians) is:", tan_result)
print("Exponential of 2 is:", exp_result)
print("Logarithm (base e) of 10 is:", log_result)
print("Logarithm (base 10) of 100 is:", log10_result)