# Statsmodels تجزیه و تحلیل یک مدل رگرسیون ساده با استفاده از 
import statsmodels.api as sm
import numpy as np


x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 3.5, 4.5, 5.5, 7])

# add_constant اضافه کردن عبارت توسط تابع 
x = sm.add_constant(x)

# مدل رگرسیون ساده
model = sm.OLS(y, x).fit()

print(model.summary())
