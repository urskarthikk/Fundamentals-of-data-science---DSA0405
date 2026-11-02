import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats

# Sample data (replace with given 18 observations)
df = pd.DataFrame({
    'Age': [23, 25, 30, 35, 40, 45, 28, 32, 38,
            42, 26, 29, 33, 37, 41, 44, 31, 36],
    'Fat': [15, 18, 20, 22, 25, 28, 17, 19, 23,
            26, 16, 21, 24, 27, 29, 30, 20, 22]
})

# Mean, Median and Standard Deviation
print(df.mean())
print(df.median())
print(df.std())

# Boxplots
df.boxplot()
plt.title('Boxplot of Age and Fat')
plt.show()

# Scatter plot
plt.scatter(df['Age'], df['Fat'])
plt.xlabel('Age')
plt.ylabel('Body Fat')
plt.title('Age vs Body Fat')
plt.show()

# Q-Q plots
stats.probplot(df['Age'], dist="norm", plot=plt)
plt.title('Q-Q Plot of Age')
plt.show()

stats.probplot(df['Fat'], dist="norm", plot=plt)
plt.title('Q-Q Plot of Body Fat')
plt.show()
