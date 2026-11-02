import matplotlib.pyplot as plt

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

rainfall = [20, 30, 40, 50, 80, 100, 120, 110, 90, 150, 180, 60]

plt.scatter(months, rainfall)
plt.xlabel('Months')
plt.ylabel('Rainfall (mm)')
plt.title('Monthly Rainfall')
plt.show()
