import matplotlib.pyplot as plt
import numpy as np

#----------------------------------------------------------------------------------
#### رسم نمودار میله ای  برای نمایش میانگین درآمد‌ ماهانه افراد در سه شهر مختلف با نمودار میله ای 
# cities = ['City A', 'City B', 'City C']
# income_monthly = [np.random.randint(2000, 18000) for _ in range(3)]
# plt.figure(figsize=(10, 6))  
# plt.bar(cities, income_monthly, color='blue')
# plt.xlabel('Cities')
# plt.ylabel('Monthly Income ($)')
# plt.title('Monthly Incomes Chart')
# plt.show()

#----------------------------------------------------------------------------------
####  رسم نمودار خطی برای نمایش تغییرات قیمت سهام در بازار سهام
# days = np.arange(1, 11)
# stock_prices = np.array([100, 105, 110, 112, 115, 112, 113, 120, 125,138])
# plt.figure(figsize=(10, 6))  
# plt.plot(days, stock_prices, marker='o', linestyle='-', color='blue')
# plt.xlabel('Days')
# plt.ylabel('Stock Price ($)')
# plt.title('Stock Price Chart')
# plt.show()

#----------------------------------------------------------------------------------
####رسم نمودار نقطه ای برای نمایش رابطه بین وزن و قد در جمعیت
# population_size = 20
# heights = np.random.uniform(150, 200, population_size)
# weights = np.random.uniform(50, 100, population_size)

# plt.figure(figsize=(10, 6))  
# plt.scatter(heights, weights, color='blue', alpha=0.5)
# plt.xlabel('Height (cm)')
# plt.ylabel('Weight (kg)')
# plt.title('Height and Weight Chart')
# plt.show()

#----------------------------------------------------------------------------------
#### رسم نمودار دایره ای نسبتی وقت صرف شده در روز به فعالیت های مختلف
# activities = ['Sleeping', 'Working', 'Eating', 'Study', 'Others']
# time_spent = [8, 8, 2, 3, 3]
# plt.figure(figsize=(10, 6))  
# plt.pie(time_spent, labels=activities, autopct='%1.1f%%', startangle=90, colors=['blue', 'green', 'orange', 'red', 'pink'])
# plt.axis('equal')  
# plt.title('Time Spent Chart')
# plt.legend()
# plt.show()

#----------------------------------------------------------------------------------
#### رسم نمودار شمعی برای نمایش تغییرات قیمت سهام در پنج روز اول اگوست 2023
# import pandas as pd
# import mplfinance as mpf
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
# mpf.plot(df, type='candle', style='charles', title='Candlestick Chart')

#----------------------------------------------------------------------------------
#### رسم نمودار باکس ویسکر برای نمایش میزان توزیع سن افراد در سه گروه مختلف 
# data = [
#     [12, 15, 20, 25, 30, 35, 40, 45, 50, 55],
#     [15, 18, 22, 26, 30, 38, 42, 47, 52, 58],
#     [10, 14, 18, 22, 27, 32, 38, 44, 50, 60]
# ]
# plt.figure(figsize=(10, 6))  
# plt.boxplot(data, labels=['A', 'B', 'C'])
# plt.xlabel('Groups')
# plt.ylabel('Values')
# plt.title('Box and Whisker Plot')
# plt.show()

#----------------------------------------------------------------------------------
#### رسم نمودار هیستوگرام برای معدل دانشجویان یک کلاس 30 نفره در چهار گروه از نظر معدل
# student_grades = np.random.uniform(0, 20, 30)
# bins = [0, 10, 15, 18, 20]
# colors = ['blue', 'green', 'orange', 'red']
# N, bins, patches =plt.hist(student_grades, bins=bins, edgecolor='black')
# for i in range(len(colors)):
#     patches[i].set_facecolor(colors[i])
# plt.xlabel('Grades')
# plt.ylabel('Frequency')
# plt.title('histogram Student Grades')
# plt.show()

#----------------------------------------------------------------------------------
#### رسم نمودار حبابی برای تعدادی کالا که هر کدام سه ویژگی قیمت، وزن و میزان محبوبیت را دارند 
# num_products = 5
# prices = np.random.uniform(10, 100, num_products)
# weights = np.random.uniform(0.5, 5, num_products)
# popularity = np.random.uniform(0, 100, num_products)
# plt.scatter(prices, weights, s=popularity, c=popularity)
# plt.xlabel('Price')
# plt.ylabel('Weight')
# plt.title('Bubble Chart')
# plt.colorbar(label='Popularity')
# plt.show()