import matplotlib.pyplot as plt


x = [1,3,5,7,9,11,13,15,17,19]
y = [3,6,9,12,15,18,21,24,27,30]


meanX = sum(x)/len(x)
meanY = sum(y)/len(y)

# y = mx + c

numerator = sum((x[i] - meanX) * (y[i] - meanY) for i in range(len(x)))
denominator = sum((x[i] - meanX) ** 2 for i in range(len(x)))

m = numerator / denominator
c = meanY - m * meanX

#newX = 7
#newY = m * newX + c
#print(f"Predicted Y for X={newX}: {newY}")

Y_pred = [c + m * x_i for x_i in x]
newx = 21
newy = c + m * newx

print(newy)

plt.scatter(x, y, color='blue', label='Original Data')
plt.plot(y, Y_pred, color='red', label='Linear Regression Line')
plt.legend()
plt.show()