import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

print("📊 Starting Day 5: Data Visualization & Risk Reporting...")

# 1. Load the engineered dataset from the Day 4 folder
data_path = "Day-04-Feature-Engineering/engineered_fraud_data.csv"
if not os.path.exists(data_path):
    print(f"❌ Error: Could not find {data_path}. Please check your folder structure.")
    exit()

df = pd.read_csv(data_path)
print(f"✅ Loaded dataset with {len(df)} rows for visualization.")

# Create a folder to save our charts
os.makedirs("Day-05-Data-Visualization", exist_ok=True)

# Set styling for professional-looking charts
sns.set_theme(style="whitegrid")
plt.figure(figsize=(10, 6))

# Chart 1: Top Fraud Hotspots (Shipping Country)
sns.countplot(data=df, x='shipping_country', order=df['shipping_country'].value_counts().index[:5], palette='Reds_r')
plt.title('Top 5 High-Risk Geographic Shipping Destinations', fontsize=14, fontweight='bold')
plt.xlabel('Country', fontsize=12)
plt.ylabel('Number of Fraudulent Transactions', fontsize=12)
plt.tight_layout()
plt.savefig('Day-05-Data-Visualization/top_fraud_countries.png', dpi=300)
plt.close()
print("📉 Saved: top_fraud_countries.png")

# Chart 2: Device Shifting vs. Consistent Devices
plt.figure(figsize=(6, 6))
device_counts = df['device_changed'].value_counts()
labels = ['Consistent Device', 'Device Switched']
colors = ['#4CAF50', '#FF5722']

plt.pie(device_counts, labels=labels, autopct='%1.1f%%', startangle=140, colors=colors, explode=(0, 0.1))
plt.title('Impact of Behavioral Anomaly:\nDevice Switching in Fraudulent Accounts', fontsize=12, fontweight='bold')
plt.tight_layout()
plt.savefig('Day-05-Data-Visualization/device_switching_distribution.png', dpi=300)
plt.close()
print("📉 Saved: device_switching_distribution.png")

print("\n🎉 Day 5 Visualizations generated successfully inside 'Day-05-Data-Visualization/' folder!")
