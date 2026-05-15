import csv
import random
from datetime import datetime, timedelta
from faker import Faker
import pandas as pd

fake = Faker()
Faker.seed(42)
random.seed(42)

def generate_fraud_dataset(num_records=10000):
    print(f"🚀 Generating {num_records} synthetic e-commerce transactions...")
    user_ids = [f"USER_{1000 + i}" for i in range(500)]
    device_ids = [f"DEV_{5000 + i}" for i in range(50)]
    dataset = []
    start_time = datetime(2026, 1, 1)

    for i in range(num_records):
        tx_id = f"TXN_{100000 + i}"
        user_id = random.choice(user_ids)
        device_id = random.choice(device_ids)
        timestamp = start_time + timedelta(minutes=random.randint(1, 15) * i)
        amount = round(random.gammavariate(1, 50.0) + 5.0, 2)
        ip_address = fake.ipv4()
        shipping_country = fake.country_code()
        billing_country = shipping_country
        is_fraud = 0 
        
        if random.random() < 0.015:
            is_fraud = 1
            amount = round(random.uniform(300.0, 1500.0), 2)
            billing_country = fake.country_code()
            
        dataset.append([
            tx_id, user_id, timestamp.strftime('%Y-%m-%d %H:%M:%S'), 
            amount, ip_address, device_id, shipping_country, billing_country, is_fraud
        ])
        
    columns = ['transaction_id', 'user_id', 'timestamp', 'amount', 'ip_address', 
               'device_id', 'shipping_country', 'billing_country', 'is_fraud']
    df = pd.DataFrame(dataset, columns=columns)
    df.to_csv('raw_transactions.csv', index=False)
    print("✅ Success! 'raw_transactions.csv' created and saved.")
    print(f"📊 Total Fraud Events Injected: {df['is_fraud'].sum()} ({df['is_fraud'].mean()*100:.2f}%)")
    return df

df_clean = generate_fraud_dataset()
