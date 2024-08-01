import numpy as np

### محاسبه میانگین و واریانس یک آرایه از اعداد.
data = np.array([10, 15, 20, 25, 30])
mean = np.mean(data)
variance = np.var(data)
print("Mean:", mean)
print("Variance:", variance)




### تولید داده تصادفی با توزیع نرمال
# mean = 0
# std_dev = 1
# sample_size = 100
# data_normal = np.random.normal(mean, std_dev, sample_size)
# print(data_normal)

