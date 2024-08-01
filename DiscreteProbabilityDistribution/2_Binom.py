#بذر یک گیاه به احتمال 80 درصد جوانه می‌زند، 7 بذر را کاشته ایم
# import scipy.stats as stats
# n = 7
# p = 0.8

# x = 4
# prob = stats.binom.pmf(x, n, p)
# print(f"P(X=4) : {prob:.4f}")

# print(100*"*")


# n = 7
# p = 0.8
# x_values = [6,7]
# sum_prob=0
# for x in x_values:
#     prob = stats.binom.pmf(x, n, p)
#     print(f"P(X={x}) : {prob:.4f}")
#     sum_prob+=prob
# print(f"P(X>5) : {sum_prob:.4f}")




#----------------------------------------------------------------------------------------
#فوتبالیستی باید در  یک فصل 12 پنالتی بزند، سابقه این فوتبالیست نشان می‌دهد که 75 درصد پنالتی هایش گل می‌شود
# import scipy.stats as stats

# n = 12
# p = 0.75
# x_values = [10,11,12]

# sum_prob=0
# for x in x_values:
#     sum_prob+=stats.binom.pmf(x, n, p)
    
# print(f"P(X>=10) : {sum_prob:.4f}")


import scipy.stats as stats
import math

n = 12
p = 0.75
expected_value = stats.binom.mean(n, p)
print(f"E(x): {expected_value:.2f}")

variance = stats.binom.var(n, p)
print(f"Var(x): {variance:.2f}")

std_dev = math.sqrt(variance)
print(f"S.D: {std_dev:.2f}")

cv = (std_dev / (expected_value)) * 100  # درصد
print(f"C.V: {cv:.2f}%")



