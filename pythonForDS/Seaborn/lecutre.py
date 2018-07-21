# Distribution Plots
import seaborn as sns
import matplotlib.pyplot as plt # because not using jupyter notebook
# if using jupyter notebook use %matplotlib inline for visualization inline
tips = sns.load_dataset('tips')
print(tips.head()) #people who had a meal and left tip in the end
sns.distplot(tips['total_bill'])
plt.show()
