from matplotlib import pyplot as plt
y = [5, 3, 7, 10, 9, 5, 3.5, 8]
x = range(8)
plt.plot(x, y, color='blue')
plt.bar(x,y,width=0.7,color='white')
plt.show()
