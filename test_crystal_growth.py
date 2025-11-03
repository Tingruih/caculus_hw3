import numpy as np
import matplotlib.pyplot as plt
from crystal_growth import *

def viz_limit(target_temperature, eps, target_power, delta, power_range):
    min_power = power_range[0]
    max_power = power_range[1]

    w_values = np.linspace(min_power, max_power, 500)
    T_values = np.array([get_temperature(w_value) for w_value in w_values])
    
    # Begin plotting
    plt.figure(figsize=(10, 6))
    plt.plot(w_values, T_values, label='T(w) = 0.1w² + 2.155w + 20', color='black')
    
    # Plot point at T=200
    plt.scatter([target_power], [target_temperature], color='black', zorder=5)
    plt.axhline(y=target_temperature, color='gray', linestyle='--')  # Horizontal line at T=target_temperature
    plt.axvline(x=target_power, color='gray', linestyle='--')  # Vertical line at target_power
    plt.text(target_power + 0.1, target_temperature + 0.1, f"w = {target_power:.3f}", fontsize=9)
    
    # Plot horizontal lines as epsilon bounds
    # TODO: modify y_high and y_low to plot the correct lines
    y_high = target_temperature
    y_low = target_temperature
    plt.axhline(y=y_high, color='red', linestyle='-', label='eps bounds')
    plt.axhline(y=y_low, color='red', linestyle='-')
    plt.vlines(target_power, y_low, y_high, color='red', linestyle='dashed')
    plt.text(power_range[0]+0.2, y_high+1,
            f"T = {target_temperature:.3f} + {eps:.3f}", color='red', fontsize=9, va='bottom')

    plt.text(power_range[0]+0.2, y_low-1,
            f"T = {target_temperature:.3f} - {eps:.3f}", color='red', fontsize=9, va='top')
    
    # Plot vertical lines as delta bounds
    # TODO: modify x_left and x_right to plot the correct lines
    x_left = target_power
    x_right = target_power
    plt.axvline(x=x_left, color='blue', linestyle='-', label='delta bounds')
    plt.axvline(x=x_right, color='blue', linestyle='-')
    plt.hlines(target_temperature, x_left, x_right, color='blue', linestyle='dashed')
    min_temperature = get_temperature(min_power)
    plt.text(x_right+0.05, min_temperature+1,
            f"T = {target_power:.3f} + {delta:.3f}", color='blue', fontsize=9)

    plt.text(x_left-0.7, min_temperature+1,
            f"T = {target_power:.3f} - {delta:.3f}", color='blue', fontsize=9)
    
    # Labels and title
    plt.title("Crystal Growth Temperature Control")
    plt.xlabel("Power Input (w)")
    plt.ylabel("Temperature T(w)")
    plt.grid(True)
    plt.legend()
    plt.savefig("limit.png", dpi=300, bbox_inches='tight')
    plt.close()  # Close the figure to free memory
    
# Solve powers
# TODO: Report and explain the meaning of the solved powers
target_temperature = 200
eps = 1
target_power = solve_power(target_temperature)
higher_power = solve_power(target_temperature+eps)
lower_power = solve_power(target_temperature-eps)

delta=0
# TODO: Update delta of the power so that the temperature is within an error tolerance epsilon = 1 at 200
# Note: Please see the meanning of delta in the precise definition of the limit. 

# Set power range for plotting
power_range = [target_power-2, target_power+2]

# Draw the graph
viz_limit(target_temperature, eps, target_power, delta, power_range)

