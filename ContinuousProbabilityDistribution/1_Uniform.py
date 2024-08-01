import numpy as np

randNumbers=np.random.uniform(low=0.1,high=0.99,size=(5,3))
print(randNumbers)

# randNumbers= np.random.uniform(size=5)
# print(randNumbers)



# randNumbers=np.random.uniform(10,20,5)
# print(randNumbers)



# np.random.seed(0)
# randNumbers=np.random.uniform(0.0, 1.0, size = 5)
# print(randNumbers)


# -----------------------------------------------------------------

# import numpy as np
# import matplotlib.pyplot as plt


# def uniform_probability_density(x, a, b):
#     if x < a or x > b:
#         return 0
#     else:
#         return 1 / (b - a)


# a = 2
# b = 8
# mean = (a + b) / 2
# variance = ((b - a) ** 2) / 12
# print(f'E(x): {mean}')
# print(f'Var(x): {variance}')


# # P(3<X<5)
# c = 3
# d = 5
# probability_x_lt_p = (d - c) / (b - a)
# print(f'P({c}<= X <={d}) : {probability_x_lt_p}')


# # P(X<6)=P(2<X<6)
# c = a
# d = 6
# probability_x_lt_p = (d - c) / (b - a)
# print(f'P({c}<= X <={d}) : {probability_x_lt_p}')



# # P(3<X)
# c = 3
# d = b
# probability_x_lt_p = (d - c) / (b - a)
# print(f'P({c}<= X <={d}) : {probability_x_lt_p}')



# x_values = np.linspace(a - 1, b + 1, 1000)
# prob_values = [uniform_probability_density(x, a, b) for x in x_values]
# plt.plot(x_values, prob_values)
# plt.xlabel('X')
# plt.ylabel('Y')
# plt.title(f'Uniform Probability Distributions[{a}, {b}]')
# plt.show()