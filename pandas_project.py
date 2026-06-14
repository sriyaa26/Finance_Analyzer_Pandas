import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset
data = pd.read_csv("personal_finance_dataset.csv")

# Data Cleaning
data.dropna(inplace=True)

# Convert Date Column
data["Date"] = pd.to_datetime(data["Date"])

# Extract Date Features
data["Year"] = data["Date"].dt.year
data["Month"] = data["Date"].dt.month
data["Day"] = data["Date"].dt.day

# -----------------------------
# Payment Mode Analysis
# -----------------------------

most_used_payment = data["Payment_Mode"].value_counts().idxmax()
least_used_payment = data["Payment_Mode"].value_counts().idxmin()

payment_spending = data.groupby("Payment_Mode")["Amount"].sum()

# -----------------------------
# Category Analysis
# -----------------------------

most_common_category = data["Category"].mode()[0]
highest_spending_category = (
    data.groupby("Category")["Amount"].sum().idxmax()
)

# -----------------------------
# Monthly Analysis
# -----------------------------

monthly_spending = data.groupby("Month")["Amount"].sum()

highest_spending_month = monthly_spending.idxmax()
lowest_spending_month = monthly_spending.idxmin()

# -----------------------------
# High Value Transactions
# -----------------------------

high_value = data[data["Amount"] > 4000]

most_common_high_value_category = (
    high_value["Category"].value_counts().idxmax()
)

# -----------------------------
# Visualizations
# -----------------------------

# Category Spending
data.groupby("Category")["Amount"].sum().plot(kind="bar")
plt.title("Category Spending")
plt.xlabel("Category")
plt.ylabel("Amount")
plt.savefig("category_spending.png")
plt.close()

# Payment Mode Usage
data["Payment_Mode"].value_counts().plot(kind="bar")
plt.title("Payment Mode Usage")
plt.xlabel("Payment Mode")
plt.ylabel("Transactions")
plt.savefig("payment_mode_usage.png")
plt.close()

# Monthly Spending Trend
monthly_spending.plot(kind="line")
plt.title("Monthly Spending Trend")
plt.xlabel("Month")
plt.ylabel("Amount")
plt.savefig("monthly_spending.png")
plt.close()

# -----------------------------
# Final Report
# -----------------------------

print("===== PERSONAL FINANCE REPORT =====")
print("Most Used Payment Mode:", most_used_payment)
print("Least Used Payment Mode:", least_used_payment)
print("Most Common Category:", most_common_category)
print("Highest Spending Category:", highest_spending_category)
print("Highest Spending Month:", highest_spending_month)
print("Lowest Spending Month:", lowest_spending_month)
print("Most Common High Value Category:", most_common_high_value_category)
