import matplotlib.pyplot as plt

months = [1, 2, 3, 4, 5]
sales = [100, 150, 180, 200, 250]

plt.scatter(months, sales)
plt.xlabel('Months')
plt.ylabel('Sales')
plt.title('Product Sales Scatter Plot')
plt.show()
