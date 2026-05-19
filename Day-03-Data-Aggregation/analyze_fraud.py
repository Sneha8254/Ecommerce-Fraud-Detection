import pandas as pd

def run_fraud_analysis():
    try:
        try:
            df = pd.read_csv("Day-02-Fraud-Detection/raw_transactions.csv")
        except FileNotFoundError:
            df = pd.read_csv("raw_transactions.csv")
            
        print("\n📊 --- E-COMMERCE FRAUD ANALYSIS REPORT --- 📊\n")
        
        # 1. Total Financial Risk
        total_risk = df['amount'].sum()
        print(f"💰 Total Financial Amount at Risk: ${total_risk:,.2f}")
        
        # 2. Average Fraudulent Transaction Value
        avg_fraud_value = df['amount'].mean()
        print(f"💳 Average Fraudulent Order Value: ${avg_fraud_value:,.2f}\n")
        
        # 3. Top 5 Fraud Hotspots
        print("🗺️ Top 5 Shipping Countries with Highest Fraud Volume:")
        country_counts = df['shipping_country'].value_counts().head(5)
        
        for country, count in country_counts.items():
            print(f"   • {country}: {count} cases")
            
    except FileNotFoundError:
        print("❌ Error: Could not find 'raw_transactions.csv' anywhere in this directory.")

if __name__ == "__main__":
    run_fraud_analysis()
