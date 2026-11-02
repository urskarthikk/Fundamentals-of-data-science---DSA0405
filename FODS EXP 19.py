import numpy as np
from scipy import stats

drug = [12, 15, 14, 10, 18, 16, 13, 17, 11, 14]
placebo = [5, 7, 6, 4, 8, 5, 9, 6, 7, 4]

def ci(data):
    n = len(data)
    mean = np.mean(data)
    se = stats.sem(data)
    t = stats.t.ppf(0.975, n-1)
    margin = t * se
    return mean-margin, mean+margin

print("Drug CI:", ci(drug))
print("Placebo CI:", ci(placebo))
