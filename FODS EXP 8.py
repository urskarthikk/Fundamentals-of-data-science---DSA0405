import pandas as pd

data = {
    'product': ['Mobile', 'Laptop', 'Tablet', 'Mobile', 'Laptop', 'Mouse'],
    'quantity': [20, 15, 10, 25, 30, 12],
    'date': ['2026-10-05', '2026-10-10', '2026-10-12',
             '2026-10-15', '2026-10-20', '2026-10-25']
}

df = pd.DataFrame(data)

df['date'] = pd.to_datetime(df['date'])

# Filter past month
df = df[df['date'].dt.month == 10]

# Find top 5 products
top5 = df.groupby('product')['quantity'].sum().nlargest(5)

print(top5)
