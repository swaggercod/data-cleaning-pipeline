import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Set random seed for reproducibility (Her seferinde aynı veriyi üretsin)
np.random.seed(42)

# Number of records
n_records = 1000

# Generate sample e-commerce data with INTENTIONAL PROBLEMS
data = {
    'order_id': range(1001, 1001 + n_records),
    
    # Customer names - some with extra spaces, mixed case
    'customer_name': np.random.choice([
        'John Doe', 'jane smith', 'ALICE WONG', '  Bob Johnson  ', 
        'Maria Garcia', None, 'Emma Wilson', 'Michael Brown  '
    ], n_records),
    
    # Email - some invalid, some null
    'email': np.random.choice([
        'john@email.com', 'jane@email.com', 'alice@invalid', 
        None, 'bob@email.com', 'not-an-email', 'maria@email.com'
    ], n_records),
    
    # Product category - inconsistent naming
    'category': np.random.choice([
        'Electronics', 'electronics', 'ELECTRONICS',
        'Clothing', 'clothing', 'Books', 'books',
        None, 'Home & Garden', 'home & garden'
    ], n_records),
    
    # Price - some negative (error), some outliers, some null
    'price': np.concatenate([
        np.random.uniform(10, 500, 950),  # Normal prices
        np.random.uniform(-50, -10, 20),  # Negative prices (error)
        [None] * 20,                       # Null values
        np.random.uniform(5000, 10000, 10) # Outliers
    ]),
    
    # Quantity - some zero, some negative, some null
    'quantity': np.concatenate([
        np.random.randint(1, 10, 950),
        np.random.randint(-5, 0, 20),  # Negative quantities
        [None] * 20,
        np.random.randint(0, 1, 10)    # Zero quantities
    ]),
    
    # Order date - some invalid formats, some future dates
    'order_date': np.random.choice([
        '2024-01-15', '2024/02/20', '15-03-2024',  # Different formats
        None, '2026-12-31',  # Future date
        '2024-01-01', '2024-02-14', '2023-11-20'
    ], n_records),
    
    # Payment status - inconsistent values
    'payment_status': np.random.choice([
        'Paid', 'paid', 'PAID', 'Pending', 'pending',
        'Failed', 'failed', None, 'Refunded', 'Unknown'
    ], n_records),
    
    # Customer rating - some out of range (1-5 expected)
    'customer_rating': np.concatenate([
        np.random.randint(1, 6, 950),  # Valid ratings 1-5
        np.random.randint(6, 11, 20),  # Invalid ratings
        [None] * 30
    ])
}

# Create DataFrame
df = pd.DataFrame(data)

# Shuffle the data
df = df.sample(frac=1, random_state=42).reset_index(drop=True)

# Add some duplicate rows (realistic problem)
duplicates = df.sample(50, random_state=42)
df = pd.concat([df, duplicates], ignore_index=True)

# Save to CSV
df.to_csv('data/raw/ecommerce_raw_data.csv', index=False)

print(f"✅ Generated {len(df)} records with intentional data quality issues")
print(f"📁 Saved to: data/raw/ecommerce_raw_data.csv")
print("\n📊 Problems included:")
print("- Missing values (nulls)")
print("- Inconsistent formatting (spaces, case)")
print("- Invalid data (negative prices, future dates)")
print("- Outliers")
print("- Duplicates")
print("- Inconsistent categories")
print("- Invalid email formats")