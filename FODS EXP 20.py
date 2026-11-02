import numpy as np
from scipy.stats import ttest_ind

A = [1, 0, 1, 1, 0, 1, 0, 1, 1, 0]
B = [0, 0, 1, 0, 1, 0, 0, 1, 0, 0]

print("Design A:", np.mean(A))
print("Design B:", np.mean(B))

t, p = ttest_ind(A, B)

print("T-value:", t)
print("P-value:", p)

if p < 0.05:
    print("Significant difference")
else:
    print("No significant difference")
