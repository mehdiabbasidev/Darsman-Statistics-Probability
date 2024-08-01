#### P(X<1000)=?
# import numpy as np
# import scipy.stats as stats
# import math

# weights = [1022, 1003, 998, 1006, 1012, 989]
# mean = np.mean(weights)                 # mean = sum(weights) / len(weights)
# variance = np.var(weights)              # variance = sum((x - mean) ** 2 for x in weights) / (len(weights) )
# std_deviation=math.sqrt(variance)
# print(f"mean : {mean}")
# print(f"variance : {variance}")
# print(f"std_deviation : {std_deviation}")

# dw = 1000
# prob = stats.norm.cdf(dw, loc=mean, scale=std_deviation)
# print(f"P(X<{dw}) : {prob:.4f}")








#### P(998<X<1015)=?
from scipy import stats
import numpy as np

weights = [1022, 1003, 998, 1006, 1012, 989]

mean = np.mean(weights)
variance = np.var(weights)
std_deviation=np.sqrt(variance)
print(f"mean : {mean}")
print(f"variance : {variance}")
print(f"std_deviation : {std_deviation}")

lower_bound = 998
upper_bound = 1015
prob_upper_bound=stats.norm.cdf(upper_bound, loc=mean, scale=std_deviation)
prob_lower_bound=stats.norm.cdf(lower_bound, loc=mean, scale=std_deviation)
prob =prob_upper_bound  - prob_lower_bound
print(f"P({lower_bound}<X<{upper_bound}) : {prob:.4}")
