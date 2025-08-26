import pandas as pd

# Load the e-commerce sales data from the table
df = pd.read_csv('women_clothing_ecommerce_sales.csv')

# Convert revenue to numeric
df['revenue'] = pd.to_numeric(df['revenue'], errors='coerce')

# Extract category from SKU
df['category'] = df['sku'].str.split('-').str[0]

# Get top 5 products by revenue
top_products = df.groupby('sku')['revenue'].sum().sort_values(ascending=False).head(5)

# Get top 5 categories by revenue
top_categories = df.groupby('category')['revenue'].sum().sort_values(ascending=False).head(5)

# Create a summary DataFrame
summary = pd.DataFrame({
    'Top Products': top_products.index.tolist() + [''] * (5 - len(top_products)),
    'Product Revenue': top_products.values.tolist() + [0] * (5 - len(top_products)),
    'Top Categories': top_categories.index.tolist() + [''] * (5 - len(top_categories)),
    'Category Revenue': top_categories.values.tolist() + [0] * (5 - len(top_categories))
})

print (summary)