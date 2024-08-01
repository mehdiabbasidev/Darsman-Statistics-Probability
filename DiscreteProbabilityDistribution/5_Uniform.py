#می‌خواهیم به یازده دانش‌آموز یک کلاس به صورت تصادفی نمره‌ای با مقدارهای صحیح از ۱۰ تا ۲۰ بدهیم
#احتمال اینکه نمره دانش آموزی 18باشد
#احتمال اینکه نمره دانش آموزی کمتر از 13 باشد
 
import numpy as np
from scipy.stats  import randint
import matplotlib.pyplot as plt

a,b=10,20
x_values = np.r_[a:b+1]                      #x_values = np.linspace(a, b+1, 11)  [10,11,12,....,20]
uniform_pmf = randint.pmf(x_values, a, b+1)

x=18
index=np.where(x_values==x)[0][0]
print(f"P(X={x}): {uniform_pmf[index]:.5f}")






sum_prob=0
for x in range(a,13):
    index=np.where(x_values==x)[0][0]
    sum_prob+=uniform_pmf[index]
print(f"P(X<13): {sum_prob:.5f}")
    
plt.plot(x_values, uniform_pmf, 'bo', ms=10)
plt.vlines(x_values, 0, uniform_pmf, colors='r', lw=1, alpha=0.2)
plt.xlabel('X_Values')
plt.ylabel('Probability')
plt.show()


























# from scipy.stats import randint
# low, high =1, 11
# mean, var, skew, kurt = randint.stats(low, high, moments='mvsk')
# print(mean, var, skew, kurt )







# import numpy as np
# import matplotlib.pyplot as plt
# from scipy.stats import skew, kurtosis

# # تعداد دانش‌آموزان
# n_students = 5

# # تعداد نمرات
# n_grades = 10

# # ایجاد توزیع یکنواخت از 10 تا 20 برای نمرات
# grades = np.random.randint(10, 21, size=(n_students, n_grades))
# print(grades)
# # محاسبه نمودار چولگی برای هر دانش‌آموز
# skewness_values = [skew(student_grades) for student_grades in grades]
# print(skewness_values)
# # محاسبه نمودار کشیدگی برای هر دانش‌آموز
# kurtosis_values = [kurtosis(student_grades) for student_grades in grades]
# print(kurtosis_values)

# # نمودار چولگی
# plt.figure(figsize=(12, 4))
# plt.subplot(1, 2, 1)
# plt.hist(skewness_values, bins=20, color='skyblue', edgecolor='black')
# plt.title('Histogram of Skewness')
# plt.xlabel('Skewness Value')
# plt.ylabel('Frequency')

# # نمودار کشیدگی
# plt.subplot(1, 2, 2)
# plt.hist(kurtosis_values, bins=20, color='salmon', edgecolor='black')
# plt.title('Histogram of Kurtosis')
# plt.xlabel('Kurtosis Value')
# plt.ylabel('Frequency')

# plt.tight_layout()
# plt.show()






# import numpy as np
# import matplotlib.pyplot as plt

# # تعداد دانش‌آموزان
# n_students = 11

# # تعداد نمرات
# n_grades = 10000

# # ایجاد توزیع یکنواخت از 10 تا 20 برای نمرات
# grades = np.random.randint(10, 21, size=(n_students, n_grades))

# # محاسبه میانگین نمرات هر دانش‌آموز
# mean_grades = np.mean(grades, axis=1)

# # ترسیم نمودار خطی
# plt.figure(figsize=(8, 6))
# plt.plot(range(1, n_students + 1), mean_grades, marker='o', linestyle='-', color='b')
# plt.title('میانگین نمرات دانش‌آموزان')
# plt.xlabel('دانش‌آموز')
# plt.ylabel('میانگین نمره')
# plt.xticks(range(1, n_students + 1))
# plt.grid(True)

# plt.show()



# import numpy as np
# from scipy.stats import skew
# import matplotlib.pyplot as plt

# x1 = np.linspace( -5, 5, 200 )
# y1 = 1./(np.sqrt(2.*np.pi)) * np.exp( -.5*(x1)**2  )

# print(x1)
# print(y1)
# print( '\nSkewness for data : ', skew(y1))

# plt.plot(x1, y1, 'bo', ms=2)
# plt.xlabel('X')
# plt.ylabel('Probability')
# plt.show()
