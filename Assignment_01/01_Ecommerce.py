# Question:
# 1. The Problem: E-Commerce Order Processing SystemYou are building a backend module for an e-commerce platform. You are given a list of raw transaction logs. Each transaction is represented as a Tuple containing (customer_id, product_name, order_amount).  Filter with Lists: Extract all orders where the order_amount is greater than $50 into a new List.Track Unique Products with Sets: Create a Set of all unique product names purchased across all transactions to see what inventory is in demand.Aggregate with Dictionaries: Create a Dictionary where the key is the customer_id and the value is their total spending amount. 



# Code:
transactions = [
    ("C101", "Laptop", 1200.0),
    ("C102", "Mouse", 25.0),
    ("C101", "Keyboard", 75.0),
    ("C103", "Monitor", 300.0),
    ("C102", "MousePad", 15.0),
    ("C103", "Laptop", 1200.0)
]

# 1. Filter orders > $50
high_value_orders = [tx for tx in transactions if tx[2] > 50]

# 2. Track unique products
unique_products = {tx[1] for tx in transactions}

# 3. Aggregate customer spending
customer_spending = {}
for customer_id, _, amount in transactions:
    customer_spending[customer_id] = customer_spending.get(customer_id, 0.0) + amount

print("High-Value Orders:", high_value_orders)
print("Unique Products:", unique_products)
print("Customer Spending:", customer_spending)



# Output:
# High-Value Orders: [('C101', 'Laptop', 1200.0), ('C101', 'Keyboard', 75.0), ('C103', 'Monitor', 300.0), ('C103', 'Laptop', 1200.0)]
# Unique Products: {'Monitor', 'Mouse', 'Laptop', 'Keyboard', 'MousePad'}
# Customer Spending: {'C101': 1275.0, 'C102': 40.0, 'C103': 1500.0}