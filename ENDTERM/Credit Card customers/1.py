import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

file_path = r'C:\Data Preparation\Endterm\Credit Card customers\BankChurners.csv'
df = pd.read_csv(file_path)

df_cleaned = df.dropna()
df_cleaned = df_cleaned.drop_duplicates()


# 1.
total_customers = len(df_cleaned)
print(f"Total number of customers: {total_customers}")

# 2.
average_age = df_cleaned['Customer_Age'].mean()
print(f"Average age of customers: {average_age:.2f}")

# 3. 
gender_distribution = df_cleaned['Gender'].value_counts()
print("Gender distribution:")
print(gender_distribution)

# 4. 
income_distribution = df_cleaned['Income_Category'].value_counts()
print("Income category distribution:")
print(income_distribution)

# 5.
average_credit_limit = df_cleaned['Credit_Limit'].mean()
print(f"Average credit limit: ${average_credit_limit:.2f}")

# 6. 
high_utilization_customers = len(df_cleaned[df_cleaned['Avg_Utilization_Ratio'] > 0.8])
print(f"Number of customers with high utilization ratio (> 0.8): {high_utilization_customers}")

# 7. 
attrition_rate = (df_cleaned['Attrition_Flag'].value_counts(normalize=True)['Attrited Customer'] * 100)
print(f"Attrition rate: {attrition_rate:.2f}%")

# 8.
education_levels = df_cleaned['Education_Level'].value_counts().head(5)
print("Top 5 education levels by customer count:")
print(education_levels)

# 9. 
high_credit_customers = len(df_cleaned[df_cleaned['Credit_Limit'] > 10000])
print(f"Number of customers with credit limit > $10,000: {high_credit_customers}")

# 10. 
average_months_on_book = df_cleaned['Months_on_book'].mean()
print(f"Average months on book: {average_months_on_book:.2f}")

# 11. 
total_revolving_balance = df_cleaned['Total_Revolving_Bal'].sum()
print(f"Total revolving balance across all customers: ${total_revolving_balance:.2f}")

# 12. 
average_transaction_amount = df_cleaned['Total_Trans_Amt'].mean()
print(f"Average transaction amount: ${average_transaction_amount:.2f}")

# 13. 
correlation_age_credit = df_cleaned['Customer_Age'].corr(df_cleaned['Credit_Limit'])
print(f"Correlation between age and credit limit: {correlation_age_credit:.2f}")

# 14. 
high_transaction_customers = len(df_cleaned[df_cleaned['Total_Trans_Ct'] > 50])
print(f"Number of customers with more than 50 transactions: {high_transaction_customers}")

# 15. 
married_customers_percentage = (df_cleaned['Marital_Status'].value_counts(normalize=True)['Married'] * 100)
print(f"Percentage of married customers: {married_customers_percentage:.2f}%")

# 16. 
top_card_categories = df_cleaned['Card_Category'].value_counts().head(5)
print("Top 5 card categories by customer count:")
print(top_card_categories)

# 17. 
average_transaction_count = df_cleaned['Total_Trans_Ct'].mean()
print(f"Average number of transactions per customer: {average_transaction_count:.2f}")

# 18. 
significant_transaction_changes = len(df_cleaned[df_cleaned['Total_Ct_Chng_Q4_Q1'] > 2.0])
print(f"Number of customers with significant changes in transaction count (> 2.0): {significant_transaction_changes}")
