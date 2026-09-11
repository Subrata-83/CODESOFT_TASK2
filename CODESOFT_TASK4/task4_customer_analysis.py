# ============================================================
# CODSOFT DATA ANALYTICS INTERNSHIP
# TASK 4: CUSTOMER DATA ANALYSIS
# ============================================================

import pandas as pd
import matplotlib.pyplot as plt
import os
import tkinter as tk
from tkinter import filedialog


# ============================================================
# STEP 1: SELECT DATASET
# ============================================================

root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename(
    title="Select Customer Dataset",
    filetypes=[
        ("Excel Files", "*.xlsx *.xls"),
        ("CSV Files", "*.csv")
    ]
)

if not file_path:
    print("No file selected. Program stopped.")
    exit()


# ============================================================
# OUTPUT FOLDER
# ============================================================
# All output files will be saved in the same folder
# where this Python script is located.

folder_path = os.path.dirname(os.path.abspath(__file__))

print("\n============================================================")
print("OUTPUT FOLDER")
print("============================================================")
print(f"All output files will be saved to:\n{folder_path}")


# ============================================================
# STEP 2: LOAD DATASET
# ============================================================

if file_path.lower().endswith(".csv"):
    df = pd.read_csv(file_path)
else:
    df = pd.read_excel(file_path)

print("\n========== CUSTOMER DATASET LOADED SUCCESSFULLY ==========")

print("\nFirst 5 rows:")
print(df.head())

