# all three matplotlib lectures are within this file
# most popular plotting lib for Python
# gives control over every aspect of figure
#matplotlib.org - official website with examples + code examples
import matplotlib.pyplot as plt
# ***plt.show() will be used each time we'd like to show the plot
import numpy as np
x = np.linspace(0,5,11)
y = x ** 2
# print(x)
# print(y)
# two methods of plotting - functional and OO method
# functional
# plt.plot(x,y, '-b') #-b for color blue
# plt.xlabel('X label')
# plt.ylabel('Y label')
# plt.title('SomeTitle')
# plt.show()
# multiple plots on same canvas
# plt.subplot(1,2,1) #rows, cols, plotnumber refering to
# plt.plot(x,y,'r')
#
# plt.subplot(1,2,2)
# plt.plot(y,x,'b')
# plt.show()

# OO method
# fig = plt.figure()
# axes = fig.add_axes([0.1,0.1,0.8,0.8]) #left, bottom, width, height
# axes.plot(x,y)
# axes.set_xlabel('X label')
# axes.set_ylabel('Y label')
# axes.set_title('Title')
# plt.show()

# fig = plt.figure()
# axes1 = fig.add_axes([0.1,0.1,0.8,0.8]) #left, bottom, width, height
# axes2 = fig.add_axes([0.2,0.5,0.4,0.3])
# axes1.plot(x,y)
# axes2.plot(y,x)
# axes1.set_title('Larger Plot')
# axes2.set_title('Smaller plot')
# fig, axes =  plt.subplots(nrows=1, ncols=2) #2 subplots - tuple unpacking
# axes[0].plot(x,y)
# axes[0].set_title('First Plot')
#
# axes[1].plot(y,x)
# axes[1].set_title('Second Plot')
# plt.tight_layout() #just for nice plotting without any "tight values"
# # Figure size and DPI
# plt.show()


# fig,axes = plt.subplots(nrows=2, ncols=1, figsize=(8,2))
# axes[0].plot(x,y)
# axes[1].plot(y,x)
# plt.tight_layout()
# plt.show()
# fig.savefig('myPic.png') #save figure to a file
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.plot(x,x**2, label='X Squared')
ax.plot(x,x**3, label='X Cubed')
ax.set_title('Title')
ax.set_xlabel('X')
ax.set_ylabel('Y')

ax.legend(loc=0)
plt.show()
