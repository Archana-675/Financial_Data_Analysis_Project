import os
import pandas as pd
import matplotlib.pyplot as plt

# ----------------------------
# Load dataset
# ----------------------------
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATASET_PATH = os.path.join(BASE_DIR, "dataset", "personal_finance.csv")

df = pd.read_csv(DATASET_PATH)

print("Dataset loaded successfully")
print("Columns:", df.columns)

# ----------------------------
# Date processing
# ----------------------------
df['Date'] = pd.to_datetime(df['Date'])
df['Month'] = df['Date'].dt.month

# ----------------------------
# Treat all records as expenses
# ----------------------------
total_expense = df['Amount'].sum()

print("\nFinancial Summary")
print("Total Expense:", total_expense)

# ----------------------------
# Expense by Category
# ----------------------------
category_expense = df.groupby('Category')['Amount'].sum()

plt.figure()
category_expense.plot(kind='bar')
plt.title("Expense by Category")
plt.xlabel("Category")
plt.ylabel("Amount")
plt.tight_layout()
plt.savefig(os.path.join(BASE_DIR, "output", "expense_by_category.png"))
plt.show()

# ----------------------------
# Monthly Expense Trend
# ----------------------------
monthly_expense = df.groupby('Month')['Amount'].sum()

plt.figure()
plt.plot(monthly_expense, marker='o')
plt.title("Monthly Expense Trend")
plt.xlabel("Month")
plt.ylabel("Amount")
plt.grid(True)
plt.tight_layout()
plt.savefig(os.path.join(BASE_DIR, "output", "monthly_expense_trend.png"))
plt.show()

print("\n✅ Analysis completed successfully")
