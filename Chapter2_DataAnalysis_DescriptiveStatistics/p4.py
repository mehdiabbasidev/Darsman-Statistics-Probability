# import matplotlib.pyplot as plt

# # داده‌ها
# products = ['CPU', 'RAM', 'HDD', 'VGA', 'MOUSE']
# salesNumber = [25, 30, 20, 20, 65]


# # رسم نمودار میله‌ای
# # plt.bar(products, salesNumber, color='blue', label='salesNumber')  

# #  رسم نمودار نقطه‌ای
# # plt.scatter(products, salesNumber, color='black', marker='o', label='salesNumber Points')

# # اضافه کردن نمودار دایره‌ای
# # plt.pie(salesNumber, labels=products, autopct='%1.1f%%', startangle=0)


# plt.xlabel('Products')
# plt.ylabel('Values')
# plt.title('Chart')
# plt.legend()
# plt.show()





####  نمودار شمعی (Candlestick Chart)

# import pandas as pd
# import mplfinance as mpf

# # داده‌ها برای نمونه
# data = {
#     'date':  ['2023-08-01', '2023-08-02', '2023-08-03', '2023-08-04', '2023-08-05'],
#     'open':  [150, 155, 152, 154, 160],
#     'high':  [160, 160, 156, 158, 165],
#     'low':   [145, 150, 150, 152, 158],
#     'close': [155, 158, 153, 155, 163]
# }


# df = pd.DataFrame(data)
# df['date'] = pd.to_datetime(df['date'])
# df.set_index('date', inplace=True)
# print(df)
# mpf.plot(df, type='candle', style='charles', title='Candlestick Chart')




#### نمودار باکس ویسکر (Box Plot)

# import matplotlib.pyplot as plt

# # داده‌ها برای نمونه
# data = [
#     [12, 15, 20, 25, 30, 35, 40, 45, 50, 55],
#     [15, 18, 22, 26, 30, 38, 42, 47, 52, 58],
#     [10, 14, 18, 22, 27, 32, 38, 44, 50, 60]
# ]

# # رسم نمودار باکس ویسکر
# plt.boxplot(data, labels=['A', 'B', 'C'])

# plt.xlabel('Groups')
# plt.ylabel('Values')
# plt.title('Box and Whisker Plot')

# plt.show()




# import matplotlib.pyplot as plt
# import numpy as np

# # داده‌ها برای نمونه
# data = np.random.randn(20)  # داده‌های تصادفی با توزیع نرمال
# print(data)
# # رسم نمودار هیستوگرام
# plt.hist(data, bins=5, edgecolor='black')  # bins تعداد بازه‌ها

# plt.xlabel('Values')
# plt.ylabel('Frequency')
# plt.title('Histogram Plot')

# plt.show()



# import matplotlib.pyplot as plt
# import numpy as np

# # داده‌ها برای نمونه
# x = np.random.rand(20)  # داده‌های تصادفی برای محور x
# y = np.random.rand(20)  # داده‌های تصادفی برای محور y
# sizes = np.random.randint(10, 100, size=20)  # اندازه‌های تصادفی برای اندازه حباب‌ها

# # رسم نمودار حبابی
# plt.scatter(x, y, s=sizes, c='blue', alpha=0.5)

# plt.xlabel('X Values')
# plt.ylabel('Y Values')
# plt.title('Bubble Chart')

# plt.show()





import matplotlib.pyplot as plt
import numpy as np

# داده‌ها برای نمونه
data = [np.random.normal(0, std, 100) for std in range(1, 5)]

# رسم نمودار باکس ویسکر
plt.boxplot(data, labels=['Data 1', 'Data 2', 'Data 3', 'Data 4'])

plt.xlabel('Data Groups')
plt.ylabel('Values')
plt.title('Box Plot Example')

plt.show()






import matplotlib.pyplot as plt
import numpy as np

# داده‌ها برای نمونه
products = ['Product A', 'Product B', 'Product C', 'Product D', 'Product E']
prices = np.random.randint(10, 100, size=len(products))
inventory = np.random.randint(1, 50, size=len(products))
popularity = np.random.randint(100, 1000, size=len(products))

# رسم نمودار حبابی
plt.scatter(prices, inventory, s=popularity/10, c='blue', alpha=0.5)
plt.xlabel('Price')
plt.ylabel('Inventory')
plt.title('Product Characteristics Bubble Chart')

# افزودن برچسب به حباب‌ها
for i, product in enumerate(products):
    plt.annotate(product, (prices[i], inventory[i]), textcoords="offset points", xytext=(0,10), ha='center')

plt.show()




