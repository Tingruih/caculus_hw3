import numpy as np
import matplotlib.pyplot as plt
from crystal_growth import *

def viz_limit(target_temperature, eps, target_power, delta, power_range):
    min_power = power_range[0]
    max_power = power_range[1]

    w_values = np.linspace(min_power, max_power, 500) # 在功率範圍內取 500 個點

    T_values = np.array([get_temperature(w_value) for w_value in w_values]) # 計算每個功率對應的溫度
    
    # Begin plotting
    plt.figure(figsize=(10, 6)) # 設定圖片大小
    plt.plot(w_values, T_values, label='T(w) = 0.1w² + 2.155w + 20', color='black') 
    # 畫橫軸w_values、縱軸T_values、設定圖形標籤T(w) = 0.1w² + 2.155w + 20、設定顏色為黑色
    # Plot point at T=200
    plt.scatter([target_power], [target_temperature], color='black', zorder=5)
    # 在(x, y) = (target_power, target_temperature)劃一個黑點
    plt.axhline(y=target_temperature, color='gray', linestyle='--')  # Horizontal line at T=target_temperature
    plt.axvline(x=target_power, color='gray', linestyle='--')  # Vertical line at target_power
    plt.text(target_power + 0.1, target_temperature + 0.1, f"w = {target_power:.3f}", fontsize=9)
    #在點(x, y) = (target_power, target_temperature)上方 0.1 的地方寫出文字target_power(小數點後三位)並設定大小 9
    
    # Plot horizontal lines as epsilon bounds
    # TODO: modify y_high and y_low to plot the correct lines
    y_high = target_temperature + eps
    y_low = target_temperature - eps # 溫度在 eps 範圍內的上下界
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
    delta = max(abs(target_power - lower_power), abs(higher_power ))
    # 計算在溫度誤差範圍 1 內時，功率的最大偏差(delta)
    plt.axvline(x=x_left, color='blue', linestyle='-', label='delta bounds')
    plt.axvline(x=x_right, color='blue', linestyle='-')
    plt.hlines(target_temperature, x_left, x_right, color='blue', linestyle='dashed')
    min_temperature = get_temperature(min_power)
    plt.text(x_right+0.05, min_temperature+1,
            f"T = {target_power:.3f} + {delta:.3f}", color='blue', fontsize=9)

    plt.text(x_left-0.7, min_temperature+1,
            f"T = {target_power:.3f} - {delta:.3f}", color='blue', fontsize=9)
    
    # Labels and title
    plt.title("Crystal Growth Temperature Control") # 設定標題名稱
    plt.xlabel("Power Input (w)") # X 座標設為 w
    plt.ylabel("Temperature T(w)") # Y座標設為 T
    plt.grid(True) # 加上格線
    plt.legend() # 顯示圖例標籤
    plt.savefig("limit.png", dpi=300, bbox_inches='tight') # 儲存為 limit.png
    plt.close()  # Close the figure to free memory
    
# Solve powers
# TODO: Report and explain the meaning of the solved powers
target_temperature = 200
eps = 1
target_power = solve_power(target_temperature)
higher_power = solve_power(target_temperature+eps)
lower_power = solve_power(target_temperature-eps)# 描寫溫度的誤差(eps)範圍

delta = max(abs(higher_power - target_power), abs(lower_power - target_power))# 溫度在誤差 1 的範圍內，功率的最大偏差值就是要的 delta
# TODO: Update delta of the power so that the temperature is within an error tolerance epsilon = 1 at 200
# Note: Please see the meanning of delta in the precise definition of the limit. 


# Set power range for plotting
power_range = [target_power-2, target_power+2]# 設定功率範圍


# Draw the graph
viz_limit(target_temperature, eps, target_power, delta, power_range)# 畫出eps delta圖

