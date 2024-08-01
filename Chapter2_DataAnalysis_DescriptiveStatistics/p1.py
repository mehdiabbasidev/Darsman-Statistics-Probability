import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

data = [1, 2, 5, 5, 7, 2, 3, 4, 2, 4, 1, 9]
sorted_data = sorted(data)  # مرتب‌سازی داده‌ها


mean_value = np.mean(data)  # محاسبه میانگین
median_value = np.median(data)  # محاسبه میانه
mode_value = stats.mode(data).mode[0]  # محاسبه مد
variance_value = np.var(data)  # محاسبه واریانس
std_deviation_value = np.std(data)  # محاسبه انحراف معیار
data_range = np.ptp(data)  # محاسبه محدوده
percentiles = np.percentile(data, [10, 40, 70,90])  # محاسبه صدک‌ها
quartiles = np.percentile(data, [25, 50, 75])  # محاسبه چارک‌ها
q1 = np.percentile(data, 25)  # چارک اول (25th percentile)
q3 = np.percentile(data, 75)  # چارک سوم (75th percentile)
iqr = q3 - q1  # محدوده بین‌چارکی (IQR)

print(80*"*")
print("sorted_data : \t\t",sorted_data)
print("mean_value : \t\t",mean_value)
print("median_value: \t\t",median_value)
print("mode_value : \t\t",mode_value)
print("variance_value : \t",variance_value)
print("std_deviation_value : \t",std_deviation_value)
print("data_range : \t\t",data_range)
print("percentiles : \t\t",percentiles)
print("quartiles : \t\t",quartiles)
print("IQR : \t\t\t", iqr)
print(80*"*")