
from scipy.stats import expon


# prob = expon.cdf(x=1, scale=0.25)    #scale=m
# print('Probability :',1-prob)



# #------------------------------------------------------------------
# prob = expon.cdf(x=10, scale=5)
# print('Probability :',1-prob)

# #------------------------------------------------------------------
# prob = expon.cdf(x=1, scale=2)     
# print('Probability :',prob)
# prob = expon.cdf(x=5, scale=2)
# print('Probability :',1-prob)

#------------------------------------------------------------------
prob = expon.cdf(x=6, scale=2)
print('Probability :',1-prob)



















# import numpy as np
# n = 8
# values=np.random.default_rng()
# print(values)
# time_between_calls = values.exponential(scale=0.2, size=n)
# print(time_between_calls)


# from scipy.stats import expon
# import matplotlib.pyplot as plt
# import numpy as np

#creating an array of values between
#-1 to 10 with a difference of 0.1
# x = 1
# print(x)  
# y = expon.pdf(x, 0, 2)
# print(y)  
  
# z = expon.cdf(x, 4, 1)
# print(z)    
 
# # plt.plot(x, y) 
# # plt.show()



# import matplotlib.pyplot as plt 
# import numpy as np 
# from scipy.stats import expon  
# x = np.array([1,2,3,4,5,6,7,8,9,10])
# y1 = expon.pdf(x, 0.25, 10) 

# print(x)
# print(y1)
# # print(y2)






# import matplotlib.pyplot as plt
# import numpy as np

# #fixing the seed for reproducibility
# #of the result
# np.random.seed(10)

# size = 10000
# #drawing 10000 sample from 
# #exponential distribution
# sample = np.random.exponential(1, size)
# bin = np.arange(0,10,0.1)

# plt.hist(sample, bins=bin, edgecolor='blue') 
# plt.title("Exponential Distribution") 
# plt.show()


# import scipy.stats as stats
# prob=stats.expon.cdf(100)
# print(prob)



# import numpy as np

# from scipy.stats import expon

# q = np.arange (0.09, 1, 0.2)

# ecrv = expon.rvs(scale = 3,  size = 15)

# print ("Exponential Continuous Random Variates:\n\n", ecrv)

# ex = expon.cdf(q, loc = 0.2, scale = 10)

# print ("\nProbability Distribution : \n", ex)




# from scipy.stats import expon
# import matplotlib.pyplot as plt
# import numpy as np
# fig, ax = plt.subplots(1, 1)
# # Calculate a few first moments:

# mean, var, skew, kurt = expon.stats(moments='mvsk')

# # Display the probability density function (``pdf``):

# x = np.linspace(expon.ppf(0.01),
#               expon.ppf(0.99), 100)
# ax.plot(x, expon.pdf(x),
#          'r-', lw=5, alpha=0.6, label='expon pdf')

# # Alternatively, freeze the distribution and display the frozen pdf:

# rv = expon()
# ax.plot(x, rv.pdf(x), 'k-', lw=2, label='frozen pdf')

# # Check accuracy of ``cdf`` and ``ppf``:

# vals = expon.ppf([0.001, 0.5, 0.999])
# np.allclose([0.001, 0.5, 0.999], expon.cdf(vals))
# # True

# # Generate random numbers:

# r = expon.rvs(size=1000)

# # And compare the histogram:

# ax.hist(r, normed=True, histtype='stepfilled', alpha=0.2)
# ax.legend(loc='best', frameon=False)
# plt.show()




# from scipy.stats import expon
# import matplotlib.pyplot as plt
# import seaborn as sns

# #When average time between 2 messages is 50 seconds
# data1 = expon.rvs(scale=5, size=10000)



# #Plot sample data
# sns.kdeplot(x=data1, fill=True, label='1/lambda=5')
# plt.xlabel('Units of time between successive events')
# plt.ylabel('Probability')
# plt.title('Exponential Distribution')
# plt.legend()
# plt.xlim(0, 8)
# plt.show();
