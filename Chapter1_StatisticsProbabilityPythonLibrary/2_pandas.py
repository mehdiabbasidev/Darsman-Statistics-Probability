import pandas as pd

# ساخت یک دیتافریم از داده‌ها و نمایش آن
# data = {'Name': ['mehdi', 'ali', 'reza', 'ahmad'],'Age': [25, 30, 22, 28]}
# df = pd.DataFrame(data)
# print(df)



#1) خواندن و نمایش داده‌ها از فایل‌های مختلف  
# df_csv = pd.read_csv('data.csv')
# print(df_csv)


#2) تجزیه و تحلیل داده‌ها و اعمال توابع آماری به داده‌ها
file_path = './data/sales.csv'
df = pd.read_csv(file_path)

# # محاسبه میانگین فروش برای هر ماه
mean_sales = df.groupby('Month')['Sales'].mean()
print(mean_sales)

# # محاسبه حداکثر فروش برای هر ماه
max_sales = df.groupby('Month')['Sales'].max()
print(max_sales)


