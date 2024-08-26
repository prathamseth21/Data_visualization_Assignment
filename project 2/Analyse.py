import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from db_connection import connect_to_database, fetch_data  

# Step 1: Connect to the Database
connection = connect_to_database()

# Step 2: Fetch Data from the Database
customer_data, product_data, order_data = fetch_data(connection)

if customer_data is None or product_data is None or order_data is None:
    print("Data could not be fetched from the database.")
else:
    # Customer Analysis

    # ## 1. Identify the total number of customers city-wise
    # customer_city_count = customer_data['city'].value_counts()

    # # Create a bar chart for total number of customers city-wise
    # plt.figure(figsize=(10, 6))
    # customer_city_count.plot(kind='bar', color='skyblue')
    # plt.title('Total Number of Customers City-Wise')
    # plt.xlabel('City')
    # plt.ylabel('Number of Customers')
    # plt.xticks(rotation=45)
    # plt.tight_layout()
    # plt.show()

    # ## 2. Identify the most frequent customers based on their order history
    # frequent_customers = order_data['customer_id'].value_counts().reset_index()
    # frequent_customers.columns = ['customer_id', 'order_count']

    # # Create a bar chart for the top 10 most frequent customers
    # top_10_customers = frequent_customers.head(10)
    # plt.figure(figsize=(10, 6))
    # plt.bar(top_10_customers['customer_id'], top_10_customers['order_count'], color='salmon')
    # plt.title('Top 10 Most Frequent Customers Based on Order History')
    # plt.xlabel('Customer ID')
    # plt.ylabel('Number of Orders')
    # plt.xticks(rotation=45)
    # plt.tight_layout()
    # plt.show()

    # Product Analysis

    # ## 1. Determine the total number of products available by category
    # product_category_count = product_data['category'].value_counts()

    # # Create a bar chart for total number of products available by category
    # plt.figure(figsize=(10, 6))
    # product_category_count.plot(kind='bar', color='lightgreen')
    # plt.title('Total Number of Products Available by Category')
    # plt.xlabel('Category')
    # plt.ylabel('Number of Products')
    # plt.xticks(rotation=45)
    # plt.tight_layout()
    # plt.show()

    ## 2. Analyze the distribution of products across sub-categories
    # product_sub_category_distribution = product_data['sub_category'].value_counts()

    # # Create a bar chart for the distribution of products across sub-categories
    # plt.figure(figsize=(10, 6))
    # product_sub_category_distribution.plot(kind='bar', color='violet')
    # plt.title('Distribution of Products Across Sub-Categories')
    # plt.xlabel('Sub-Category')
    # plt.ylabel('Number of Products')
    # plt.xticks(rotation=45)
    # plt.tight_layout()
    # plt.show()
    

    ### Product Analysis
    
    # # 1. Identify products with low stock levels
    # low_stock_threshold = 80  # Define what is considered low stock
    # low_stock_products = product_data[product_data['stock'] < low_stock_threshold]

    # # Create a bar chart for products with low stock levels
    # plt.figure(figsize=(10, 6))
    # plt.bar(low_stock_products['product_name'], low_stock_products['stock'], color='orange')
    # plt.title('Products with Low Stock Levels')
    # plt.xlabel('Product Name')
    # plt.ylabel('Stock Level')
    # plt.xticks(rotation=90)
    # plt.tight_layout()
    # plt.show()

    # # 2. Calculate the average, maximum, and minimum selling prices for products
    # avg_price = product_data['selling_price'].mean()
    # max_price = product_data['selling_price'].max()
    # min_price = product_data['selling_price'].min()

    # # Create a bar chart for average, maximum, and minimum selling prices
    # plt.figure(figsize=(8, 5))
    # plt.bar(['Average', 'Maximum', 'Minimum'], [avg_price, max_price, min_price], color=['blue', 'green', 'red'])
    # plt.title('Average, Maximum, and Minimum Selling Prices for Products')
    # plt.ylabel('Price')
    # plt.tight_layout()
    # plt.show()


    ### Order Analysis
    
    # # 1. Calculate the top 10 orders product-wise
    # top_10_products_by_order = order_data.groupby('product_id')['quantity'].sum().nlargest(10).reset_index()
    # top_10_products_by_order = top_10_products_by_order.merge(product_data[['product_id', 'product_name']], on='product_id')

    # # Create a bar chart for the top 10 orders product-wise
    # plt.figure(figsize=(10, 6))
    # plt.bar(top_10_products_by_order['product_name'], top_10_products_by_order['quantity'], color='purple')
    # plt.title('Top 10 Orders Product-Wise')
    # plt.xlabel('Product Name')
    # plt.ylabel('Total Quantity Ordered')
    # plt.xticks(rotation=90)
    # plt.tight_layout()
    # plt.show()


    # # 2. Analyze the order status distribution (e.g., pending, delivered)
    # order_status_distribution = order_data['order_status'].value_counts()

    # # Create a bar chart for the order status distribution
    # plt.figure(figsize=(8, 5))
    # order_status_distribution.plot(kind='bar', color='cyan')
    # plt.title('Order Status Distribution')
    # plt.xlabel('Order Status')
    # plt.ylabel('Number of Orders')
    # plt.xticks(rotation=0)
    # plt.tight_layout()
    # plt.show()



    ### Popular Products Analysis
    
    # # Identify the most popular products based on order quantity (horizontal bar chart)
    # popular_products = order_data.groupby('product_id')['quantity'].sum().reset_index()
    # popular_products = popular_products.merge(product_data[['product_id', 'product_name']], on='product_id')
    # popular_products = popular_products.sort_values('quantity', ascending=True)

    # # Create a horizontal bar chart for the most popular products
    # plt.figure(figsize=(10, 6))
    # plt.barh(popular_products['product_name'], popular_products['quantity'], color='coral')
    # plt.title('Most Popular Products Based on Order Quantity')
    # plt.xlabel('Total Quantity Ordered')
    # plt.ylabel('Product Name')
    # plt.tight_layout()
    # plt.show()


    ### Sales Analysis
    
    # # 1. Calculate total revenue generated from orders product-wise
    # product_revenue = order_data.groupby('product_id')['total_price'].sum().reset_index()
    # product_revenue = product_revenue.merge(product_data[['product_id', 'product_name']], on='product_id')

    # # Create a bar chart for total revenue generated from orders product-wise
    # plt.figure(figsize=(10, 6))
    # plt.bar(product_revenue['product_name'], product_revenue['total_price'], color='skyblue')
    # plt.title('Total Revenue Generated from Orders Product-Wise')
    # plt.xlabel('Product Name')
    # plt.ylabel('Total Revenue')
    # plt.xticks(rotation=90)
    # plt.tight_layout()
    # plt.show()


    # # 2. Calculate total revenue product category wise percentage (Pie Chart)
    # # Merge product data with order data to get categories
    # merged_data = order_data.merge(product_data[['product_id', 'category']], on='product_id')
    # category_revenue = merged_data.groupby('category')['total_price'].sum()

    # # Plotting a pie chart for revenue distribution across product categories
    # plt.figure(figsize=(5, 3))
    # plt.pie(category_revenue, labels=category_revenue.index, autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired(np.arange(len(category_revenue))))
    # plt.title('Total Revenue Percentage by Product Category')
    # plt.axis('equal')
    # plt.tight_layout()
    # plt.show()

    # # 3. Analyze the performance of different product categories in terms of sales
    # merged_data = order_data.merge(product_data[['product_id', 'category']], on='product_id')
    # category_performance = merged_data.groupby('category')['quantity'].sum()

    # # Plotting a bar chart for performance of different product categories
    # plt.figure(figsize=(10, 6))
    # category_performance.plot(kind='bar', color='teal')
    # plt.title('Performance of Different Product Categories in Terms of Sales')
    # plt.xlabel('Category')
    # plt.ylabel('Total Quantity Sold')
    # plt.xticks(rotation=45)
    # plt.tight_layout()
    # plt.show()

    # # 4. Identify the most profitable products based on the difference between original and selling prices
    # product_data['profit'] = product_data['selling_price'] - product_data['original_price']
    # most_profitable_products = product_data.sort_values('profit', ascending=False).head(10)

    # # Plotting a bar chart for the most profitable products
    # plt.figure(figsize=(10, 6))
    # plt.bar(most_profitable_products['product_name'], most_profitable_products['profit'], color='gold')
    # plt.title('Top 10 Most Profitable Products')
    # plt.xlabel('Product Name')
    # plt.ylabel('Profit (Selling Price - Original Price)')
    # plt.xticks(rotation=90)
    # plt.tight_layout()
    # plt.show()


    # 1. Identify product names with the highest and lowest order quantities
    # product_order_quantity = order_data.groupby('product_id')['quantity'].sum().reset_index()
    # product_order_quantity = product_order_quantity.merge(product_data[['product_id', 'product_name']], on='product_id')

    # # Highest and Lowest Order Quantities
    # highest_orders = product_order_quantity.sort_values('quantity', ascending=False).head(10)
    # lowest_orders = product_order_quantity.sort_values('quantity').head(10)

    # # Plotting bar chart for products with the highest order quantities
    # plt.figure(figsize=(10, 6))
    # plt.bar(highest_orders['product_name'], highest_orders['quantity'], color='green')
    # plt.title('Top 10 Products with Highest Order Quantities')
    # plt.xlabel('Product Name')
    # plt.ylabel('Order Quantity')
    # plt.xticks(rotation=90)
    # plt.tight_layout()
    # plt.show()

    # # Plotting bar chart for products with the lowest order quantities
    # plt.figure(figsize=(10, 6))
    # plt.bar(lowest_orders['product_name'], lowest_orders['quantity'], color='red')
    # plt.title('Top 10 Products with Lowest Order Quantities')
    # plt.xlabel('Product Name')
    # plt.ylabel('Order Quantity')
    # plt.xticks(rotation=90)
    # plt.tight_layout()
    # plt.show()

    # # 2. Identify customers with the highest and lowest order quantities by customer name
    # customer_order_quantity = order_data.groupby('customer_id')['quantity'].sum().reset_index()
    # customer_order_quantity = customer_order_quantity.merge(customer_data[['customer_id', 'name']], on='customer_id')

    # # Highest and Lowest Order Quantities by Customer
    # highest_customers = customer_order_quantity.sort_values('quantity', ascending=False).head(10)
    # lowest_customers = customer_order_quantity.sort_values('quantity').head(10)

    # # Plotting bar chart for customers with the highest order quantities
    # plt.figure(figsize=(10, 6))
    # plt.bar(highest_customers['name'], highest_customers['quantity'], color='blue')
    # plt.title('Top 10 Customers with Highest Order Quantities')
    # plt.xlabel('Customer Name')
    # plt.ylabel('Order Quantity')
    # plt.xticks(rotation=90)
    # plt.tight_layout()
    # plt.show()

    # # Plotting bar chart for customers with the lowest order quantities
    # plt.figure(figsize=(10, 6))
    # plt.bar(lowest_customers['name'], lowest_customers['quantity'], color='orange')
    # plt.title('Top 10 Customers with Lowest Order Quantities')
    # plt.xlabel('Customer Name')
    # plt.ylabel('Order Quantity')
    # plt.xticks(rotation=90)
    # plt.tight_layout()
    # plt.show()

    # # 3. Determine the most preferred payment modes
    # payment_mode_counts = order_data['payment_mode'].value_counts()

    # # Plotting bar chart for most preferred payment modes
    # plt.figure(figsize=(8, 5))
    # plt.bar(payment_mode_counts.index, payment_mode_counts.values, color='purple')
    # plt.title('Most Preferred Payment Modes')
    # plt.xlabel('Payment Mode')
    # plt.ylabel('Number of Orders')
    # plt.xticks(rotation=45)
    # plt.tight_layout()
    # plt.show()

    # # Time-based Analysis

    # # 4. Month-wise total sales
    # order_data['order_month'] = pd.to_datetime(order_data['order_date']).dt.to_period('M')
    # monthly_sales = order_data.groupby('order_month')['total_price'].sum()

    # # Plotting bar chart for month-wise total sales
    # plt.figure(figsize=(10, 6))
    # monthly_sales.plot(kind='bar', color='cyan')
    # plt.title('Month-wise Total Sales')
    # plt.xlabel('Month')
    # plt.ylabel('Total Sales')
    # plt.xticks(rotation=45)
    # plt.tight_layout()
    # plt.show()

    # # 5. Month and year wise total sales
    # order_data['order_year_month'] = pd.to_datetime(order_data['order_date']).dt.to_period('M')
    # year_month_sales = order_data.groupby('order_year_month')['total_price'].sum()

    # # Plotting bar chart for month and year-wise total sales
    # plt.figure(figsize=(12, 6))
    # year_month_sales.plot(kind='bar', color='skyblue')
    # plt.title('Month and Year-wise Total Sales')
    # plt.xlabel('Year-Month')
    # plt.ylabel('Total Sales')
    # plt.xticks(rotation=45)
    # plt.tight_layout()
    # plt.show()

    # # 6. Identify peak order date
    # order_date_sales = order_data.groupby('order_date')['total_price'].sum()

    # # Plotting bar chart for peak order date
    # plt.figure(figsize=(12, 6))
    # order_date_sales.plot(kind='bar', color='magenta')
    # plt.title('Total Sales by Order Date')
    # plt.xlabel('Order Date')
    # plt.ylabel('Total Sales')
    # plt.xticks(rotation=45)
    # plt.tight_layout()
    # plt.show()

    # # Geographical Analysis

    # # 7. Explore the distribution of customers across different cities
    # city_distribution = customer_data['city'].value_counts()

    # # Plotting bar chart for customer distribution across cities
    # plt.figure(figsize=(10, 6))
    # plt.bar(city_distribution.index, city_distribution.values, color='brown')
    # plt.title('Distribution of Customers Across Different Cities')
    # plt.xlabel('City')
    # plt.ylabel('Number of Customers')
    # plt.xticks(rotation=90)
    # plt.tight_layout()
    # plt.show()

    # # 8. Analyze whether certain products or categories are more popular in a specific city
    # city_product_data = merged_data.groupby(['city', 'category'])['quantity'].sum().unstack().fillna(0)

    # # Plotting bar chart for product popularity across cities
    # city_product_data.plot(kind='bar', stacked=True, figsize=(14, 7), colormap='tab20')
    # plt.title('Product Popularity Across Cities')
    # plt.xlabel('City')
    # plt.ylabel('Total Quantity Sold')
    # plt.xticks(rotation=90)
    # plt.tight_layout()
    # plt.show()

    # # Product Performance

    # # 9. Identify the top 10 best-selling products
    # best_selling_products = product_order_quantity.sort_values('quantity', ascending=False).head(10)

    # # Plotting bar chart for top 10 best-selling products
    # plt.figure(figsize=(10, 6))
    # plt.bar(best_selling_products['product_name'], best_selling_products['quantity'], color='darkgreen')
    # plt.title('Top 10 Best-Selling Products')
    # plt.xlabel('Product Name')
    # plt.ylabel('Total Quantity Sold')
    # plt.xticks(rotation=90)
    # plt.tight_layout()
    # plt.show()

    # # 10. Identify top 10 slow-moving products based on low sales
    # slow_moving_products = product_order_quantity.sort_values('quantity').head(10)

    # # Plotting bar chart for top 10 slow-moving products
    # plt.figure(figsize=(10, 6))
    # plt.bar(slow_moving_products['product_name'], slow_moving_products['quantity'], color='gray')
    # plt.title('Top 10 Slow-Moving Products')
    # plt.xlabel('Product Name')
    # plt.ylabel('Total Quantity Sold')
    # plt.xticks(rotation=90)
    # plt.tight_layout()
    # plt.show()

    # # Customer Retention

    # # 11. Analyze repeat customers and their order patterns
    # repeat_customers = order_data.groupby('customer_id').size().reset_index(name='order_count')
    # repeat_customers = repeat_customers[repeat_customers['order_count'] > 1].merge(customer_data[['customer_id', 'name']], on='customer_id')

    # # Plotting bar chart for repeat customers and their order patterns
    # plt.figure(figsize=(10, 6))
    # plt.bar(repeat_customers['name'], repeat_customers['order_count'], color='navy')
    # plt.title('Repeat Customers and Their Order Patterns')
    # plt.xlabel('Customer Name')
    # plt.ylabel('Number of Orders')
    # plt.xticks(rotation=90)
    # plt.tight_layout()
    # plt.show()

    # # Payment Analysis

    # # 12. Display successful and pending payments order counts
    # payment_status_counts = order_data['order_status'].value_counts()

    # # Plotting bar chart for successful and pending payments order counts
    # plt.figure(figsize=(8, 5))
    # plt.bar(payment_status_counts.index, payment_status_counts.values, color='indigo')
    # plt.title('Successful and Pending Payments Order Counts')
    # plt.xlabel('Order Status')
    # plt.ylabel('Number of Orders')
    # plt.xticks(rotation=45)
    # plt.tight_layout()
    # plt.show()


    # Step 3: Close the Database Connection
    if connection and connection.is_connected():
        connection.close()
        print("Database connection closed.")