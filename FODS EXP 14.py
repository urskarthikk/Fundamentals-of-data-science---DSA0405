from collections import Counter
import re

file = open(r'C:\Users\yashw\Downloads\14 exp note pad.txt', 'r')

text = file.read().lower()
file.close()

text = re.sub(r'[^\w\s]', '', text)

words = text.split()

frequency = Counter(words)

print("Word Frequency Distribution:")
for word, count in frequency.items():
    print(word, ":", count)
