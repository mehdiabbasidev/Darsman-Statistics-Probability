#فرض کنید یک سکه داریم که به طور متوسط ۳۰٪ از زمان شیر می‌آید.
# import scipy.stats as stats
# p = 0.3
# prob_success = stats.bernoulli.pmf(1, p)
# print(prob_success)
# prob_failure = stats.bernoulli.pmf(0, p)
# print(prob_failure)

#----------------------------------------------------------------------------------------
#یک سیستم اتوماتیک برای تشخیص ایمیل‌های اسپم و معمولی داریم. احتمال اینکه ایمیل وارد صندوق ایمیل شما شود و اسپم نباشد برابر با 0.9 است
import scipy.stats as stats
p = 0.9
prob_success = stats.bernoulli.pmf(1, p)
print(prob_success)
prob_failure = stats.bernoulli.pmf(0, p)
print(prob_failure)