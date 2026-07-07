import pandas as pd
import matplotlib.pyplot as plt

# =========================
# 1. LOAD DATA
# =========================
df = pd.read_csv("retail_sales_dataset.csv")

print("DATA LOADED")
print(df.head())

# =========================
# 2. DATA CLEANING
# =========================
print("\nNULL VALUES:\n", df.isnull().sum())
print("\nDUPLICATES:", df.duplicated().sum())

df = df.drop_duplicates()

# =========================
# 3. BASIC KPI
# =========================
total_revenue = df["Total Amount"].sum()
total_quantity = df["Quantity"].sum()
avg_sales = df["Total Amount"].mean()

print("\n===== KPI =====")
print("Total Revenue:", total_revenue)
print("Total Quantity:", total_quantity)
print("Average Sales:", avg_sales)

# =========================
# 4. CATEGORY ANALYSIS
# =========================
category_sales = df.groupby("Product Category")["Total Amount"].sum()

print("\nCATEGORY SALES:\n", category_sales)

# BAR GRAPH
plt.figure()
category_sales.plot(kind="bar")
plt.title("Category Wise Sales")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig("category_sales.png")
plt.show()

# =========================
# 5. GENDER ANALYSIS
# =========================
gender_sales = df.groupby("Gender")["Total Amount"].sum()

plt.figure()
gender_sales.plot(kind="pie", autopct="%1.1f%%")
plt.title("Gender Wise Sales")
plt.ylabel("")
plt.tight_layout()
plt.savefig("gender_sales.png")
plt.show()

# =========================
# 6. MONTHLY TREND
# =========================
df["Date"] = pd.to_datetime(df["Date"])

monthly_sales = df.groupby(df["Date"].dt.to_period("M"))["Total Amount"].sum()

plt.figure()
monthly_sales.plot(kind="line", marker="o")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig("monthly_sales.png")
plt.show()

# =========================
# 7. SAVE FINAL OUTPUT FILE
# =========================
df.to_csv("cleaned_retail_data.csv", index=False)

print("\nPROJECT COMPLETED SUCCESSFULLY")
print("Charts saved as PNG files")
print("Cleaned data saved as CSV")