import pandas as pd
import matplotlib.pyplot as plt
import re
from collections import Counter

df = pd.read_csv('data.csv')

stop_words = ['the', 'and', 'is', 'a', 'an', 'in', 'to', 'of']

words = []

for text in df['feedback'].dropna():
    text = re.sub(r'[^\w\s]', '', text.lower())
    for word in text.split():
        if word not in stop_words:
            words.append(word)

freq = Counter(words)

n = int(input("Enter N: "))
top = freq.most_common(n)

print(top)

w, f = zip(*top)

plt.bar(w, f)
plt.xlabel('Words')
plt.ylabel('Frequency')
plt.title('Top N Frequent Words')
plt.show()
