import math

# Square root of 16
number = 16
sqrt_result = math.sqrt(number)

# Value of pi
pi_value = math.pi

# Sine of 30 degrees
sin_angle_degrees = 30
sin_angle_radians = math.radians(sin_angle_degrees)
sin_result = math.sin(sin_angle_radians)

# Cosine of 60 degrees
cos_angle_degrees = 60
cos_angle_radians = math.radians(cos_angle_degrees)
cos_result = math.cos(cos_angle_radians)

# Tangent of 30 degrees (Fixing from 45 degrees)
tan_angle_degrees = 30
tan_angle_radians = math.radians(tan_angle_degrees)
tan_result = math.tan(tan_angle_radians)

# Exponential of 2
exp_result = math.exp(2)

# Logarithm (base e) of 10
log_result = math.log(10)

# Logarithm (base 10) of 100
log10_result = math.log(100, 10)

# Display output
print("Square root of", number, "is:", sqrt_result)
print("Value of pi is:", pi_value)
print("Sine of 30 degrees (in radians) is:", sin_result)
print("Cosine of 60 degrees (in radians) is:", cos_result)
print("Tangent of 45 degrees (in radians) is:", tan_result)
print("Exponential of 2 is:", exp_result)
print("Logarithm (base e) of 10 is:", log_result)
print("Logarithm (base 10) of 100 is:", log10_result)