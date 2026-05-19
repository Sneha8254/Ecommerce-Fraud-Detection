# 🛡️ E-Commerce Fraud Detection & Automation Pipeline

A self-initiated 7-day data engineering and analytics project. This repository contains an end-to-end simulation pipeline that generates synthetic e-commerce transactions, performs automated fraud analysis, engineers behavioral risk features, and creates visual risk dashboards.

---

## ⚙️ Architecture Overview

The project is structured as a sequential multi-day pipeline orchestrated by a master automation controller:

```text
[Day 3: Data Generation] ──> (raw_transactions.csv)
                                      │
                                      ▼
[Day 4: Feature Engineering] ──> (engineered_fraud_data.csv)
                                      │
                                      ▼
[Day 5: Data Visualization] ──> (Risk Reports & PNG Charts)

