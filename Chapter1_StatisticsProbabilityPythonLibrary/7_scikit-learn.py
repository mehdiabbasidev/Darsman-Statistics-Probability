# مثال: آموزش یک مدل ساده خطی با استفاده از Scikit-learn.

from sklearn.linear_model import LinearRegression
import numpy as np

# ساخت داده‌ها
x = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)
y = np.array([2, 3.5, 4.5, 5.5, 7])

# ایجاد مدل
model = LinearRegression()

# آموزش مدل با داده‌ها
model.fit(x, y)

# نمایش پارامترهای مدل
print("Intercept:", model.intercept_)
print("Coefficient:", model.coef_)
