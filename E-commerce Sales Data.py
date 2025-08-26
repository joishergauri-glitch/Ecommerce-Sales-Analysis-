import pandas as pd

import plotly.express as px


df = pd.read_csv('women_clothing_ecommerce_sales.csv')

# Convert order_date to datetime
df['order_date'] = pd.to_datetime(df['order_date'])
# Extract month and year for trend analysis
df['Year_Month'] = df['order_date'].dt.to_period('M')
df['Year_Month'] = df['Year_Month'].astype(str)
# Monthly sales trend with additional metrics
monthly_sales = df.groupby('Year_Month').agg({
    'revenue': 'sum',
    'order_id': 'nunique',
    'quantity': 'sum'
}).reset_index()
monthly_sales = monthly_sales.sort_values('Year_Month')

# Create line chart for monthly sales trend
fig = px.line(monthly_sales, x='Year_Month', y='revenue',
              title='Monthly Sales Trend',
              labels={'revenue': 'Revenue ($)', 'Year_Month': 'Month'})
fig.update_layout(xaxis_title='Month', yaxis_title='Revenue ($)')
fig.show()

# Display the monthly sales data
monthly_sales

