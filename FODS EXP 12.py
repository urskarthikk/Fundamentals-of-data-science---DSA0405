import matplotlib.pyplot as plt

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

temperature = [25, 27, 30, 33, 35, 32, 30, 29, 28, 27, 26, 24]

plt.plot(months, temperature, marker='o')
plt.xlabel('Months')
plt.ylabel('Temperature (°C)')
plt.title('Monthly Temperature')
plt.show()
