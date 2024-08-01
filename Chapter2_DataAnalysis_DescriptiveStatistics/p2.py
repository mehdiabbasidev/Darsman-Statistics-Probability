import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

data = [1, 2, 5, 5, 7, 2, 3, 4, 2, 4, 1, 9]   # [1,1,2,2,2,3,4,4,5,5,7,9]
x_values = np.arange(len(data))  
data2 = [3, 7, 2, 6, 1, 4, 7, 6, 1, 3,2, 1]   # [1,1,2,2,2,3,4,4,5,5,7,9]
x_values2 = np.arange(len(data))  
plt.figure(figsize=(13, 6))  
plt.plot(x_values, data, marker='o', linestyle='-', color='blue', label='Data')
plt.plot(x_values2, data2, marker='o', linestyle='-', color='green', label='Data')
plt.xticks(x_values) 
plt.xlabel('Index')
plt.ylabel('Values')
plt.title('Line Plot of Data')
plt.legend()
plt.tight_layout()  
plt.show()



#### محاسبه میانگین
# mean_value = np.mean(data)  
# plt.axhline(mean_value, color='red', linestyle='dashed', linewidth=1, label='Mean')
# plt.text(x_values[-1] + 1, mean_value, f'Mean: {mean_value:.2f}', color='red', verticalalignment='center')


#### محاسبه میانه
# median_value = np.median(data)  
# plt.axhline(median_value, color='green', linestyle='dashed', linewidth=1, label='Median')
# plt.text(x_values[-1] + 1, median_value, f'Median: {median_value}', color='green', verticalalignment='center')


#### محاسبه مد
# mode_value = stats.mode(data).mode[0]  
# plt.axhline(mode_value, color='purple', linestyle='dashed', linewidth=1, label='Mode')
# plt.text(x_values[-1] + 1, mode_value, f'Mode: {mode_value}', color='purple', verticalalignment='center')


#### محاسبه واریانس
# variance_value = np.var(data)  
# plt.axhline(variance_value, color='orange', linestyle='dashed', linewidth=1, label='Variance')
# plt.text(x_values[-1] + 1, variance_value, f'Variance: {variance_value:.2f}', color='orange', verticalalignment='center')


#### محاسبه انحراف معیار
# std_deviation_value = np.std(data)  
# plt.axhline(std_deviation_value, color='brown', linestyle='dashed', linewidth=1, label='Std Deviation')
# plt.text(x_values[-1] + 1, std_deviation_value, f'Std Dev: {std_deviation_value:.2f}', color='brown', verticalalignment='center')


#### محاسبه محدوده
# data_range = np.ptp(data)  
# plt.axhline(data_range, color='black', linestyle='dashed', linewidth=1, label='data_range')
# plt.text(x_values[-1] + 1, data_range, f'Range: {data_range}', color='black', verticalalignment='center')


# #### محاسبه صدک‌ها
# percentiles = np.percentile(data, [10, 40, 70,90]) 
# plt.axhline(percentiles[0], color='magenta', linestyle='dashed', linewidth=1, label='percentiles[0]')
# plt.axhline(percentiles[1], color='cyan', linestyle='dashed', linewidth=1, label='percentiles[1]')
# plt.axhline(percentiles[2], color='blue', linestyle='dashed', linewidth=1, label='percentiles[2]')
# plt.axhline(percentiles[3], color='green', linestyle='dashed', linewidth=1, label='percentiles[3]')
# plt.text(x_values[-1] + 1, percentiles[0], f'25th Percentile: {percentiles[0]}', color='magenta', verticalalignment='center')
# plt.text(x_values[-1] + 1, percentiles[1], f'50th Percentile: {percentiles[1]}', color='cyan', verticalalignment='center')
# plt.text(x_values[-1] + 1, percentiles[2], f'75th Percentile: {percentiles[2]}', color='blue', verticalalignment='center')
# plt.text(x_values[-1] + 1, percentiles[3], f'100th Percentile: {percentiles[3]}', color='green', verticalalignment='center')


#### محاسبه چارک‌ها
# quartiles = np.percentile(data, [25, 50, 75])  
# plt.axhline(quartiles[0], color='purple', linestyle='dashed', linewidth=1, label='quartiles[0]')
# plt.axhline(quartiles[1], color='blue', linestyle='dashed', linewidth=1,   label='quartiles[1]')
# plt.axhline(quartiles[2], color='green', linestyle='dashed', linewidth=1,  label='quartiles[2]')
# plt.text(x_values[-1] + 1, quartiles[0], f'Q1 (25th Quartile): {quartiles[0]}', color='purple', verticalalignment='center')
# plt.text(x_values[-1] + 1, quartiles[1], f'Q2 (50th Quartile): {quartiles[1]}', color='blue', verticalalignment='center')
# plt.text(x_values[-1] + 1, quartiles[2], f'Q3 (75th Quartile): {quartiles[2]}', color='green', verticalalignment='center')


#### محدوده بین‌چارکی (IQR)
# q1 = np.percentile(data, 25)  # چارک اول (25th percentile)
# q3 = np.percentile(data, 75)  # چارک سوم (75th percentile)
# iqr = q3 - q1 
# plt.axhline(iqr, color='pink', linestyle='dashed', linewidth=1, label='IQR')
# plt.text(x_values[-1] + 1, iqr, f'IQR: {iqr}', color='pink', verticalalignment='center')



# plt.xticks(x_values) 
# plt.xlabel('Index')
# plt.ylabel('Values')
# plt.title('Line Plot of Data')
# plt.legend()
# plt.tight_layout()  
# plt.show()



