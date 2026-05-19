#!/bin/bash

# Exit immediately if any script fails
set -e

# Store the root directory path
ROOT_DIR=$(pwd)

echo "🚀 [STARTING PIPELINE AUTOMATION]"
echo "================================="

# Step 1: Run Day 3 scripts
echo "🔄 Step 1: Generating and Aggregating Data..."
cd "$ROOT_DIR/Day-03-Data-Aggregation"
python3 generate_data.py
python3 analyze_fraud.py

# Step 2: Run Day 4 script
echo "🧠 Step 2: Engineering Behavioral Features..."
cd "$ROOT_DIR/Day-04-Feature-Engineering"
python3 feature_engineering.py

# Step 3: Run Day 5 script
echo "📊 Step 3: Generating Risk Reports and Charts..."
cd "$ROOT_DIR/Day-05-Data-Visualization"
python3 visualize_fraud.py

echo "================================="
echo "🎉 [PIPELINE EXECUTION COMPLETE! ALL SYSTEMS GREEN]"
