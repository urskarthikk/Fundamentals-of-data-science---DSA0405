import matplotlib.pyplot as plt

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May']
sales = [100, 150, 120, 200, 250]

plt.plot(months, sales, marker='o')
plt.xlabel('Months')
plt.ylabel('Sales')
plt.title('Monthly Sales Line Plot')
plt.show()
