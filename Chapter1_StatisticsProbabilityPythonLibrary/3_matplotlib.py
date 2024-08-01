# رسم نمودار میله‌ای
import matplotlib.pyplot as plt

groups = ['A', 'B', 'C', 'D']
values = [15, 30, 10, 25]
plt.bar(groups, values)
plt.xlabel('Groups')
plt.ylabel('Values')
plt.show()