print("\nDataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns.tolist())

print("\nDataset Information:")
df.info()


# ============================================================
# STEP 3: CHECK MISSING VALUES
# ============================================================

print("\n========== MISSING VALUES ==========")

missing_values = df.isnull().sum()

print(missing_values)

print("\nTotal Missing Values:")
print(df.isnull().sum().sum())


# ============================================================
# STEP 4: HANDLE MISSING VALUES
# ============================================================

print("\n========== HANDLING MISSING VALUES ==========")

# Categorical columns
categorical_columns = ["Gender", "Location"]

for column in categorical_columns:

    if column in df.columns:

        if df[column].isnull().sum() > 0:

            df[column] = df[column].fillna(
                df[column].mode()[0]
            )


# Numerical columns
numerical_columns = [
    "Annual_Income",
    "Purchase_Amount"
]

for column in numerical_columns:

    if column in df.columns:

        if df[column].isnull().sum() > 0:

            df[column] = df[column].fillna(
                df[column].median()
            )


print("\nMissing values after cleaning:")
print(df.isnull().sum())

print("\nTotal Missing Values After Cleaning:")
print(df.isnull().sum().sum())


# ============================================================
# STEP 5: CHECK AND REMOVE DUPLICATES
# ============================================================

print("\n========== DUPLICATE RECORDS ==========")

duplicate_count = df.duplicated().sum()

print(
    f"Number of duplicate rows: "
    f"{duplicate_count}"
)

if duplicate_count > 0:

    df = df.drop_duplicates()


print(
    f"Duplicate rows after cleaning: "
    f"{df.duplicated().sum()}"
)


# ============================================================
# STEP 6: DATA TYPE CHECK
# ============================================================

print("\n========== DATA TYPES ==========")

print(df.dtypes)


# ============================================================
# STEP 7: FINAL DATA VERIFICATION
# ============================================================

print("\n========== FINAL DATA VERIFICATION ==========")

print(
    f"Total missing values: "
    f"{df.isnull().sum().sum()}"
)

print(
    f"Total duplicate rows: "
    f"{df.duplicated().sum()}"
)

print(
    f"Final dataset shape: "
    f"{df.shape}"
)


# ============================================================
# STEP 8: SAVE CLEANED DATASET
# ============================================================

cleaned_file = os.path.join(
    folder_path,
    "cleaned_customer_data.csv"
)

df.to_csv(
    cleaned_file,
    index=False
)

print("\n========== CLEANED DATASET SAVED ==========")

print(
    "File name: "
    "cleaned_customer_data.csv"
)

print(
    f"Saved location: "
    f"{cleaned_file}"
)

print(
    "\n========== TASK 4 DATA CLEANING COMPLETED =========="
)


# ============================================================
# STEP 9: CUSTOMER ANALYSIS
# ============================================================

print("\n========== CUSTOMER ANALYSIS ==========")


# ------------------------------------------------------------
# AGE ANALYSIS
# ------------------------------------------------------------

print("\n--- Age Analysis ---")

average_age = df["Age"].mean()

minimum_age = df["Age"].min()

maximum_age = df["Age"].max()

print(
    f"Average Customer Age: "
    f"{average_age:.2f}"
)

print(
    f"Minimum Customer Age: "
    f"{minimum_age}"
)

print(
    f"Maximum Customer Age: "
    f"{maximum_age}"
)


# ------------------------------------------------------------
# INCOME ANALYSIS
# ------------------------------------------------------------

print("\n--- Income Analysis ---")

average_income = df["Annual_Income"].mean()

highest_income = df["Annual_Income"].max()

lowest_income = df["Annual_Income"].min()

print(
    f"Average Annual Income: "
    f"{average_income:.2f}"
)

print(
    f"Highest Annual Income: "
    f"{highest_income}"
)

print(
    f"Lowest Annual Income: "
    f"{lowest_income}"
)


# ------------------------------------------------------------
# PURCHASE ANALYSIS
# ------------------------------------------------------------

print("\n--- Purchase Analysis ---")

average_purchase = df["Purchase_Amount"].mean()

highest_purchase = df["Purchase_Amount"].max()

average_frequency = df["Purchase_Frequency"].mean()

print(
    f"Average Purchase Amount: "
    f"{average_purchase:.2f}"
)

print(
    f"Highest Purchase Amount: "
    f"{highest_purchase:.2f}"
)

print(
    f"Average Purchase Frequency: "
    f"{average_frequency:.2f}"
)


# ------------------------------------------------------------
# PRODUCT CATEGORY ANALYSIS
# ------------------------------------------------------------

print("\n--- Product Category Analysis ---")

product_analysis = df.groupby(
    "Product_Category"
).agg(
    Customers=("Customer_ID", "count"),
    Total_Sales=("Purchase_Amount", "sum"),
    Average_Spending=("Purchase_Amount", "mean")
)

print(product_analysis)


# ------------------------------------------------------------
# LOCATION ANALYSIS
# ------------------------------------------------------------

print("\n--- Location Analysis ---")

location_analysis = df.groupby(
    "Location"
).agg(
    Customers=("Customer_ID", "count"),
    Total_Sales=("Purchase_Amount", "sum"),
    Average_Spending=("Purchase_Amount", "mean")
).sort_values(
    by="Total_Sales",
    ascending=False
)

print(location_analysis)


# ------------------------------------------------------------
# LOYALTY STATUS ANALYSIS
# ------------------------------------------------------------

print("\n--- Loyalty Status Analysis ---")

loyalty_analysis = df.groupby(
    "Loyalty_Status"
).agg(
    Customers=("Customer_ID", "count"),
    Total_Sales=("Purchase_Amount", "sum"),
    Average_Spending=("Purchase_Amount", "mean")
)

print(loyalty_analysis)


# ------------------------------------------------------------
# PURCHASE CHANNEL ANALYSIS
# ------------------------------------------------------------

print("\n--- Purchase Channel Analysis ---")

channel_analysis = df.groupby(
    "Purchase_Channel"
).agg(
    Customers=("Customer_ID", "count"),
    Total_Sales=("Purchase_Amount", "sum"),
    Average_Spending=("Purchase_Amount", "mean")
)

print(channel_analysis)


# ------------------------------------------------------------
# GENDER ANALYSIS
# ------------------------------------------------------------

print("\n--- Gender Analysis ---")

gender_analysis = df.groupby(
    "Gender"
).agg(
    Customers=("Customer_ID", "count"),
    Total_Sales=("Purchase_Amount", "sum"),
    Average_Spending=("Purchase_Amount", "mean")
)

print(gender_analysis)


# ------------------------------------------------------------
# TOP 10 CUSTOMERS BY PURCHASE AMOUNT
# ------------------------------------------------------------

print(
    "\n--- Top 10 Most Valuable Customers ---"
)

top_customers = df.nlargest(
    10,
    "Purchase_Amount"
)

print(
    top_customers[
        [
            "Customer_ID",
            "Age",
            "Location",
            "Purchase_Amount",
            "Loyalty_Status",
            "Spending_Score"
        ]
    ]
)


# ------------------------------------------------------------
# HIGH VALUE CUSTOMER GROUP
# ------------------------------------------------------------

print(
    "\n--- High-Value Customer Group ---"
)

high_value_customers = df[
    (df["Spending_Score"] >= 70)
    &
    (df["Purchase_Frequency"] >= 10)
]

print(
    f"Number of High-Value Customers: "
    f"{len(high_value_customers)}"
)

print(
    high_value_customers[
        [
            "Customer_ID",
            "Age",
            "Location",
            "Purchase_Frequency",
            "Purchase_Amount",
            "Loyalty_Status",
            "Spending_Score"
        ]
    ].head(10)
)


# ============================================================
# AGE GROUP ANALYSIS
# ============================================================

bins = [
    17,
    25,
    35,
    45,
    55,
    100
]

labels = [
    "18-25",
    "26-35",
    "36-45",
    "46-55",
    "56+"
]

df["Age_Group"] = pd.cut(
    df["Age"],
    bins=bins,
    labels=labels
)

print("\n--- Customer Age Groups ---")

age_group_analysis = df.groupby(
    "Age_Group",
    observed=False
).agg(
    Customers=("Customer_ID", "count"),
    Total_Sales=("Purchase_Amount", "sum"),
    Average_Spending=("Purchase_Amount", "mean")
)

print(age_group_analysis)


print(
    "\n========== CUSTOMER ANALYSIS COMPLETED =========="
)


# ============================================================
# STEP 10: DATA VISUALIZATION
# ============================================================

print(
    "\n========== DATA VISUALIZATION =========="
)

charts_folder = os.path.join(
    folder_path,
    "charts"
)

os.makedirs(
    charts_folder,
    exist_ok=True
)


# ------------------------------------------------------------
# CHART 1: SALES BY PRODUCT CATEGORY
# ------------------------------------------------------------

plt.figure(figsize=(10, 6))

product_analysis["Total_Sales"].plot(
    kind="bar"
)

plt.title(
    "Total Sales by Product Category"
)

plt.xlabel(
    "Product Category"
)

plt.ylabel(
    "Total Sales"
)

plt.xticks(
    rotation=45
)

plt.tight_layout()

plt.savefig(
    os.path.join(
        charts_folder,
        "sales_by_product_category.png"
    )
)

plt.close()


# ------------------------------------------------------------
# CHART 2: SALES BY LOCATION
# ------------------------------------------------------------

plt.figure(figsize=(10, 6))

location_analysis["Total_Sales"].plot(
    kind="bar"
)

plt.title(
    "Total Sales by Location"
)

plt.xlabel(
    "Location"
)

plt.ylabel(
    "Total Sales"
)

plt.xticks(
    rotation=45
)

plt.tight_layout()

plt.savefig(
    os.path.join(
        charts_folder,
        "sales_by_location.png"
    )
)

plt.close()


# ------------------------------------------------------------
# CHART 3: SALES BY LOYALTY STATUS
# ------------------------------------------------------------

plt.figure(figsize=(8, 5))

loyalty_analysis["Total_Sales"].plot(
    kind="bar"
)

plt.title(
    "Total Sales by Loyalty Status"
)

plt.xlabel(
    "Loyalty Status"
)

plt.ylabel(
    "Total Sales"
)

plt.xticks(
    rotation=0
)

plt.tight_layout()

plt.savefig(
    os.path.join(
        charts_folder,
        "sales_by_loyalty_status.png"
    )
)

plt.close()


# ------------------------------------------------------------
# CHART 4: SALES BY PURCHASE CHANNEL
# ------------------------------------------------------------

plt.figure(figsize=(8, 5))

channel_analysis["Total_Sales"].plot(
    kind="bar"
)

plt.title(
    "Total Sales by Purchase Channel"
)

plt.xlabel(
    "Purchase Channel"
)

plt.ylabel(
    "Total Sales"
)

plt.xticks(
    rotation=0
)

plt.tight_layout()

plt.savefig(
    os.path.join(
        charts_folder,
        "sales_by_purchase_channel.png"
    )
)

plt.close()


# ------------------------------------------------------------
# CHART 5: CUSTOMERS BY AGE GROUP
# ------------------------------------------------------------

plt.figure(figsize=(8, 5))

age_group_analysis["Customers"].plot(
    kind="bar"
)

plt.title(
    "Customers by Age Group"
)

plt.xlabel(
    "Age Group"
)

plt.ylabel(
    "Number of Customers"
)

plt.xticks(
    rotation=0
)

plt.tight_layout()

plt.savefig(
    os.path.join(
        charts_folder,
        "customers_by_age_group.png"
    )
)

plt.close()


# ------------------------------------------------------------
# CHART 6: INCOME VS PURCHASE AMOUNT
# ------------------------------------------------------------

plt.figure(figsize=(8, 5))

plt.scatter(
    df["Annual_Income"],
    df["Purchase_Amount"],
    alpha=0.6
)

plt.title(
    "Annual Income vs Purchase Amount"
)

plt.xlabel(
    "Annual Income"
)

plt.ylabel(
    "Purchase Amount"
)

plt.tight_layout()

plt.savefig(
    os.path.join(
        charts_folder,
        "income_vs_purchase_amount.png"
    )
)

plt.close()


# ------------------------------------------------------------
# CHART 7: SPENDING SCORE DISTRIBUTION
# ------------------------------------------------------------

plt.figure(figsize=(8, 5))

plt.hist(
    df["Spending_Score"],
    bins=10
)

plt.title(
    "Spending Score Distribution"
)

plt.xlabel(
    "Spending Score"
)

plt.ylabel(
    "Number of Customers"
)

plt.tight_layout()

plt.savefig(
    os.path.join(
        charts_folder,
        "spending_score_distribution.png"
    )
)

plt.close()


print(
    "\nAll charts created successfully!"
)

print(
    f"Charts saved in: "
    f"{charts_folder}"
)


# ============================================================
# STEP 11: SAVE ANALYSIS REPORTS
# ============================================================

print(
    "\n========== SAVING ANALYSIS REPORTS =========="
)


product_analysis.to_csv(
    os.path.join(
        folder_path,
        "product_category_analysis.csv"
    )
)


location_analysis.to_csv(
    os.path.join(
        folder_path,
        "location_analysis.csv"
    )
)


loyalty_analysis.to_csv(
    os.path.join(
        folder_path,
        "loyalty_analysis.csv"
    )
)


channel_analysis.to_csv(
    os.path.join(
        folder_path,
        "purchase_channel_analysis.csv"
    )
)


age_group_analysis.to_csv(
    os.path.join(
        folder_path,
        "age_group_analysis.csv"
    )
)


print(
    "Analysis reports saved successfully!"
)

print(
    "\n========== TASK 4 ANALYSIS COMPLETED =========="
)

print(
    "Customer analysis and visualization "
    "completed successfully."
)


# ============================================================
# STEP 12: CUSTOMER SEGMENTATION
# ============================================================

print(
    "\n========== CUSTOMER SEGMENTATION =========="
)


def assign_segment(row):

    if (
        row["Spending_Score"] >= 70
        and row["Purchase_Frequency"] >= 10
    ):

        return "High Value"

    elif (
        row["Loyalty_Status"]
        in ["Gold", "Platinum"]
        and row["Purchase_Frequency"] >= 8
    ):

        return "Loyal"

    elif (
        row["Spending_Score"] >= 40
        and row["Purchase_Frequency"] >= 6
    ):

        return "Potential"

    else:

        return "Low Engagement"


df["Customer_Segment"] = df.apply(
    assign_segment,
    axis=1
)


# ------------------------------------------------------------
# SEGMENT SUMMARY
# ------------------------------------------------------------

segment_analysis = df.groupby(
    "Customer_Segment"
).agg(
    Customers=("Customer_ID", "count"),
    Average_Income=("Annual_Income", "mean"),
    Average_Frequency=(
        "Purchase_Frequency",
        "mean"
    ),
    Average_Purchase=(
        "Purchase_Amount",
        "mean"
    ),
    Average_Spending_Score=(
        "Spending_Score",
        "mean"
    )
).sort_values(
    by="Customers",
    ascending=False
)


print(
    "\n--- Customer Segment Summary ---"
)

print(segment_analysis)


# ------------------------------------------------------------
# SALES BY SEGMENT
# ------------------------------------------------------------

segment_sales = df.groupby(
    "Customer_Segment"
)["Purchase_Amount"].sum().sort_values(
    ascending=False
)

print(
    "\n--- Sales by Customer Segment ---"
)

print(segment_sales)


# ------------------------------------------------------------
# SHOW CUSTOMERS BY SEGMENT
# ------------------------------------------------------------

for segment in [
    "High Value",
    "Loyal",
    "Potential",
    "Low Engagement"
]:

    print(
        f"\n--- {segment} Customers ---"
    )

    segment_customers = df[
        df["Customer_Segment"] == segment
    ]

    print(
        segment_customers[
            [
                "Customer_ID",
                "Age",
                "Location",
                "Purchase_Frequency",
                "Purchase_Amount",
                "Loyalty_Status",
                "Spending_Score"
            ]
        ].head(10)
    )


# ------------------------------------------------------------
# SAVE SEGMENTATION DATA
# ------------------------------------------------------------

customer_segments_file = os.path.join(
    folder_path,
    "customer_segments.csv"
)

customer_segment_summary_file = os.path.join(
    folder_path,
    "customer_segment_summary.csv"
)


df.to_csv(
    customer_segments_file,
    index=False
)


segment_analysis.to_csv(
    customer_segment_summary_file
)


# ------------------------------------------------------------
# SEGMENT CHART 1
# ------------------------------------------------------------

plt.figure(figsize=(8, 5))

segment_analysis["Customers"].plot(
    kind="bar"
)

plt.title(
    "Number of Customers by Segment"
)

plt.xlabel(
    "Customer Segment"
)

plt.ylabel(
    "Number of Customers"
)

plt.xticks(
    rotation=0
)

plt.tight_layout()

plt.savefig(
    os.path.join(
        charts_folder,
        "customer_segmentation.png"
    )
)

plt.close()


# ------------------------------------------------------------
# SEGMENT CHART 2
# ------------------------------------------------------------

plt.figure(figsize=(8, 5))

segment_sales.plot(
    kind="bar"
)

plt.title(
    "Total Sales by Customer Segment"
)

plt.xlabel(
    "Customer Segment"
)

plt.ylabel(
    "Total Sales"
)

plt.xticks(
    rotation=0
)

plt.tight_layout()

plt.savefig(
    os.path.join(
        charts_folder,
        "sales_by_customer_segment.png"
    )
)

plt.close()


print(
    "\n========== CUSTOMER SEGMENTATION COMPLETED =========="
)

print(
    f"Customer segment data saved as: "
    f"{customer_segments_file}"
)

print(
    f"Customer segment summary saved as: "
    f"{customer_segment_summary_file}"
)

print(
    f"Segmentation charts saved in: "
    f"{charts_folder}"
)


# ============================================================
# STEP 13: BUSINESS INSIGHTS
# ============================================================

print(
    "\n" + "=" * 60
)

print(
    "STEP 5: BUSINESS INSIGHTS & "
    "MARKETING RECOMMENDATIONS"
)

print(
    "=" * 60
)


# ------------------------------------------------------------
# KEY BUSINESS METRICS
# ------------------------------------------------------------

total_customers = len(df)

total_sales = df[
    "Purchase_Amount"
].sum()

average_purchase = df[
    "Purchase_Amount"
].mean()


# ------------------------------------------------------------
# BEST PRODUCT
# ------------------------------------------------------------

best_product = (
    df.groupby(
        "Product_Category"
    )["Purchase_Amount"]
    .sum()
    .sort_values(
        ascending=False
    )
)


# ------------------------------------------------------------
# BEST LOCATION
# ------------------------------------------------------------

best_location = (
    df.groupby(
        "Location"
    )["Purchase_Amount"]
    .sum()
    .sort_values(
        ascending=False
    )
)


# ------------------------------------------------------------
# BEST AGE GROUP
# ------------------------------------------------------------

best_age_group = (
    df.groupby(
        "Age_Group",
        observed=False
    )["Purchase_Amount"]
    .mean()
    .sort_values(
        ascending=False
    )
)


# ------------------------------------------------------------
# BEST PURCHASE CHANNEL
# ------------------------------------------------------------

best_channel = (
    df.groupby(
        "Purchase_Channel"
    )["Purchase_Amount"]
    .sum()
    .sort_values(
        ascending=False
    )
)


# ------------------------------------------------------------
# BEST LOYALTY STATUS
# ------------------------------------------------------------

loyalty_spending = (
    df.groupby(
        "Loyalty_Status"
    )["Purchase_Amount"]
    .mean()
    .sort_values(
        ascending=False
    )
)


# ------------------------------------------------------------
# CUSTOMER SEGMENT SIZE
# ------------------------------------------------------------

segment_customers = (
    df["Customer_Segment"]
    .value_counts()
    .sort_values(
        ascending=False
    )
)


# ------------------------------------------------------------
# CUSTOMER SEGMENT SALES
# ------------------------------------------------------------

segment_sales = (
    df.groupby(
        "Customer_Segment"
    )["Purchase_Amount"]
    .sum()
    .sort_values(
        ascending=False
    )
)


# ============================================================
# PRINT KEY BUSINESS INSIGHTS
# ============================================================

print(
    "\nKEY BUSINESS INSIGHTS"
)

print(
    "-" * 60
)


print(
    f"Total Customers: "
    f"{total_customers}"
)


print(
    f"Total Sales: "
    f"{total_sales:.2f}"
)


print(
    f"\nAverage Purchase Amount: "
    f"{average_purchase:.2f}"
)


print(
    f"\nBest Product Category by Total Sales: "
    f"{best_product.index[0]} "
    f"({best_product.iloc[0]:.2f})"
)


print(
    f"Best Location by Total Sales: "
    f"{best_location.index[0]} "
    f"({best_location.iloc[0]:.2f})"
)


print(
    f"Highest Spending Age Group: "
    f"{best_age_group.index[0]} "
    f"({best_age_group.iloc[0]:.2f} average)"
)


print(
    f"Dominant Purchase Channel by Total Sales: "
    f"{best_channel.index[0]} "
    f"({best_channel.iloc[0]:.2f})"
)


print(
    f"Highest Average Spending Loyalty Status: "
    f"{loyalty_spending.index[0]} "
    f"({loyalty_spending.iloc[0]:.2f})"
)


print(
    f"Largest Customer Segment: "
    f"{segment_customers.index[0]} "
    f"({segment_customers.iloc[0]} customers)"
)


print(
    f"Highest Sales Customer Segment: "
    f"{segment_sales.index[0]} "
    f"({segment_sales.iloc[0]:.2f})"
)


# ============================================================
# MARKETING RECOMMENDATIONS
# ============================================================

recommendations = [

    "1. High Value Customers: Offer VIP rewards, early access "
    "to new products, personalized offers, and exclusive "
    "discounts to improve retention.",

    "2. Potential Customers: Use targeted promotions, product "
    "recommendations, bundles, and loyalty upgrades to convert "
    "them into High Value customers.",

    "3. Loyal Customers: Provide exclusive membership benefits, "
    "repeat-purchase rewards, and personalized campaigns to "
    "maintain long-term loyalty.",

    "4. Low Engagement Customers: Run win-back campaigns, "
    "limited-time discounts, reminder messages, and personalized "
    "offers to increase engagement.",

    "5. Product Strategy: Focus promotional campaigns on "
    "high-performing product categories while using cross-selling "
    "and bundle offers for other categories.",

    "6. Location Strategy: Give additional promotional attention "
    "to locations with strong sales performance and create "
    "location-specific campaigns.",

    "7. Channel Strategy: Strengthen the online channel while "
    "encouraging omnichannel purchases through online-to-store "
    "and store-to-online offers.",

    "8. Loyalty Strategy: Provide higher-value rewards and "
    "personalized benefits to customers with stronger loyalty "
    "and purchasing activity."
]


print(
    "\nMARKETING RECOMMENDATIONS"
)

print(
    "-" * 60
)


for recommendation in recommendations:

    print(
        recommendation
    )


# ============================================================
# SAVE BUSINESS INSIGHTS
# ============================================================

insights_file = os.path.join(
    folder_path,
    "business_insights.txt"
)


with open(
    insights_file,
    "w",
    encoding="utf-8"
) as file:

    file.write(
        "CUSTOMER DATA ANALYSIS - BUSINESS INSIGHTS\n"
    )

    file.write(
        "=" * 60 + "\n\n"
    )

    file.write(
        "KEY BUSINESS METRICS\n"
    )

    file.write(
        "-" * 60 + "\n"
    )

    file.write(
        f"Total Customers: "
        f"{total_customers}\n"
    )

    file.write(
        f"Total Sales: "
        f"{total_sales:.2f}\n"
    )

    file.write(
        f"Average Purchase Amount: "
        f"{average_purchase:.2f}\n\n"
    )

    file.write(
        "KEY INSIGHTS\n"
    )

    file.write(
        "-" * 60 + "\n"
    )

    file.write(
        f"Best Product Category by Total Sales: "
        f"{best_product.index[0]} "
        f"({best_product.iloc[0]:.2f})\n"
    )

    file.write(
        f"Best Location by Total Sales: "
        f"{best_location.index[0]} "
        f"({best_location.iloc[0]:.2f})\n"
    )

    file.write(
        f"Highest Spending Age Group: "
        f"{best_age_group.index[0]} "
        f"({best_age_group.iloc[0]:.2f} average)\n"
    )

    file.write(
        f"Dominant Purchase Channel: "
        f"{best_channel.index[0]} "
        f"({best_channel.iloc[0]:.2f})\n"
    )

    file.write(
        f"Highest Average Spending Loyalty Status: "
        f"{loyalty_spending.index[0]} "
        f"({loyalty_spending.iloc[0]:.2f})\n"
    )

    file.write(
        f"Largest Customer Segment: "
        f"{segment_customers.index[0]} "
        f"({segment_customers.iloc[0]} customers)\n"
    )

    file.write(
        f"Highest Sales Customer Segment: "
        f"{segment_sales.index[0]} "
        f"({segment_sales.iloc[0]:.2f})\n\n"
    )

    file.write(
        "MARKETING RECOMMENDATIONS\n"
    )

    file.write(
        "-" * 60 + "\n"
    )

    for recommendation in recommendations:

        file.write(
            recommendation + "\n"
        )


print(
    f"\nBusiness insights saved to: "
    f"{insights_file}"
)


# ============================================================
# SAVE BUSINESS SUMMARY CSV
# ============================================================

business_summary = pd.DataFrame({

    "Metric": [

        "Total Customers",

        "Total Sales",

        "Average Purchase Amount",

        "Best Product Category",

        "Best Location",

        "Highest Spending Age Group",

        "Dominant Purchase Channel",

        "Highest Spending Loyalty Status",

        "Largest Customer Segment",

        "Highest Sales Customer Segment"
    ],

    "Value": [

        total_customers,

        round(
            total_sales,
            2
        ),

        round(
            average_purchase,
            2
        ),

        best_product.index[0],

        best_location.index[0],

        best_age_group.index[0],

        best_channel.index[0],

        loyalty_spending.index[0],

        segment_customers.index[0],

        segment_sales.index[0]
    ]
})


summary_file = os.path.join(
    folder_path,
    "business_summary.csv"
)


business_summary.to_csv(
    summary_file,
    index=False
)


print(
    f"Business summary saved to: "
    f"{summary_file}"
)


# ============================================================
# FINAL COMPLETION
# ============================================================

print(
    "\n" + "=" * 60
)

print(
    "TASK 4 COMPLETED SUCCESSFULLY"
)

print(
    "=" * 60
)

print(
    "Customer data cleaning, analysis, visualization, "
    "segmentation and business insights completed."
)

print(
    f"\nAll project outputs are available in:\n"
    f"{folder_path}"
)