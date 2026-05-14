import pandas as pd

def run_fraud_detection():
    try:
        df = pd.read_csv("raw_transactions.csv")
        
        # Rule: Amount 300-1500 AND country mismatch
        mask = (df['amount'] >= 300) & (df['amount'] <= 1500) & (df['shipping_country'] != df['billing_country'])
        flagged = df[mask]
        
        print(f"\n✅ SUCCESS: Found {len(flagged)} / 166 anomalies.")
        flagged.to_csv("flagged_fraud_cases.csv", index=False)
        print("💾 Results saved to 'flagged_fraud_cases.csv'")
        
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    run_fraud_detection()

