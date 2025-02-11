# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 14:31:00 2024

@author: Antonio
"""

from faker import Faker
import random
import pandas as pd

import os ## setup the working directory
os.chdir(r"C:\Users\Antonio\my_projects\my_database\raw_data")

# initialize faker
fake = Faker()

# constants
num_customer = 1000
product_names = [
    'Laptop', 'Smartphone', 'Tablet', 'Camera', 'Printer', 'Speaker', 'Mouse', 'USB', 'Keyboard', 'Headphones', 'Earphones'
    ]


# generate location. Done in this way to make it work with the customers random.choice
locations = []
for _ in range(225):
    location_id = len(locations)+1
    locations.append({
        'location_id': location_id,
        'country_name': fake.unique.country()
        })

locations_df = pd.DataFrame(locations)

# generate customers
customers = []
for _ in range(num_customer):
    customer_id = len(customers)+1
    customers.append({
        'customer_id': customer_id,
        'name': fake.name(),
        #'email': fake.email(),
        'location_id': random.choice(locations_df['location_id']),
        'address': fake.address(),
        'phone_number': fake.phone_number()
    })

# generate orders
from datetime import datetime
orders = []
for customer in customers:
    for _ in range(random.randint(1,100)): # to generate a random number of orders/customer
        order_id = len(orders) + 1
        orders.append({
            'order_id': order_id,
            'customer_id': customer['customer_id'],
            'product': random.choice(product_names),
            'quantity': random.randint(1,10),
            'price': round(random.uniform(10.0, 100.0), 2),
            'order_date': fake.date_between_dates(
                date_start=datetime(2024,1,1), date_end=datetime(2024,12,31)), #generate dates between date_start and date_end
        })

# create dataframes
customers_df = pd.DataFrame(customers)
orders_df = pd.DataFrame(orders)

# Export to CSV
customers_df.to_csv('customers.csv', index = False)
orders_df.to_csv('orders.csv', index = False)
locations_df.to_csv('locations.csv', index = False)




