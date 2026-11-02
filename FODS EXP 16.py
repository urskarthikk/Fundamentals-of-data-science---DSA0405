from collections import Counter

reviews = [
    "Good product and good quality",
    "Excellent product",
    "Good quality product"
]

words = " ".join(reviews).lower().split()

frequency = Counter(words)

print(frequency)
