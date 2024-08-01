# seaborn رسم نمودار به کمک
import seaborn as sns
import matplotlib.pyplot as plt

data = sns.load_dataset("iris")

sns.set(style="whitegrid")
plt.figure(figsize=(8, 6))

sns.scatterplot(x="sepal_length", y="sepal_width", data=data, hue="species", palette="Set1", s=100)
plt.show()
