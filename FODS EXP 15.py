import pandas as pd

likes = [100, 200, 100, 300, 200, 100, 400, 300, 200]

df = pd.DataFrame({'likes': likes})

print(df['likes'].value_counts().sort_index())
