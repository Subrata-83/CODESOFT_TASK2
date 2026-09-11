# CODESOFT_TASK4



## CodSoft Data Analytics Internship - Task 4

This project focuses on analyzing customer data to understand customer behavior, purchasing patterns, customer segments, and business performance using Python.

## Objective

The main objectives of this project are:

- Analyze customer information and purchasing behavior
- Clean and preprocess the customer dataset
- Identify valuable customer groups
- Perform customer segmentation
- Analyze sales based on different factors
- Create visualizations and reports
- Generate useful business insights and marketing recommendations

## Dataset

The dataset contains 1,000 customer records with the following attributes:

- Customer_ID
- Age
- Gender
- Location
- Annual_Income
- Purchase_Frequency
- Purchase_Amount
- Product_Category
- Purchase_Channel
- Loyalty_Status
- Membership_Years
- Spending_Score

## Technologies Used

- Python
- Pandas
- Matplotlib
- OpenPyXL
- Tkinter

## Data Cleaning

The following data preprocessing steps were performed:

1. Loaded the customer dataset.
2. Inspected the dataset structure and data types.
3. Identified missing values.
4. Filled missing categorical values using the mode.
5. Filled missing numerical values using the median.
6. Checked for duplicate records.
7. Removed duplicate records if found.
8. Verified the cleaned dataset.
9. Saved the cleaned dataset as a CSV file.

## Data Analysis

The following analyses were performed:

- Customer age analysis
- Annual income analysis
- Purchase frequency analysis
- Purchase amount analysis
- Product category analysis
- Location-wise sales analysis
- Loyalty status analysis
- Purchase channel analysis
- Gender-wise analysis
- Age-group analysis
- Spending score analysis
- Top customers by purchase amount
- High-value customer analysis

## Customer Segmentation

Customers were divided into four segments based on their spending behavior, purchase frequency, and loyalty status.

### High Value

Spending Score >= 70 and Purchase Frequency >= 10

### Loyal

Gold or Platinum loyalty status and Purchase Frequency >= 8

### Potential

Spending Score >= 40 and Purchase Frequency >= 6

### Low Engagement

Customers who do not meet the above conditions.

### Segmentation Results

| Customer Segment | Number of Customers |
|------------------|---------------------|
| Low Engagement | 414 |
| Potential | 271 |
| Loyal | 170 |
| High Value | 145 |

## Key Results

- Total Customers: **1,000**
- Total Purchase Amount: **366,808.86**
- Average Purchase Amount: **366.81**
- Best Performing Product Category: **Sports**
- Sports Total Sales: **82,106.74**
- Highest Sales Location: **Siliguri**
- Siliguri Total Sales: **41,933.45**
- Most Used Purchase Channel: **Online**
- Online Total Sales: **201,960.42**
- Highest Average Spending Age Group: **18-25**
- Highest Average Spending Loyalty Group: **Silver**
- Largest Customer Segment: **Low Engagement**
- Highest Sales Customer Segment: **Potential**
- High Value Customers: **145**

## Visualizations

The project generates the following visualizations:

1. Sales by Product Category
2. Sales by Location
3. Sales by Loyalty Status
4. Sales by Purchase Channel
5. Customers by Age Group
6. Income vs Purchase Amount
7. Spending Score Distribution
8. Customer Segmentation
9. Sales by Customer Segment

All charts are stored inside the `charts` folder.

## Business Insights

### High Value Customers
High-value customers have strong spending scores and frequent purchases. They can be targeted with premium offers and exclusive rewards.

### Potential Customers
Potential customers can be encouraged to increase their purchase frequency through targeted promotions and personalized recommendations.

### Loyal Customers
Gold and Platinum customers can be retained through loyalty rewards, exclusive discounts, and membership benefits.

### Low Engagement Customers
Re-engagement campaigns, personalized offers, and special discounts can be used to increase their activity.

### Product Strategy
Sports generated the highest total purchase amount among the product categories. This category can receive additional promotional focus.

### Channel Strategy
Online purchases generated the highest total purchase amount. Digital marketing and online promotions can therefore be prioritized.

## Project Structure

```text
Customer Data Analysis/
│
├── task4_customer_analysis.py
├── cleaned_customer_data.csv
├── customer_segments.csv
├── customer_segment_summary.csv
├── business_insights.txt
├── business_summary.csv
├── product_category_analysis.csv
├── location_analysis.csv
├── loyalty_analysis.csv
├── purchase_channel_analysis.csv
├── age_group_analysis.csv
├── README.md
│
└── charts/
    ├── sales_by_product_category.png
    ├── sales_by_location.png
    ├── sales_by_loyalty_status.png
    ├── sales_by_purchase_channel.png
    ├── customers_by_age_group.png
    ├── income_vs_purchase_amount.png
    ├── spending_score_distribution.png
    ├── customer_segmentation.png
    └── sales_by_customer_segment.png

🎯 **Internship**

This project was completed for the CodSoft Data Analytics Internship – Task 4.
