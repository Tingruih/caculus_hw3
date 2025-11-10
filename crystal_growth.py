import math

def get_temperature(power):
    temperature = 0.1 * power ** 2 + 2.155 * power + 20
    # TODO: Compute the temperature according to the equation T(w) = 0.1w^2 + 2.155w + 20
    return temperature

def solve_power(temperature):
    power = 0

    a = 0.1
    b = 2.155
    c = 20 - temperature
    
    discriminant = b**2 - 4*a*c
    if discriminant >= 0:
        sqrt_d = math.sqrt(discriminant)
        root1 = (-b + sqrt_d) / (2*a)
        root2 = (-b - sqrt_d) / (2*a)
        power = max(root1, root2)  # only return the positive root

    #TODO: Solves the equation T(w) = 0.1w^2 + 2.155w + 20 for a given temperature.
    #Note: Only return the positive root

    return power
