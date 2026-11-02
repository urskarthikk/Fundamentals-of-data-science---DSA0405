import pandas as pd

data = {
    'property_id': [1, 2, 3, 4],
    'location': ['Chennai', 'Chennai', 'Bangalore', 'Bangalore'],
    'bedrooms': [3, 5, 2, 6],
    'area': [1200, 2000, 1000, 2500],
    'price': [5000000, 8000000, 4000000, 9000000]
}

property_data = pd.DataFrame(data)

# 1. Average price in each location
print(property_data.groupby('location')['price'].mean())

# 2. Properties with more than four bedrooms
print(property_data[property_data['bedrooms'] > 4])

# 3. Property with largest area
print(property_data.loc[property_data['area'].idxmax()])
