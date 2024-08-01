# SciPy محاسبه مقدار پی با استفاده از توزیع نرمال در 
from scipy.stats import norm

p_value = norm.cdf(1.96) - norm.cdf(-1.96)
print("p-value:", p_value)
