import pandas as pd
import numpy as np

# Load the e-commerce sales data from the table
df = pd.read_csv('women_clothing_ecommerce_sales.csv')

# Convert relevant columns to appropriate data types
df['order_date'] = pd.to_datetime(df['order_date'])
df['revenue'] = pd.to_numeric(df['revenue'], errors='coerce')
df['unit_price'] = pd.to_numeric(df['unit_price'], errors='coerce')
df['quantity'] = pd.to_numeric(df['quantity'], errors='coerce')

# Since we don't have customer_id, we'll segment based on order characteristics
# High-value vs Low-value orders (based on revenue)
revenue_threshold = df['revenue'].quantile(0.75)
df['order_value_segment'] = df['revenue'].apply(
    lambda x: 'High-value' if x >= revenue_threshold else 'Low-value'
)

# New vs Returning products (based on order date)
# First we need to determine what constitutes a "new" product
# We'll define products ordered in the first 25% of the date range as "new"
date_threshold = df['order_date'].quantile(0.25)
df['product_segment'] = df['order_date'].apply(
    lambda x: 'New' if x <= date_threshold else 'Established'
)

# Create summary statistics for order segments
# High-value vs Low-value orders
high_value_orders = df[df['order_value_segment'] == 'High-value']['order_id'].nunique()
low_value_orders = df[df['order_value_segment'] == 'Low-value']['order_id'].nunique()
high_value_revenue = df[df['order_value_segment'] == 'High-value']['revenue'].sum()
low_value_revenue = df[df['order_value_segment'] == 'Low-value']['revenue'].sum()

# New vs Established products/orders
new_orders = df[df['product_segment'] == 'New']['order_id'].nunique()
established_orders = df[df['product_segment'] == 'Established']['order_id'].nunique()
new_revenue = df[df['product_segment'] == 'New']['revenue'].sum()
established_revenue = df[df['product_segment'] == 'Established']['revenue'].sum()

# Create summary DataFrame
segmentation_summary = pd.DataFrame({
    'Segment': ['High-value Orders', 'Low-value Orders', 'New Products/Orders', 'Established Products/Orders'],
    'Order Count': [high_value_orders, low_value_orders, new_orders, established_orders],
    'Total Revenue': [high_value_revenue, low_value_revenue, new_revenue, established_revenue]
})

print (segmentation_summary)