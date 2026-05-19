import pandas as pd
import numpy as np

print("🚀 Starting Day 4: Feature Engineering & Behavioral Profiling...")

# 1. Load the dataset
try:
    df = pd.read_csv("../Day-03-Data-Aggregation/raw_transactions.csv")
    print(f"✅ Successfully loaded dataset with {len(df)} rows.")
except FileNotFoundError:
    print("❌ Error: '../Day-03-Data-Aggregation/raw_transactions.csv' not found.")
    exit()

# Ensure timestamp is in datetime format for time-based metrics
df['timestamp'] = pd.to_datetime(df['timestamp'])

# Sort by user and time so we can calculate gaps between orders
df = df.sort_values(by=['user_id', 'timestamp']).reset_index(drop=True)

print("\nEngineering behavioral features...")

# Feature 1: User Transaction Velocity (Time difference between consecutive orders)
df['time_since_last_order_min'] = df.groupby('user_id')['timestamp'].diff().dt.total_seconds() / 60.0
df['time_since_last_order_min'] = df['time_since_last_order_min'].fillna(9999)

# Feature 2: Historical Order Count (Rolling frequency)
df['user_order_count'] = df.groupby('user_id').cumcount() + 1

# Feature 3: Device Shifting Flag (Updated to use 'device_id')
df['prev_device_id'] = df.groupby('user_id')['device_id'].shift(1)
df['device_changed'] = (df['device_id'] != df['prev_device_id']) & (df['prev_device_id'].notna())
df['device_changed'] = df['device_changed'].astype(int)

# Drop the temporary column used for calculation
df = df.drop(columns=['prev_device_id'])

# 2. Isolate highly suspicious behavioral patterns
# Flag transactions where a user makes a new order within less than 10 minutes of their last one
high_velocity_fraud = df[df['time_since_last_order_min'] < 10]

print("\n--- Day 4 Behavioral Insights ---")
print(f"🔹 Total transactions engineered: {len(df)}")
print(f"🚨 High-Velocity Alerts (Orders under 10 mins apart): {len(high_velocity_fraud)}")
print(f"📱 Instances of device-switching between consecutive orders: {df['device_changed'].sum()}")

# 3. Save the newly engineered dataset
df.to_csv("engineered_fraud_data.csv", index=False)
print("\n💾 Saved updated dataset with new features to 'engineered_fraud_data.csv'!")
